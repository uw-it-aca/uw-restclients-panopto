from unittest import TestCase
from uw_panopto.remote_recorder import get_remote_recorders
from uw_panopto.util import fdao_panopto_override


@fdao_panopto_override
class TestRemoteRecorders(TestCase):

    def test_remote_recorders(self):
        recorders = get_remote_recorders('foobar')

        self.assertTrue(len(recorders) == 2)
