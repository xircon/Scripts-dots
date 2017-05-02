#! /usr/bin/env python
from operator import itemgetter, attrgetter
import glob, os, sys

def sort_files_by_last_modified(files):
    """ Given a list of files, return them sorted by the last
         modified times. """
    fileData = {}
    for fname in files:
        fileData[fname] = os.stat(fname).st_mtime

    fileData = sorted(fileData.items(), key = itemgetter(1))
    return fileData 

def delete_oldest_files(sorted_files, keep = 3):
    """ Given a list of files sorted by last modified time and a number to 
        keep, delete the oldest ones. """
    delete = len(sorted_files) - keep
    for x in range(0, delete):
        print("Deleting: " + sorted_files[x][0])
        os.remove(sorted_files[x][0])

def print_usage():
    """ Print the usage message for the script. """
    print("""Deletes files other than the most recent.
Usage:
    delete_files '/path/to/files/pre_*.ext' <num_to_keep default=3>
    e.g. delete_files '/home/boggins/pictures/*.jpg' 5
delete_files -h prints this message.
    """)

if len(sys.argv) < 2 or sys.argv[1] == '-h':
    print_usage()
    sys.exit(1)

keep = 3

if len(sys.argv) > 2:
    keep = int(sys.argv[2])

# Find all files matching the path.
file_paths = glob.glob(sys.argv[1])

# Sort the files according to the last modification time.
sorted_files = sort_files_by_last_modified(file_paths)

delete_oldest_files(sorted_files, keep)

