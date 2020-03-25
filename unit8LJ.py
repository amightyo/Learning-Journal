# modified version of 'invert_dict()' function  From Section 11.5 of:
# Downey, A. (2015). Think Python: How to think like a
# computer scientist. Needham, Massachusetts: Green Tree Press.


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        for item in val:
            inverse[item] = key
    return inverse

# implement method to read from a ".txt" file


def readFile(filename):
    dictOut = dict()
    # open file in read mode
    with open(filename, 'r') as inputfile:
        # iterate over the file
        for line in inputfile.readlines():
            # using "," to split the line
            line = line.strip().split(',')
            dictOut[line[0]] = line[1:]
    # return dictOut as format of dictionary
    return dictOut
# implement method to write to a file


def writeFile(inverted_d, filename):
    # open the file in write mode
    with open(filename, 'w+') as invertedFile:
        # iterate over the dictionary
        for key, value in inverted_d.items():
            # write contents to file
            invertedFile.write(str(key)+':'+str(value)+'\n')


if __name__ == "__main__":
    # read data from file
    d = readFile('figureskating.txt')
    # display dictionary
    print("\n ***Dictionary***\n ", d)
    # get dictionary from invert_dict method
    invt_d = invert_dict(d)
    # display inverted dictionary
    print('\n ***Inverted Dictionary***\n', invt_d)
    # write content into a file
    writeFile(invt_d, 'Invt_FigureSkating_Dict.txt')
