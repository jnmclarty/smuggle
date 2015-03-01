from smuggle import Smuggler, Payload
from datetime import datetime as dt
from unittest import TestCase

import time, shutil, os, nose

class SmugglerTests(TestCase):
  
    def setUp(self):
        if not os.path.exists('testdir'):
            os.makedirs('testdir')
        self.s = Smuggler('testdir')
        
    def tearDown(self):
        shutil.rmtree('testdir')
        
    def test_smuggling(self):

        x = [1,2,3]
        self.s.smuggle(x=x)
        pp = self.s.passphrases()
        
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

    def test_payload(self):
        
        x = [1,2,3]
        y = ['a','b','c']
        self.s.smuggle(x=x,y=y)
        
        #TODO handle sub one secon smuggle intervals
        time.sleep(1.5)
    
        a = [4,5,6]
        b = ['d','e','f']
        self.s.smuggle(x=a,y=b)
        
        
        p = Payload('testdir')
        
        msg = "Problem testing payloads"
        
        self.assertDictEqual({'x' : [x,a], 'y' : [y,b]},
                             p.asvardict(),msg)
                             
        self.assertListEqual([x, y, a, b],
                             p.aslist(),msg)

    def test_payload_destroy(self):
        
        x = [1,2,3]
        y = ['a','b','c']
        self.s.smuggle(x=x,y=y)
        
        #TODO handle sub one secon smuggle intervals
        time.sleep(1.5)
    
        a = [4,5,6]
        b = ['d','e','f']
        self.s.smuggle(x=a,y=b)
                
        p = Payload('testdir')
        
        self.assertEqual(4,p.destroy(verbose=False),"Problem destroying payloads")

if __name__ == '__main__':
    nose.runmodule(argv=[__file__, '-vvs', '-x'],exit=False) #, '--pdb-failure'],