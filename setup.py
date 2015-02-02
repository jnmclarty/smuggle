import os

from setuptools import setup

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

print "Setting up smuggle"

setup(
  name = 'smuggle',
  version = '0.1',
  description = 'Log, catalogue, and move python objects via pickling',
  long_description=(read('README.rst')),
  author = 'Jeffrey McLarty',
  author_email = 'jeffrey.mclarty@gmail.com',
  url = 'https://github.com/jnmclarty/smuggle',
  download_url = 'https://github.com/jnmclarty/smuggle/tarball/0.1',
  py_modules=['smuggle'],
  include_package_data=True,
  keywords = ['debugging', 'logging', 'smuggle', 'smuggler', 'exception', 'pickle', 'pickling'],
  classifiers = ['Development Status :: 4 - Beta',
                 'Topic :: Office/Business',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Software Development',
                 'Topic :: System :: Logging',
                 'Topic :: Utilities'])