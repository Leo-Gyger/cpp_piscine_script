#!/usr/bin/python3
import  sys
import  os
import  re

def main():
    if len(sys.argv) < 3:
        print("Error, needs 2 or 3 arguments",file = sys.stderr)
        print("1. Name of the class",file = sys.stderr)
        print("2. Location where you want your files to be created",file = sys.stderr)
        print("3. (optional) name of the class that you want 1. to be a copy of with a new name",file = sys.stderr)
        quit()
    if len(sys.argv) == 4:
        createfolder(sys.argv[2])
        copy_replace()
        try:
            makefile = open("Makefile", mode='x')
            createmake(makefile)
        except:
            editmake()
            quit()
    try:
        createfolder(sys.argv[2])
        headerfile = open(sys.argv[1] + ".hpp",mode='x')
        classfile = open(sys.argv[1] + ".cpp",mode='x')
    except:
        print("Error file already exist", file = sys.stderr)
        quit()
    createheader(headerfile)
    createclass(classfile)
    try:
        makefile = open("Makefile",mode='x')
        createmake(makefile)
    except:
        editmake()

def copy_replace():
    with open(sys.argv[1] + ".hpp", mode='r') as header:
                text = header.read()
                ntext = re.sub(sys.argv[1], sys.argv[3], text)
                ntext = re.sub(sys.argv[1].upper(), sys.argv[3].upper(), ntext)
                with open(sys.argv[3] + ".hpp", mode='w') as nheader:
                    nheader.write(ntext)
    with open(sys.argv[1] + ".cpp", mode='r') as file:
                text = file.read()
                ntext = re.sub(sys.argv[1], sys.argv[3], text)
                with open(sys.argv[3] + ".cpp", mode='w') as nfile:
                    nfile.write(ntext)

def editmake():
    file = open("Makefile")
    lines = file.readlines()
    lines[7] = "\nFILES += {}.cpp\n".format(sys.argv[1])
    file.close()
    file = open("Makefile", 'w')
    file.writelines(lines)
    file.close()

def createfolder(path):
    path = os.path.join(os.getcwd(), path)
    os.makedirs(path, exist_ok = True)
    os.chdir(path)

def createheader(file):
    file.write("#ifndef {}_HPP\n".format(sys.argv[1].upper()))
    file.write("# define {}_HPP\n".format(sys.argv[1].upper()))
    file.write("# include <iostream>\n\n")
    file.write("class " + sys.argv[1] + "\n")
    file.write("{\n\t")
    file.write("private:\n\t\t")
    file.write("std::string var;\n\t")
    file.write("public:\n\t\t")
    file.write(sys.argv[1] + "();\n\t\t")
    file.write(sys.argv[1] + "(const {}& rhs);\n\t\t".format(sys.argv[1]))
    file.write(sys.argv[1] + "& operator=(const {}& rhs);\n\t\t".format(sys.argv[1]))
    file.write("~" + sys.argv[1] + "();\n")
    file.write("};\n\n")
    file.write("#endif")
    file.close()

def createclass(file):
    file.write("#include \"{}.hpp\"\n\n".format(sys.argv[1]))
    file.write("{}::{}(void): var()\n".format(sys.argv[1], sys.argv[1]))
    file.write("{\n")
    file.write("}\n\n")
    file.write("{}::{}(const {}& rhs): var(rhs.var)\n".format(sys.argv[1], sys.argv[1], sys.argv[1]))
    file.write("{\n")
    file.write("}\n\n")
    file.write("{}& {}::operator= (const {}& rhs)\n".format(sys.argv[1], sys.argv[1], sys.argv[1]))
    file.write("{\n\t")
    file.write("this->var = rhs.var;\n\t")
    file.write("return (*this);\n")
    file.write("}\n\n")
    file.write("{}::~{}(void)\n".format(sys.argv[1],sys.argv[1]))
    file.write("{\n")
    file.write("}\n\n")
    file.close()

def createmake(file):
    file.write('''CC = c++

CFLAGS = -Wall -Wextra -Werror -std=c++98 -o
NAME = {}
DIR_OBJ =   ./objs
FILES = main.cpp\\
        {}.cpp

all : $(NAME)

OBJ = $(FILES:%.cpp=%.o)
$(NAME): $(OBJ)
	$(CC) $(CFLAGS) $(NAME) $(FILES)
fclean: clean
	rm -rf $(NAME)
clean:	
	rm -f $(OBJ)
re: fclean clean all

.PHONY: clean fclean all re'''.format(sys.argv[2], sys.argv[1]))
    file.close()
main()
