import sys

def read_file(file):
    f = open(file,"r")
    lines = f.readlines()
    cities_list = []
    for line in lines:
        line = line.replace("\n","")
        cities_list.append(line)
    return cities_list

def main():
    cities_path = sys.argv[1]
    read_file(cities_path)

if __name__ == '__main__':
    main()
