import re

from specific_utils import env_utils

initial_toolchain_installation_key = "ZEPHYR_SDK_INSTALL_DIR:PATH="


# returning the dir where the toolchain was initially installed when the build took place
def get_initial_toolchain_dir(filepath):
    # Opening the file using the Path function
    with open(filepath, "r") as file:
        while True:
            # Get next line from file
            line = file.readline()

            if re.search(initial_toolchain_installation_key, line):
                return line.replace(initial_toolchain_installation_key, "").replace("\n", "")

            # if line is empty
            # end of file is reached
            if not line:
                print("no original dir found")
                exit(1)


def run(pathToBuild, toolchain_path):
    initial_toolchain_installation = get_initial_toolchain_dir(f"{pathToBuild}/CMakeCache.txt")

    all_paths = env_utils.get_all_filepaths_in_path(pathToBuild)

    for filepath in all_paths:
        env_utils.replace_all_in_file(filepath, initial_toolchain_installation, toolchain_path, False)

    pass


def add_needed_events_to_list(event_list, pathToBuild, toolchain_path):
    initial_toolchain_installation = get_initial_toolchain_dir(f"{pathToBuild}/CMakeCache.txt")

    if initial_toolchain_installation == toolchain_path:
        print("no need to relink the toolchain installation path since it's the same than the initial one")

    all_paths = env_utils.get_all_filepaths_in_path(pathToBuild)

    for filepath in all_paths:
        env_utils.add_thread_event_to_list(event_list, filepath, initial_toolchain_installation, toolchain_path, False)
