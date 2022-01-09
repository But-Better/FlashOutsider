import os
import subprocess
import threading
import shutil

from distutils import dir_util

# list up all files existing in a path
#
# (this scan also lists up files in subdirectories,
# but not the directories itself)
from distutils.errors import DistutilsFileError

from env_reader import env_reader


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

    if os.path.isdir(target):
        try:
            dir_util.copy_tree(target, to)
        except DistutilsFileError:
            use_env_copy(target, to)

        dir_util.remove_tree(target)
    else:
        shutil.move(target, to)


def target_exists(target):
    return os.path.exists(target)


def use_env_copy(target, to):
    external_copy = get_env("external_recursive_copy_tool")
    change_to_dir(exclude_last_in_path(external_copy))
    return exec_command(["./copy", f"{target}/*", to])
    pass


def copy_dir(target, to, overwrite=False):
    if os.path.exists(path=to) and not overwrite:
        raise FileExistsError(f"{to} already exists, but wasn't allowed to overwrite it")

    elif overwrite:
        remove_dir(path=to)

    try:
        dir_util.copy_tree(src=target, dst=to)
    except DistutilsFileError:
        use_env_copy(target, to)


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


def create_empty_file_if_non_existing(file_path):
    if os.path.exists(file_path):
        return
    else:
        # create a file
        with open(file_path, 'w') as fp:
            fp.close()


def exec_command(command):
    res = subprocess.check_output(command)  # system command
    return res.decode("utf-8")


def get_env(key, env_file=".env"):
    current_env = env_reader.read_from_env(env_file)

    if current_env.keys().__contains__(key):
        return current_env[key]
    else:
        return None


def exclude_last_in_path(project):
    project_split = project.split("/")
    project_split.pop()
    return ''.join(str(f"{e}/") for e in project_split)[:-1]