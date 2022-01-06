import os
import threading
import shutil


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


def get_all_in_path(path="."):
    entries = list()
    scan = os.scandir(path)
    for entry in scan:
        if entry.is_dir():
            entries.append(entry.path)
            for inner_entry in get_all_in_path(entry.path):
                entries.append(inner_entry)
                pass
            pass
        if entry.is_file():
            entries.append(entry.path)

    return entries


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


# removes dir recursively, throws no error on non-existences of given path
def remove_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)


# moves target to the newly given location
def move(target, to, overwrite=False):

    if os.path.exists(to) and not overwrite:
        raise FileExistsError(f"{to} already exists, but wasn't allowed to overwrite it")

    elif overwrite:
        remove_dir(to)

    create_dir_if_not_existing(to)

    shutil.move(target, to)


def copy_dir(target, to, overwrite=False):
    if os.path.exists(path=to) and not overwrite:
        raise FileExistsError(f"{to} already exists, but wasn't allowed to overwrite it")

    elif overwrite:
        remove_dir(path=to)

    create_dir_if_not_existing(directory=to)

    shutil.copytree(src=target, dst=to)


def create_dir_if_not_existing(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_all_dir_in_path(path):
    if not os.path.exists(path):
        raise IOError(f"{path} doesn't exist")

    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

    return dirs


def directory_contains_file(path: str, searched_file: str):
    if os.path.isfile(path):
        return path.split("/")[-1] == searched_file

    for file in os.listdir(path):
        if file == searched_file:
            return True
    else:
        return False

