import os.path
import shutil
import unittest

from project_loader import project_loader


class ProjectLoaderTest(unittest.TestCase):
    def test_build_exclude(self):
        test_path = "/this/is/a/path/with/build"
        removed_path = project_loader.exclude_build_dir(test_path)
        expected_path = "/this/is/a/path/with"
        self.assertEqual(expected_path, removed_path)
        pass

    def test_pick_new_project_to_load(self):
        test_directory = "test_project_directory"
        selected_project = project_loader.pick_new_project_to_load(test_directory)
        expected_selection = test_directory + "/test_project"
        self.assertEqual(expected_selection, selected_project)
        pass

    def test_project_contains_needed_files(self):
        test_directory = "test_project_directory/test_project/build"
        self.assertTrue(project_loader.project_contains_needed_files(test_directory))
        pass

    def test_load_in_specific_project(self):
        test_directory = "test_project_directory/test_project"
        expected_dir = "test_project_directory/test"

        if os.path.exists(expected_dir) and os.path.isdir(expected_dir):
            shutil.rmtree(expected_dir)

        loaded_in_directory = project_loader.load_in_specific_project(project=test_directory,
                                                                      project_name="test",
                                                                      to="test_project_directory",
                                                                      copy=True,
                                                                      overwrite=True)

        self.assertTrue(os.path.exists(f"{expected_dir}/build"))
        self.assertEqual(expected_dir, loaded_in_directory)


if __name__ == '__main__':
    unittest.main()
