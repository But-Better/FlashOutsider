from time import sleep, time

import pysftp

from env_reader import env_reader
from flash.flash_project import flash
from flash_preparation import prepare_flash
from project_loader import project_loader

current_env = dict()

default_env_path = ".env"


def get_env(key, re_read=True, env_file=default_env_path):
    global current_env
    if re_read:
        current_env = env_reader.read_from_env(env_file)

    if current_env.keys().__contains__(key):
        return current_env[key]
    else:
        return None


if __name__ == '__main__':
    path_to_project = project_loader.load(projects_directory=get_env("original_projects_path"),
                                          to=get_env("project_holder"))
    # path_to_project = "/home/note/zephyrproject/zephyr/fade_led"

    (zephyr_base_installation, cmake_install, toolchain_installation) = prepare_flash.read_in_from_env(default_env_path)
    prepare_flash.run(path_to_project, cmake_install, zephyr_base_installation, toolchain_installation)

    flash(path_to_project)
