from time import sleep, time

import pysftp

from flash.flash_project import flash
from flash_preparation import prepare_flash

env_file = ".env"


if __name__ == '__main__':
    # path_to_project = get_project_from_remote()
    path_to_project = "/home/note/zephyrproject/zephyr/fade_led"

    (zephyr_base_installation, cmake_install, toolchain_installation) = prepare_flash.read_in_from_env(env_file)
    prepare_flash.run(path_to_project, cmake_install, zephyr_base_installation, toolchain_installation)

    flash(path_to_project)
