# -*- coding: utf-8 -*-

import os
import pickle
from datetime import datetime as dt

#TODO Rebuild all with SQLite
#TODO Enable more options for passphrase output
#TODO Documentation
#TODO Organize the module and use __init__ better
#TODO Implement Coveralls
#TODO Make exception-pretty output
#TODO Enable other time-date formats
#TODO Implement a DEBUG mode.
#TODO ...lots more.

def parsefname(f):
    tmp = f.replace(".smug","")
    tmp = tmp.split("-")
    
    varname = tmp[0]
    date = dt.strptime(" ".join(tmp[1:7]), "%Y %m %d %H %M %S")
    
    if len(tmp) >= 7 :
        post = "-".join(tmp[7:])
    else:
        post = None
        
    return varname, date, post

def startswithany(st,li):
    for l in li:
        if st.startswith(l + "-"):
            return True
    return False
        
class Payload(object):
    def __init__(self,folder=None):
        self.cargo = []
        self.folder = folder
        if folder != None:
            for f in os.listdir(folder):
                if f.endswith(".smug"):
                    #print "Doing {}".format(f)
                    varname, date, post = parsefname(f)
                    #print varname, date, post
                    var = pickle.load(open(os.path.join(folder,f),"rb"))
                    c = Contraband(varname, var)
                    c.setdate(date)
                    c.setfname(varname, post)
                    c.setfpath(folder)
                    self.cargo.append(c)
        
        #TODO Make Smuggle work with seconds
        #for c in self.cargo:
        #    print c.dt
            
    def passphrases(self):
        """
        Returns a string, which is executable python code.
        The code sets up access to the recently smuggled objects.
        """
        msg = "\nimport pickle\n\n"
        phrases = "\n".join([c.getpassphrase() for c in self.cargo[::-1]])
        msg = msg + phrases 
        return msg
    def asvardict(self):
        """
        A dictionary of lists where the keys are variables, 
        the lists organized chronologically
        """
        tmp = {}
        for c in self.cargo:
            tmp[c.name] = []
        
        for c in self.cargo:
            tmp[c.name].append((c.dt,c.obj))
        
        for varname in list(tmp.keys()):
            tmp[varname] = sorted(tmp[varname],key=lambda x: x[0])
            tmp[varname] = [x[1] for x in tmp[varname]]
        
        return tmp
    def astimevardict1D(self):
        """
        Returns a 1D dictionary where the keys are a tuple (time,varname)
        """
        tmp = {}
        for c in self.cargo:
            tmp[(c.dt,c.name)].append(c.obj)
        return tmp
    def astimevardict2D(self):
        """a 2D dictionary where the keys are time, then varname"""
        tmp = {}
        for c in self.cargo:
            tmp[c.dt] = {}
        
        for c in self.cargo:
            tmp[c.dt][c.name] = c.obj
               
        return tmp  
    def asvartimedict2D(self):
        """a 2D dictionary where the keys are varname, then time"""
        tmp = {}
        for c in self.cargo:
            tmp[c.name] = {}
        
        for c in self.cargo:
            tmp[c.name][c.dt] = c.obj
               
        return tmp        
    def aslist(self,objnames=['ALLVARS']):
        """a chronologically ordered list of the available objects"""
        tmp = []
        
        for c in self.cargo:
            if objnames[0] == 'ALLVARS' or c.name in objnames:
                tmp.append((c.dt,c.obj))
        
        tmp = sorted(tmp,key=lambda x: x[0])
        tmp = [x[1] for x in tmp]
        
        return tmp
    def destroy(self,objnames=['ALLVARS'],verbose=True):
        """delete old pickle files from disk"""
        num = 0
        for f in os.listdir(self.folder):
            if f.endswith(".smug"):
                if objnames[0] == 'ALLVARS' or startswithany(f,objnames):
                    if verbose:
                        print(os.path.join(self.folder,f))
                    os.remove(os.path.join(self.folder,f))
                    num += 1
        return num

