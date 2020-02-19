from unittest import TestCase
from uw_panopto.sessions import get_session
from uw_panopto.util import fdao_panopto_override


@fdao_panopto_override
class TestSessions(TestCase):

    def test_get_scheduled_recordings(self):
        session = get_session('00000000-0100-0100-0100-010000000000')

        self.assertTrue(session.id == "00000000-0100-0100-0100-010000000000")
