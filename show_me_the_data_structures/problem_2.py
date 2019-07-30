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

    # valid extensions
    valid_extensions = ['.c', '.h', 'c', 'h']

    if suffix not in valid_extensions:
        return f'Invalid extension, {suffix}. Please try again.'

    if path:
        # get a list of all files in the root directory
        dirList = os.listdir(path)
        if dirList:
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
        else:
            # empty directory
            return f'Empty directory, {path}. Please try again.'
    else:
        # invalid or null path
        return f'Invalid path or not specified, {path}. Please try again.'



# TEST CASES

print(find_files('.c', '/Users/jwl/Downloads/testdir'))  # should return all files ending in .c
print(find_files('c', '/Users/jwl/Downloads/testdir'))   # should return all files ending in .c
print(find_files('C', '/Users/jwl/Downloads/testdir'))   # should return Invalid extension message
print(find_files('h', '/Users/jwl/Downloads/testdir'))   # should return all files ending in .h
print(find_files('c', ''))                               # should return Invalid path message.
print(find_files('d', '/Users/jwl/Downloads/testdir'))   # should return Invalid extension message