class Contraband(object):
    """
    Contains properties of, and the actual, object being smuggled.
    
    parameters
    ----------
    name : str
        the name of the object being smuggled
    
    obj : obj
        any picklable object.
    """
    def __init__(self,name,obj):
        self.setdate()
        self.dt_str = self.dt.strftime("%Y-%m-%d-%H-%M-%S")
        self.dt_human = self.dt.strftime("%H:%M:%S, %Y/%m/%d")
        self.name = name
        self.obj = obj
        self.fpath = ""
        self.setfname(name)
    def setdate(self,d=None):
        if d == None:
            self.dt = dt.now()
        else:
            self.dt = d
        self.dt_str = self.dt.strftime("%Y-%m-%d-%H-%M-%S")
        self.dt_human = self.dt.strftime("%H:%M:%S, %Y/%m/%d")
    def setfname(self,s="",post=""):
        tmp = s or self.name
        tmp = [tmp,self.dt_str,post]
        tmp = [x for x in tmp if not (x == '' or x == None)]
        self.fname = "-".join(tmp) + ".smug"
        self.setfout()
    def setfpath(self,p):
        self.fpath = p
        self.setfout()
    def setfout(self):
        self.fout = os.path.join(self.fpath,self.fname)
    def getpassphrase(self):
        dtls = (self.name,type(self.obj).__name__,self.dt_human)
        msg = "# {0} of type '{1}' was smuggled at {2}".format(*dtls)
        
        rep = repr(self.obj)
        if rep is not None:
            rep = rep.split("\n")
            if len(rep) == 1:
                msg += "\n#   {0}\n".format(rep[0])
            else:
                msg += "\n#   ".join(rep)
                msg += "\n"
        else:
            msg += "\n#   None"
        code_details = (self.name,self.fout)
        msg += '{0} = pickle.load(open(r"{1}","rb"))\n'.format(*code_details)
        return msg
        
class Smuggler(object):
    """
    The main object responsible for smuggling individual objects later on.
    
    parameters
    ----------
    
    folder : str, optional
        absolute path or defaults to the current working 
        directory + '\contraband'
    
    post : str, optional
        a unique string appended to the end 
    
    
    >>> MySmuggler = Smuggler()

    """  
    def __init__(self,folder=None,post=""):
        #TODO make this more flexible, and work for all operating systems.
        self.folder = folder or os.join(os.getcwd(),'contraband')
        self.post = post

        if self.folder[-1] == '\\':
            self.folder = self.folder[:-1]
            
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
        
        self.payload = Payload()
    def smuggle(self,**kwargs):
        """
        pickle and catalogue all the objects passed in using the argument name
        as a label.
        
        >>> Smuggler.smuggle(myobj=obj,myotherobj=otherobj)
        
        ...will use the strings 'myobj' and 'myotherobj'
        """
        
        for varname,var in kwargs.items():
            #print "Trying to write var {}".format(varname)
            c = Contraband(varname,var)
            c.setfname(post=self.post)
            c.setfpath(self.folder)
            pickle.dump(var,open(c.fout,'wb'))
            #print "Sucessfully wrote pickle : {}".format(c.fout)
            self.payload.cargo.append(c)
        return self
    def flushpassphrases(self):
        phrases = self.payload.passphrases()
        self.payload.cargo = []
        return phrases
    
    def passphrases(self):
        phrases = self.payload.passphrases()
        return phrases

   
if __name__ == '__main__':

    #Example one:
    HanSolo = Smuggler("C:\Smuggle")
    HanSolo.smuggle(foo="foo stuff", boo="boo stuff")
    print(HanSolo.passphrases())
    HanSolo.smuggle(foo="more foo stuff", boo="more boo stuff")
    print(HanSolo.flushpassphrases())
    HanSolo.smuggle(foo="even more foo stuff", boo="even more boo stuff")
    print(HanSolo.passphrases())
    
    #Example two:
    HanSolo = Smuggler("C:\Smuggle")
    try:
        foo, bar = "Some Foo go goo", "Well bar dee do"
        adict = {'A' : ['a','Eh'], 'B' : ['b','Bee'], 'C' : ['c','See'] }
        i, j, k = 1, 10, 100
        DoSomethingExceptional()
    except:
        HanSolo.smuggle(foo=foo,            # plain vanilla,
                        bar=bar.split(" "), # hacked up, if needed
                        mydict=adict,       # renamed? sure!
                        num=i+j+k+1000)     # caculation, ok!
        ErrorMsg = "Don't Do Exceptional Things!\n" + HanSolo.passphrases()
        #raise Exception(ErrorMsg)

    #Reading a payload:        
    MyPayload = Payload("C:\Smuggle")
    VarTimeDict = MyPayload.asvartimedict2D()
    
    for varname in list(VarTimeDict.keys()):
        for datetime in list(VarTimeDict[varname].keys()):
            print(varname, datetime, VarTimeDict[varname][datetime])