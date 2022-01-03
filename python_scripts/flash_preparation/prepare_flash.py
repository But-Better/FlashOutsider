# noinspection PyUnresolvedReferences
import threading

from python_scripts.flash_preparation.rework_scripts import rework_build_link, rework_original_path_links, \
    rework_cmake_link, rework_zephyr_base_link, rework_zephyr_toolchain_link

from python_scripts.env_reader import env_reader

env_file_path = ".env"

default_zephyr_base_installation = "~/zephyrproject/zephyr"
default_toolchain_installation = f"~/zephyr-sdk-0.13.2"
default_cmake_install = None

event_list = list()


# function to read in values from .env file
def read_in_from_env(path):
    read = env_reader.read_from_env(path)
    try:
        zephyr_base_installation = read["zephyr"]
    except KeyError:
        print(f"no zephyr installation path given in {path}, default of {default_zephyr_base_installation} will be used")
        zephyr_base_installation = default_zephyr_base_installation

    try:
        cmake_install = read["cmake"]
    except KeyError:
        print(f"no cmake installation given in {path}, script will try to find own cmake installation")
        cmake_install = default_cmake_install

    try:
        toolchain_installation = read["toolchain"]
    except KeyError:
        print(f"no toolchain installation path given in {path},  default of {default_toolchain_installation} will be used")
        toolchain_installation = default_toolchain_installation

    return zephyr_base_installation, cmake_install, toolchain_installation


def run_threads_in_list():
    for event in event_list:
        event.run()


def run(path_to_build, project_path, cmake_install, zephyr_base_path, toolchain_installation):
    # reading in from env
    read_in_from_env(env_file_path)

    # preparing link changes
    rework_build_link.add_needed_events_to_list(event_list, path_to_build)
    rework_cmake_link.add_needed_events_to_list(event_list, path_to_build, cmake_install)
    rework_original_path_links.add_needed_events_to_list(event_list, path_to_build, project_path)
    rework_zephyr_toolchain_link.add_needed_events_to_list(event_list, path_to_build, toolchain_installation)
    rework_zephyr_base_link.add_needed_events_to_list(event_list, path_to_build, zephyr_base_path)

    # run link changes
    run_threads_in_list()


