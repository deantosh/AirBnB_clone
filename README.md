# PROJECT OVERVIEW

This project focuses on creating the File Storage to store the object created and a console that acts like
a command line interpreter that allows users to interact with the File Storage.

Console
-------
-------

An AirBnB console is a command interpreter used to manage our AirBnB objects. It mimicks the Shell
but limited to a specific use-case. In our case, the console is able to manage the objets our project:

  1. Create a new object (ex: a new User or a new Place)
  2. Retrieve an object from a file, a database etc…
  3. Do operations on objects (count, compute stats, etc…)
  4. Update attributes of an object
  5. Destroy an object

File Storage
------------
------------

As mentioned before it is used to manage a File Strorage. The File Storage in this case represent a database
that store objects created. The objects are created from the classes that defines the different attribute (data)
and method (functions) used to interact with the attributes.

Therefore the objects stored in this File Storage is more than just data.

Note: The reason for creating a File Storage is to ensure that it is persistent. Being persistent means that the previously
created objects are availeble when using the console at all times.

## COMMAND LINE INTERPRETER
