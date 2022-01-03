import re

import argparse

from python_scripts.utils import env_utils

parser = argparse.ArgumentParser(description='build information')

original_dir_key = "APPLICATION_BINARY_DIR:PATH="

running_threads = list()


# returning the original dir where the build took place
def get_original_dir(filepath):
    # Opening the file using the Path function
    with open(filepath, "r") as file:
        while True:
            # Get next line from file
            line = file.readline()

            if re.search(original_dir_key, line):
                return line.replace(original_dir_key, "").replace("\n", "")

            # if line is empty
            # end of file is reached
            if not line:
                print("no original dir found")
                exit(1)


# run all threads in running_thread list
def run_preparations():
    for t in running_threads:
        t.start()

    for t in running_threads:
        t.join()


# gets arguments given from outside with the
def get_parser_args():
    parser.add_argument('--path-to-build', dest='pathToBuild', type=str,
                        help='path to the directory, where the build lies')
    parser.add_argument('--original-path', dest='original', type=str,
                        help='original path of build (optional)')

    return parser.parse_args()
    pass


def run_with_terminal_interaction():
    args = get_parser_args()
    if args.pathToBuild is None:
        parser.print_help()
        exit(1)
    env_utils.change_to_dir(args.pathToBuild)
    if args.original is None:
        original = get_original_dir(f"{args.pathToBuild}/CMakeCache.txt")
    else:
        original = args.original
    print(f"setup threads to update files with phrase: {original} -> {args.pathToBuild}")
    all_files = env_utils.get_all_filepaths_in_path()
    for filepath in all_files:
        env_utils.add_thread_event_to_list(running_threads, filepath, original, args.pathToBuild)
    print(f"{len(running_threads)} files will be scanned and updated")
    input("press <Enter> to start")
    run_preparations()
    print("done")


def run(pathToBuild, original=None):
    if original is None:
        original = get_original_dir(f"{pathToBuild}/CMakeCache.txt")

    all_files = env_utils.get_all_filepaths_in_path(pathToBuild)

    for filepath in all_files:
        env_utils.add_thread_event_to_list(running_threads, filepath, original, pathToBuild)

    run_preparations()


if __name__ == '__main__':
    run_with_terminal_interaction()


def add_needed_events_to_list(_thread_event_list, pathToBuild, original=None):
    if original is None:
        original = get_original_dir(f"{pathToBuild}/CMakeCache.txt")

    all_files = env_utils.get_all_filepaths_in_path(pathToBuild)

    for filepath in all_files:
        env_utils.add_thread_event_to_list(_thread_event_list, filepath, original, pathToBuild)

