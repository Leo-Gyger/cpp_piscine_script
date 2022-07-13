# cpp_piscine_script
a script to automate the creation of a Makefile and of canonical classes in c++

## What does it do
This script creates one header file (with header guards) that has one class
that uses the name you passed as argument. This class follows the copelian
canonical standard and therefore has a default constructor, a copy constructor,
an overload of the assignment operator and a destructor.

It also creates the class file with all of the functions declared in the header
file in it. As well as a Makefile

## Usage
Simply launch it as you would with any script (it has a shebang) and pass as
argument the name of the class you wish to create.
