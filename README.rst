Smuggle
=======

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
   
   MySmuggler = Smuggler()
   
   aList = [1,2,3]
   aDict = {'a' : 1, 'b' : 2, 'c' : 3}
   
   MySmuggler.smuggler(MyList=aList,MyDict=aDict)
   
   print MySmuggler.passphrases
   

Requirements
============

Python
------
Works on 2.7, untested on all other versions.
It is expected to be ported to 3.4 soon, and likely 2.6 as well.

Install (OSX, Linux, Posix)
===========================

The easiest way to install is with pip::

    sudo pip install smuggle

Or manually (assuming all required modules are installed on your system)::

    sudo python ./setup.py install
   
Instructions for Windows
========================

1) Make sure you have Python 2.7 and pip installed
2) Open the command prompt: Start Menu > Accessories > Command Prompt
3) Run the following command:: ``pip install smuggle``