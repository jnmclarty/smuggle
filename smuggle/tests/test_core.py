from smuggle import Smuggler
from datetime import datetime as dt
import shutil

import nose

def test_smuggle():
    
    s = Smuggler('testdir')
    x = [1,2,3]
    s.smuggle(x=x)
    pp = s.passphrases()
    shutil.rmtree('testdir')
    
    lines = pp.split("\n")[-4:-1]
    
    fmt1 = "%H:%M:%S, %Y/%m/%d"
    fmt2 = "%Y-%m-%d-%H-%M-%S"
    
    adt = dt.strptime(lines[0][-20:],fmt1)
    dfmt1 = adt.strftime(fmt1)
    dfmt2 = adt.strftime(fmt2)
    
    exp_out = \
        ["# x of type 'list' was smuggled at {}".format(dfmt1),
         "#   [1, 2, 3]",
         'x = pickle.load(open(r"testdir\\x-{}.smug","rb"))'.format(dfmt2)]
                    
    for i,(line,exp) in enumerate(zip(lines,exp_out)):
        if line != exp:
            raise Exception("Line {}, {} != {}".format(i+1,line,exp))
    
    

        
if __name__ == '__main__':
    nose.runmodule(argv=[__file__, '-vvs', '-x'],#, '--pdb-failure'],
                   exit=False)    