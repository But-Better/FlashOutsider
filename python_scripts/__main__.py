from flash.flash_project import flash
from flash_preparation import prepare_flash
from project_loader import project_loader
from specific_utils.env_utils import get_env

current_env = dict()

default_env_path = "/home/note/PycharmProjects/westflashs/python_scripts/.env"

if __name__ == '__main__':
    path_to_project = project_loader.load(projects_directory=get_env("original_projects_path"),
                                          to=get_env("project_holder"),
                                          copy=True,
                                          overwrite=True)

    (zephyr_base_installation, cmake_install, toolchain_installation) = prepare_flash.read_in_from_env(default_env_path)

    prepare_flash.run(path_to_project, cmake_install, zephyr_base_installation, toolchain_installation)

    flash(path_to_project)
