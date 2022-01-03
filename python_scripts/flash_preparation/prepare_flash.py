# noinspection PyUnresolvedReferences
import threading

from python_scripts.flash_preparation.rework_scripts import rework_build_link, rework_original_path_links, \
    rework_cmake_link, rework_zephyr_base_link, rework_zephyr_toolchain_link

from python_scripts.env_reader import env_reader

env_file_path = ".env"

local_zephyr_base_installation = "~/zephyrproject/zephyr"
local_project = "."
path_to_build = f"{local_project}/build"
toolchain_installation = f"~/zephyr-sdk-0.13.2"
cmake_install = None

event_list = list()


# function to read in values from .env file
def read_in_from_env(path):
    global local_zephyr_base_installation, local_project, path_to_build, toolchain_installation, cmake_install
    read = env_reader.read_from_env(path)
    try:
        local_zephyr_base_installation = read["zephyr"]
    except KeyError:
        print(f"no zephyr installation path given in {path}, default of {local_zephyr_base_installation} will be used")

    try:
        cmake_install = read["cmake"]
    except KeyError:
        print(f"no cmake installation given in {path}, script will try to find own cmake installation")

    try:
        local_project = read["project"]
    except KeyError:
        print("ERROR: project path wasn't given, but is necessary (project=/absolute/path/to/project)")
        exit(1)

    try:
        path_to_build = read["build"]
    except KeyError:
        print(f"no project build path given in {path}, default of {path_to_build} will be used")

    try:
        toolchain_installation = read["toolchain"]
    except KeyError:
        print(f"no toolchain installation path given in {path},  default of {toolchain_installation} will be used")


def run_threads_in_list():
    for event in event_list:
        event.run()


def run():
    # reading in from env
    read_in_from_env(env_file_path)

    # preparing link changes
    rework_build_link.add_needed_events_to_list(event_list, path_to_build)
    rework_cmake_link.add_needed_events_to_list(event_list, path_to_build, cmake_install)
    rework_original_path_links.add_needed_events_to_list(event_list, path_to_build, local_project)
    rework_zephyr_toolchain_link.add_needed_events_to_list(event_list, path_to_build, toolchain_installation)
    rework_zephyr_base_link.add_needed_events_to_list(event_list, path_to_build, local_zephyr_base_installation)

    # run link changes
    run_threads_in_list()


if __name__ == '__main__':
    run()
