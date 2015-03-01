from smuggle import Smuggler, Payload
from datetime import datetime as dt
from unittest import TestCase

import time, shutil, os, nose

class SmugglerTests(TestCase):
  
    def setUp(self):
        self.testdir = os.path.join(os.path.dirname(__file__),"testdir")
        
        if not os.path.exists(self.testdir):
            os.makedirs(self.testdir)
        self.s = Smuggler(self.testdir)
        
    def tearDown(self):
        shutil.rmtree(self.testdir)
        
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
        
        exp_file = os.path.join(self.testdir,"x-" + dfmt2) + ".smug"
        
        exp_out = \
            ["# x of type 'list' was smuggled at {}".format(dfmt1),
             "#   [1, 2, 3]",
             'x = pickle.load(open(r"{}","rb"))'.format(exp_file)]
                        
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
        
        
        p = Payload(self.testdir)
        
        msg = "Problem testing payloads"

        def sorteddictoflists(d):
            for key in d.keys():
                d[key] = [item for sublist in d[key] for item in sublist]
                d[key].sort()
            return d
            
        exp = sorteddictoflists({'x' : [x,a], 'y' : [y,b]})
        act = sorteddictoflists(p.asvardict())
        
        self.assertDictEqual(exp,act,msg)
                             
        exp = [x, y, a, b]
        act = p.aslist()
        
        exp = [item for sublist in exp for item in sublist]
        act = [item for sublist in act for item in sublist]
        
        exp.sort()
        act.sort()
        
        self.assertListEqual(exp,act,msg)

    def test_payload_destroy(self):
        
        x = [1,2,3]
        y = ['a','b','c']
        self.s.smuggle(x=x,y=y)
        
        #TODO handle sub one secon smuggle intervals
        time.sleep(1.5)
    
        a = [4,5,6]
        b = ['d','e','f']
        self.s.smuggle(x=a,y=b)
                
        p = Payload(self.testdir)
        
        #for name in list(os.listdir(self.testdir)) + ['Done']:
        #    print name
        #print len([name for name in os.listdir('testdir') if os.path.isfile(name)])
        
        #print p.destroy(verbose=False)
        num_del = p.destroy(verbose=False)
        #print num_del
        exp_num_del = 4

        #for name in list(os.listdir(self.testdir)) + ['Done']:
        #    print name
        
        self.assertEqual(exp_num_del,num_del,"Problem destroying payloads")

if __name__ == '__main__':
    nose.runmodule(argv=[__file__, '-vvs', '-x'],exit=False) #, '--pdb-failure'],