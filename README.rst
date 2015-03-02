Smuggle
=======

.. image:: https://travis-ci.org/jnmclarty/smuggle.svg?branch=master
    :target: https://travis-ci.org/jnmclarty/smuggle
    
.. image:: https://coveralls.io/repos/jnmclarty/smuggle/badge.svg 
    :target: https://coveralls.io/r/jnmclarty/smuggle

*Catalogue python pickles to reduce development and troubleshooting time.*

Description
===========

Smuggle organizes copies of python objects chronologically, 
using the pickle format, so that they can be retrieved in 
a new python session. This allows new approaches during development and 
troubleshooting production issues.  Since objects can be moved from
a prod to dev environment, smuggle becomes exceptionally handy for projects
involving complicated cases or non-idempotent processes.

When used correctly, it can also reduce the need for verbosity in logging
and certain types of error messages.

Usage
=====

.. code:: python

   from smuggle import Smuggler
   
   MySmuggler = Smuggler("C:\MyObjectLogFolder")
   
   aList = [1,2,3]
   aDict = {'a' : 1, 'b' : 2, 'c' : 3}
   
   MySmuggler.smuggle(MyList=aList,MyDict=aDict,NoteToSelf="This is cool")
   
   print(MySmuggler.passphrases())

Output
======

There are two forms of output & access; passphrases and payloads.

Passphrase
----------

A passphrase is just auto-generated python code, which looks like this:

.. code:: python

    import pickle
    
    # NoteToSelf of type 'str' was smuggled at 21:02:06, 2015/02/01
    #   'This is cool'
    NoteToSelf = pickle.load(open(r"C:\MyObjectLogFolder\NoteToSelf-2015-02-01-21-02-06.smug","rb"))
    
    # MyList of type 'list' was smuggled at 21:02:06, 2015/02/01
    #   [1, 2, 3]
    MyList = pickle.load(open(r"C:\MyObjectLogFolder\MyList-2015-02-01-21-02-06.smug","rb"))
    
    # MyDict of type 'dict' was smuggled at 21:02:06, 2015/02/01
    #   {'a': 1, 'c': 3, 'b': 2}
    MyDict = pickle.load(open(r"C:\MyObjectLogFolder\MyDict-2015-02-01-21-02-06.smug","rb"))

This output is just a copy+paste away from functioning in a new 
python file.

Payload
-------

A payload is a collection of organized pickles accessible via the catalogue functions.
There are many plans to expand the catalogue system (eg. SQLite, keyword,
time, etc.).  The current system is limited to a very simple file naming convention
which includes the time and date.  Payloads just scan a folder for ``.smug``
files.  These files, are simply pickle files.  No other changes are made to the file
format.

.. code:: python

    >>> MyPayload = Payload("C:\MyObjectLogFolder")
    >>> varlist = MyPayload.aslist()
    >>> varlist
    [{'a': 1, 'c': 3, 'b': 2}, [1, 2, 3], 'This is cool']
   

Requirements
============

Python
------
Works on 2.6, 2.7, 3.3 and 3.4.

Install (OSX, Linux, Posix)
===========================

The easiest way to install is with pip::

    sudo pip install smuggle

Or manually (assuming all required modules are installed on your system)::

    sudo python ./setup.py install
   
Instructions for Windows
========================

1) Start Menu > Accessories > Command Prompt
2) Run the following command: ``pip install smuggle``

Contributing
============

Pull requests are welcome.  To test, use ``nosetests smuggle`` or ``py.test``.