from unittest import TestCase
from uw_panopto.folders import (
    get_folder, folder_search, get_folder_children, get_folder_sessions)
from uw_panopto.util import fdao_panopto_override


@fdao_panopto_override
class TestFolders(TestCase):

    def test_get_folder(self):
        session = get_folder('00000000-0101-0101-0101-010000000010')

        self.assertTrue(session.id == "00000000-0101-0101-0101-010000000010")

    def test_folder_search(self):
        folders = folder_search('foobar')

        self.assertTrue(len(folders) == 2)

    def test_get_folder_children(self):
        folders = get_folder_children('00000000-0101-0101-0101-010000000040')

        self.assertTrue(len(folders) == 2)

    def test_get_folder_sessions(self):
        folders = get_folder_sessions('00000000-0101-0101-0101-010000000040')

        self.assertTrue(len(folders) == 1)
