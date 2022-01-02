import re

import env_utils
import subprocess

pathToBuild = "/home/note/zephyrproject/zephyr/samples/basic/fade_led/build"

local_project = "/home/note/zephyrproject/zephyr/samples/basic/fade_led"

initial_project_directory_key = "APPLICATION_SOURCE_DIR:PATH="


# returning the path where the project initially existed
def get_original_project_dir(filepath):
    # Opening the file using the Path function
    with open(filepath, "r") as file:
        while True:
            # Get next line from file
            line = file.readline()

            if re.search(initial_project_directory_key, line):
                return line.replace(initial_project_directory_key, "").replace("\n", "")

            # if line is empty
            # end of file is reached
            if not line:
                print("no original dir found")
                exit(1)


# noinspection PyShadowingNames
def run(pathToBuild, local_project):
    initial_project = get_original_project_dir(f"{pathToBuild}/CMakeCache.txt")

    all_paths = env_utils.get_all_filepaths_in_path(pathToBuild)

    for filepath in all_paths:
        env_utils.replace_all_in_file(filepath, initial_project, local_project, True)


def add_needed_events_to_list(event_list, pathToBuild, local_project):
    initial_project = get_original_project_dir(f"{pathToBuild}/CMakeCache.txt")

    all_paths = env_utils.get_all_filepaths_in_path(pathToBuild)

    for filepath in all_paths:
        env_utils.add_thread_event_to_list(event_list, filepath, initial_project, local_project, True)