import re

from specific_utils import env_utils

initial_toolchain_path_key = "ZEPHYR_BASE:PATH="


# returning the original dir where the build took place
def get_original_zephyr_base_dir(filepath):
    # Opening the file using the Path function
    with open(filepath, "r") as file:
        while True:
            # Get next line from file
            line = file.readline()

            if re.search(initial_toolchain_path_key, line):
                return line.replace(initial_toolchain_path_key, "").replace("\n", "")

            # if line is empty
            # end of file is reached
            if not line:
                print("no original dir found")
                exit(1)


# noinspection PyShadowingNames
def run(pathToBuild, local_zephyr_base_installation):
    initial_zephyr_base = get_original_zephyr_base_dir(f"{pathToBuild}/CMakeCache.txt")

    all_paths = env_utils.get_all_filepaths_in_path(pathToBuild)

    for filepath in all_paths:
        env_utils.replace_all_in_file(filepath, initial_zephyr_base, local_zephyr_base_installation, False)


def add_needed_events_to_list(event_list, pathToBuild, local_zephyr_base_installation):
    initial_zephyr_base = get_original_zephyr_base_dir(f"{pathToBuild}/CMakeCache.txt")

    all_paths = env_utils.get_all_filepaths_in_path(pathToBuild)

    for filepath in all_paths:
        env_utils.add_thread_event_to_list(event_list, filepath, initial_zephyr_base,
                                           local_zephyr_base_installation, False)
