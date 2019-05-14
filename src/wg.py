import getopt
import sys

version = '0.1'


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
    print("yes")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        help()
