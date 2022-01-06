import os.path
import re

regex_value_pattern = re.compile(r"^(.+)=(.+)$")

return_dir = dict()


# reads a line in and finds the first instance of a search result for the given regex pattern
# and then adds it to the directory (key given is the first grouping of the value pattern)
def set_value_if_existent(_dict: dict, regex: re, string: str):
    for result in regex.finditer(string):
        _dict[result.group(1)] = result.group(2)
    pass


# configuration reader for rework scripts
def read_from_env(path):
    if not os.path.exists(path):
        raise IOError(f"Configuration file could not be found, Path: {path} doesn't exist")

    with open(path, "r") as file:
        if not file.readable():
            raise IOError(f"Configuration file could not be read, Path: {path} ")

        while True:
            # Get next line from file
            line = file.readline()

            # if line is empty
            # end of file is reached
            if not line:
                return return_dir

            set_value_if_existent(return_dir, regex_value_pattern, line)
