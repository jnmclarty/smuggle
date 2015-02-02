from distutils.core import setup
setup(
  name = 'smuggle',
  packages = ['smuggle'], # this must be the same as the name above
  version = '0.1',
  description = 'Log, catalogue, and move python objects via pickling',
  author = 'Jeffrey McLarty',
  author_email = 'jeffrey.mclarty@gmail.com',
  url = 'https://github.com/jnmclarty/smuggle',
  download_url = 'https://github.com/jnmclarty/smuggle/tarball/0.1',
  keywords = ['debugging', 'logging', 'smuggle', 'smuggler', 'exception', 'pickle', 'pickling'],
  classifiers = ['Development Status :: 4 - Beta',
                 'Topic :: Office/Business',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Software Development',
                 'Topic :: System :: Logging',
                 'Topic :: Utilities'],
)