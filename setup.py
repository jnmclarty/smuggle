import os

from setuptools import setup

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

v = '0.2.0'

setup(
  name = 'smuggle',
  version = v,
  packages = ['smuggle'],
  description = 'Log, catalogue, and move python objects via pickling',
  long_description=(read('README.rst')),
  author = 'Jeffrey McLarty',
  author_email = 'jeffrey.mclarty@gmail.com',
  url = 'https://github.com/jnmclarty/smuggle',
  download_url = 'https://github.com/jnmclarty/smuggle/tarball/' + v,
  keywords = ['debugging', 'logging', 'smuggle', 'smuggler', 'exception', 'pickle', 'pickling'],
  classifiers = ['Development Status :: 4 - Beta',
                 'Topic :: Office/Business',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2.6',                 
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Topic :: Software Development',
                 'Topic :: System :: Logging',
                 'Topic :: Utilities'])