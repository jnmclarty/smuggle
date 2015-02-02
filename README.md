# smuggle

### Catalogue python pickles to reduce development and troubleshooting time.

Smuggle organizes copies of python objects chronologically, 
using the pickle format, so that they can be retrieved in 
a new python session. This allows new approaches during development and 
troubleshooting production issues.  Since objects can be moved from
a prod to dev environment, smuggle becomes exceptionally handy for projects
involving complicated cases or non-idempotent processes.

When used correctly, it can also reduce the need for verbosity in logging
and certain types of error messages.

