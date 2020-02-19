from unittest import TestCase
from uw_panopto.remote_recorder import remote_recorder_search
from uw_panopto.util import fdao_panopto_override


@fdao_panopto_override
class TestRemoteRecorders(TestCase):

    def test_remote_recorder_search(self):
        recorders = remote_recorder_search('foobar')

        self.assertTrue(len(recorders) == 3)
