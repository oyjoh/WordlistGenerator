import getopt
import sys
import os

version = '1.0'


def help():
    print("\n## WORDLIST GENERATOR ##\n")
    print("[ Options ]\n")
    print("-o\tname output file. example.txt")
    print("-k\tkeywords separated by commas. do not use spaces")
    print("-v\tVersion of the program\n")
    sys.exit()


def main(argv):
    output = ''
    seeds = ''
    try:
        opts, args = getopt.getopt(argv, "hvk:o:", ["seeds=", "output="])
    except getopt.GetoptError:
        print("invalid command")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-v':
            print(version)
        elif opt == '-h':
            help()
        elif opt in "-k":
            seeds = arg
        elif opt in "-o":
            output = arg
    keywords = seeds.split(",")
    if len(keywords) > 0 and len(output) > 0:
        generate_file(keywords, output)
    else:
        sys.exit("lack of arguments")


def generate_file(keys, filename):
    _file = open(filename, "w")
    number_of_lines = 0

    for key in keys:
        key.lower()
        for x in range(101):
            _file.write(str(key) + str(x) + "\n")
            number_of_lines += 1
        for x in range(101):
            _file.write(key.capitalize() + str(x) + "\n")
            number_of_lines += 1
        for x in range(101):
            _file.write(str(key) + str(x).zfill(3) + "\n")
            number_of_lines += 1
        for x in range(101):
            _file.write(key.capitalize() + str(x).zfill(3) + "\n")
            number_of_lines += 1
        for x in range(101, 1000):
            _file.write(str(key) + str(x) + "\n")
            number_of_lines += 1
        for x in range(101, 1000):
            _file.write(key.capitalize() + str(x) + "\n")
            number_of_lines += 1
    _file.close()
    print("\nFile successfully created!\n")
    print("Filepath: " + str(os.getcwd()) + "/" + str(filename))
    print("Number of lines: " + str(number_of_lines))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        help()
