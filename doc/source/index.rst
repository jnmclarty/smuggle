.. Smuggle documentation master file, created by
   sphinx-quickstart on Sun Feb 08 09:10:25 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Smuggle
=======

Organize Python Pickles by logging and cataloguing, enabling new approaches for debugging, troubleshooting & archiving.

.. toctree::
   :maxdepth: 2
   
   tutorial
   smuggle <reference>
   modules

Why?
----
Reduce Development Time
"""""""""""""""""""""""
Eliminate guessing which details will be needed in error messages. Eg. No need for this:
``ErrorMsg = “ERROR : object’s important attribute = {0}”.format(obj.attribute)``
   
Reduce Debugging Time
"""""""""""""""""""""
Eliminate recreation of error cases in order to simply identify root causes. 
Investigate how an object has changed over time. 
Logs are great, so are commit diffs, but object differences can shed light on changes extremely quickly.
   
Reduce Down Time
""""""""""""""""
Move production objects to new sessions and scripts on development environments.

Archive & Cache
"""""""""""""""
The pickles are store until deleted, so it could be used where simple backups or caching is needed.

Nomenclature
------------
Smuggler
   Pickler + Cataloguer of Objects
   *[Writer Object]*

Smuggle 
   The Action of Pickling + Cataloguing
   *[Writing Process]*
    
Contraband   
   Object getting Pickled + Catalogued
   *[Any Object (which can be pickled)]*
    
Payload 
   Catalogue Reader + Pickle Loader
   *[Reader Object == List of Contraband]*
    
Passphrase
   Prebuilt python code to load a catalogued pickle
   *[Access Code to Object]*   

Features
--------

- Easily Pickle Objects
- Easily Catalogue Pickles
- Easily Read the Pickles
- Easily Read the Catalogue

Installation
------------

Install smuggle by running:

    ``pip install smuggle``
    
Roadmap
-------
#. Organize the module & documentation
#. Write Documentation
#. Write Tests
#. Enable support for Python 3
#. Improve the API
#. Add a file-based indexing approach (instead of filename-based)
#. Add a SQLite indexing approach

Contribute
----------

- Issue Tracker: https://github.com/jnmclarty/smuggle/issues
- Source Code: https://github.com/jnmclarty/smuggle

Support
-------

If you are having issues, please let us know via a GitHub issue
or e-mail to me, at firstname.lastname@gmail.com.  My name is Jeffrey McLarty.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

