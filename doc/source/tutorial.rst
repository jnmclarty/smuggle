Smuggle Tutorial
================
This tutorial is just the start, but the framework is more or less complete.  It's broken down into the application usage, and the troubleshooting usage.

Application Usage
-----------------
It all starts with an application which will create picklable objects.  Getting a troubleshooting boost
is as easy as instantiating a Smuggler, then smuggling out the interesting objects.  Using the passphrases
is optional.

(Smuggler) Instantiation
^^^^^^^^^^^^^^^^^^^^^^^^
First, we need to instantiate a Smuggle object.  This happens in just one line. This is how...

(Contraband) Archiving & Cataloguing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Second, we smuggle.  "Archiving & Cataloguing" is a synonym for smuggling.  This happens in just one line. This is how...

(Passphrase) Output
^^^^^^^^^^^^^^^^^^^
Third, and optionally, use the passphrases in any output stream.  Although optional, it's highly recommended.

Troubleshooting Usage
---------------------
Using the passphrases as input, or inspecting the payload, occurs only after an application
has implemented and used a smuggler at least once. 

(Passphrase) Input
^^^^^^^^^^^^^^^^^^
Simply copy and paste from wherever the passphrases appear.  An error message? A log? A traceback? A print statement?

(Payload) Inspecting
^^^^^^^^^^^^^^^^^^^^
One can only inspect a payload
that's been created by an application using smuggler.  It can be sorted by variable name, timestamp, etc.