import unittest

from project_loader import project_loader


class ProjectLoaderTest(unittest.TestCase):
    def test_build_exclude(self):
        test_path = "/this/is/a/path/with/build"
        removed_path = project_loader.exclude_build_dir(test_path)
        expected_path = "/this/is/a/path/with"
        self.assertEqual(expected_path, removed_path)
        assert expected_path, removed_path


if __name__ == '__main__':
    unittest.main()
