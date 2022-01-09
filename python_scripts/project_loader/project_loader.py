from specific_utils import env_utils


# exclude the last directory in path (here most likely "build")
def exclude_build_dir(project):
    project_split = project.split("/")
    project_split.pop()
    return ''.join(str(f"{e}/") for e in project_split)[:-1]
    pass


def pick_new_project_to_load(path):
    potential_projects = env_utils.get_all_in_path(path=f"{path}")
    for project in potential_projects:
        project = f"{project}/build"

        if project_contains_needed_files(project):
            project = exclude_build_dir(project=project)
            return project

    return None
    pass


def project_contains_needed_files(project):
    return env_utils.directory_contains_file(path=project, searched_file="CMakeCache.txt") and \
           env_utils.directory_contains_file(path=project, searched_file="build.ninja") and \
           env_utils.directory_contains_file(path=project, searched_file="app")


def load(projects_directory, to, specific=None):
    if not specific:
        specific = pick_new_project_to_load(projects_directory)

    if specific is None:
        print("no projects currently available")
        raise EnvironmentError("no viable projects found")

    return load_in_specific_project(project=specific, project_name=specific.split("/")[-1], to=to)
    pass


def load_in_specific_project(project, project_name, to):
    new_directory = f"{to}/{project_name}"
    try:
        env_utils.move(target=f"{project}", to=new_directory)
    except FileExistsError as e:
        print(e)
        return None
    except IOError:
        raise IOError(f"project doesn't exist at location, can't copy it")

    return new_directory
    pass
