import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    # using a list might include duplicate file names.  A set may be a better suited.
    matchingFiles = list()

    # get a list of all files in the root directory
    dirList = os.listdir(path)

    # loop through all files/directories in dirList
    for file in dirList:
        fullPath = os.path.join(path, file)  # get the full path
        if os.path.isdir(fullPath):   # if the file is a directory, find all the files within
            matchingFiles = matchingFiles + find_files(suffix, fullPath)
        elif os.path.isfile(fullPath):  # it is a file
            if fullPath.endswith(suffix):
                matchingFiles.append(file)
        else:
            pass

    return matchingFiles


# TEST CASES

print(find_files('.c', '/Users/jwl/Downloads/testdir'))  # should return all files ending in .c
print(find_files('c', '/Users/jwl/Downloads/testdir'))   # should return all files ending in .c
print(find_files('C', '/Users/jwl/Downloads/testdir'))   # should return an empty list
print(find_files('c', ''))                               # will generate a FileNotFoundError, due to empty path



