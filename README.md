# cpp_piscine_script

A script to automate the creation of a Makefile and of canonical classes in c++

## What does it do

This script creates one header file (with header guards) that has one class
that uses the name you passed as argument. This class follows the copelian
canonical standard and therefore has a default constructor, a copy constructor,
an overload of the assignment operator and a destructor.

It also creates the class file with all of the functions declared in the header
file in it. As well as a Makefile that will be edited each time you add
a new class in the same folder.

## Usage

Simply launch it as you would with any script (it has a shebang) and pass as
argument the name of the class you wish to create and pass as a second,
argument the location where you want your files to be created, for example:

```sh
./script.py cat ex00
```

will create the folder ex00 and add the files inside it.
