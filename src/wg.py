import getopt
import sys
import os

version = '1.0'


def help():
    print("\n## WORDLIST GENERATOR ##\n")
    print("[ Options ]\n")
    print("-o\tName output file. Remember .txt or .csv")
    print("-k\tKeywords separated by commas. Do not use spaces")
    print('-i\tInclude "wordlist-top4800-probable.txt" at the end of your custom list')
    print("-v\tVersion of the program\n")
    sys.exit()


def main(argv):
    include_top = False
    output = ''
    seeds = ''
    try:
        opts, args = getopt.getopt(argv, "hvik:o:", ["seeds=", "output="])
    except getopt.GetoptError:
        print("invalid command")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-v':
            print("Version: " + version)
            sys.exit()
        elif opt == '-h':
            help()
        elif opt == '-i':
            include_top = True
        elif opt in "-k":
            seeds = arg
        elif opt in "-o":
            output = arg
    keywords = seeds.split(",")
    if len(keywords) > 0 and len(output) > 0:
        generate_file(keywords, output, include_top)
    else:
        sys.exit("lack of arguments")


def generate_file(keys, filename, include_top):
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

        if include_top:
            with open("wordlist-top4800-probable.txt") as infile:
                for line in infile:
                    _file.write(line)
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
