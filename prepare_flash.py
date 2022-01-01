# noinspection PyUnresolvedReferences
import threading

from rework_scripts import rework_original_path_links, rework_cmake_link, rework_zephyr_base_link, rework_build_link, \
    rework_zephyr_toolchain_link

local_zephyr_base_installation = "/home/note/zephyrproject/zephyr"
local_project = f"{local_zephyr_base_installation}/samples/basic/fade_led"
pathToBuild = f"{local_project}/build"
toolchain_installation = f"/home/note/zephyr-sdk-0.13.2"

event_list = list()


def run_threads_in_list():
    for event in event_list:
        event.run()


if __name__ == '__main__':
    rework_build_link.add_needed_events_to_list(event_list, pathToBuild)
    rework_cmake_link.add_needed_events_to_list(event_list, pathToBuild)
    rework_original_path_links.add_needed_events_to_list(event_list, pathToBuild, local_project)
    rework_zephyr_toolchain_link.add_needed_events_to_list(event_list, pathToBuild, toolchain_installation)
    rework_zephyr_base_link.add_needed_events_to_list(event_list, pathToBuild, local_zephyr_base_installation)

    run_threads_in_list()
