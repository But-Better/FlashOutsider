import os
import threading


# list up all files existing in a path
#
# (this scan also lists up files in subdirectories,
# but not the directories itself)
def get_all_filepaths_in_path(local_path="."):
    files = list()
    scan = os.scandir(local_path)
    for entry in scan:
        # noinspection PyUnresolvedReferences
        if entry.is_dir():
            for inner_entry in get_all_filepaths_in_path(entry.path):
                files.append(inner_entry)
        elif entry.is_file():
            files.append(entry.path)

    return files


# scan through file and exchange old with new
def replace_all_in_file(filename, old, new, withOutput=False):
    try:
        with open(filename, 'rt') as file:
            content = file.read()

    except UnicodeDecodeError:
        if withOutput:
            print(f"An error occurred in reading {filename}")
        return

    content = content.replace(old, new)

    with open(filename, 'wt') as file:
        file.write(content)

    if withOutput:
        print(f"replaced text in: {filename}")


# change working directory of script to the given directory
def change_to_dir(directory):
    os.chdir(directory)
    pass


def add_thread_event_to_list(_list, _filename, _old, _new, withOutput=False):
    thread = threading.Thread(
        target=replace_all_in_file, args=(_filename, _old, _new, withOutput)
    )

    _list.append(thread)


def create_dir_if_not_existing(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
