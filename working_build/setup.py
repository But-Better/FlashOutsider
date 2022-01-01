import os
import re
import threading

from pathlib2 import Path

original_dir = "/home/notefox/zephyrproject/zephyr/buildhere"
build_dir = "/home/note/PycharmProjects/westflashs/testzephyr/zephyr/build"

original_dir_key = "APPLICATION_BINARY_DIR:PATH="

running_threads = list()


def get_original_dir():
    return original_dir

    # Opening the file using the Path function
    with open(f"{build_dir}/CMakeCache.txt", "r") as file:
        while True:
            # Get next line from file
            line = file.readline()

            if re.search(original_dir_key, line):
                return line.replace(original_dir_key, "")

            # if line is empty
            # end of file is reached
            if not line:
                print("no original dir found")
                exit(1)


def change_to_dir(directory):
    os.chdir(directory)
    pass


def update_file(filename, old, new):
    try:
        with open(filename, 'rt') as file:
            content = file.read()

    except UnicodeDecodeError:
        print(f"An error occurred in reading {filename}")
        return

    content = content.replace(old, new)

    with open(filename, 'wt') as file:
        file.write(content)

    print(f"replaced text in: {filename}")


def prepare_file_preparations(file_to_prepare):
    thread = threading.Thread(
        target=update_file, args=(file_to_prepare, original, build_dir)
    )

    running_threads.append(thread)


def run_preparations():
    for t in running_threads:
        t.run()


def get_all_filepaths_in_path(local_path="."):
    files = list()
    scan = os.scandir(local_path)
    for entry in scan:
        if entry.is_dir():
            for inner_entry in get_all_filepaths_in_path(entry.path):
                files.append(inner_entry)
        elif entry.is_file():
            files.append(entry.path)

    return files


if __name__ == '__main__':
    change_to_dir(build_dir)

    original = get_original_dir()

    print(f"setup threads to update files with phrase: {original}")

    all_files = get_all_filepaths_in_path()

    for path in all_files:
        prepare_file_preparations(path)

    print(f"{len(running_threads)} files will be scanned and updated")

    input("press <Enter> to start")

    run_preparations()

    print("done")
