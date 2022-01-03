import re

from flash_preparation import env_utils
import subprocess

initial_cmake_install_key = "CMAKE_COMMAND:INTERNAL="

events_to_run = list()


# returning the original dir where the build took place
def get_original_cmake_install_dir(filepath):
    # Opening the file using the Path function
    with open(filepath, "r") as file:
        while True:
            # Get next line from file
            line = file.readline()

            if re.search(initial_cmake_install_key, line):
                return line.replace(initial_cmake_install_key, "").replace("\n", "")

            # if line is empty
            # end of file is reached
            if not line:
                print("no original dir found")
                exit(1)


def get_local_cmake_install():
    command = ["whereis", "cmake"]  # command to be executed
    res = subprocess.check_output(command)  # system command
    return res.decode("utf-8").split(" ")[1]


# noinspection PyShadowingNames
def run(path_to_build, cmake_path=None):
    if cmake_path is None:
        cmake_path = get_local_cmake_install()

    initial_install = get_original_cmake_install_dir(f"{path_to_build}/CMakeCache.txt")

    all_paths = env_utils.get_all_filepaths_in_path(path_to_build)

    for filepath in all_paths:
        env_utils.replace_all_in_file(filepath, initial_install, cmake_path, True)


def add_needed_events_to_list(_thread_event_list, path_to_build, cmake_path=None):
    if cmake_path is None:
        cmake_path = get_local_cmake_install()

    initial_install = get_original_cmake_install_dir(f"{path_to_build}/CMakeCache.txt")

    all_paths = env_utils.get_all_filepaths_in_path(path_to_build)

    for filepath in all_paths:
        env_utils.add_thread_event_to_list(_thread_event_list, filepath, initial_install, cmake_path, True)

