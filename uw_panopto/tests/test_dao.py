from unittest import TestCase
from uw_panopto.dao import Panopto_DAO


class DaoTest(TestCase):

    def test_dao(self):
        dao = Panopto_DAO()
        self.assertEqual(dao.service_name(), "panopto")
        self.assertTrue(len(dao.service_mock_paths()) > 0)
        self.assertTrue(dao.is_using_file_dao())
