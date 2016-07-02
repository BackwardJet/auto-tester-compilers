### This script is a variation of https://github.com/tejvuligonda/Utility-Scripts/blob/master/Compare%20Files/compare_files_terminal.py
import sys
import os.path

f1 = sys.argv[1]
f2 = sys.argv[2]

def open_files():

    if (not (os.path.isfile(f1))):
        print('The first path does not lead to a valid file.')
        return
    if (not (os.path.isfile(f2))):
        print('The second path does not lead to a valid file.')
        return
    with open(f1) as file1_read:
        file1 = file1_read.readlines()
    with open(f2) as file2_read:
        file2 = file2_read.readlines()
    compare(file1,file2)

def compare(file1,file2):
    # file2 is the user-created output file
    file2 = file2[5:] # skips the first 5 lines (SPIM preamble) 
    '''if (len(file1) != len(file2)):
        print('NOT EQUAL: The files do not have the same number of lines.')
        return
    '''
    for i in range(len(file1)):
        line1_f1 = file1[i]
        line1_f2 = file2[i]
        if line1_f1 != line1_f2:
            print('ERROR: NOT EQUAL', f1, f2)
            line1_f1 = '"' + ' '.join(line1_f1.split()) + '"'
            line1_f2 = '"' + ' '.join(line1_f2.split()) + '"'
            string_to_print = line1_f1 + ' != ' + line1_f2
            print(string_to_print)
            return
    print('ALL EQUAL')

if __name__ == '__main__':
    open_files()
    
