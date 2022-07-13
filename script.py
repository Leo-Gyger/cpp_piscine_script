#!/usr/bin/python3
import  sys


def main():
    if len(sys.argv) < 2:
        print("Error, needs 1 argument",file = sys.stderr)
        print("1. Name of the class",file = sys.stderr)
        quit()
    try:
        headerfile = open(sys.argv[1] + ".hpp",mode='x')
        classfile = open(sys.argv[1] + ".cpp",mode='x')
        makefile = open("Makefile",mode='x')
    except:
        print("Error file already exist", file = sys.stderr)
        quit()
    createheader(headerfile)
    createclass(classfile)
    createmake(makefile)


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
NAME = ex00
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

.PHONY: clean fclean all re'''.format(sys.argv[1]))
    file.close()
main()
