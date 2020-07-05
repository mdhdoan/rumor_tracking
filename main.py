# Author: Minh
import csv, sys

def csv_delimitize(filename, new_content):
    file = open(filename, 'r')
    for lines in file:
        new_lines = lines.replace(' ', ',')
        new_content.append(new_lines)
    file.close()

def write_csv(f_name):
    new_content = []
    csv_delimitize(f_name, new_content)
    new_file = open('twitter_activity.csv', 'w')
    for line in new_content:
        new_file.write(line)
    new_file.close()
    
if __name__ == "__main__":
    f_name = sys.argv[1]
    write_csv(f_name)
    