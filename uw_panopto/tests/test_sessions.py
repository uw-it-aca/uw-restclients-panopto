from unittest import TestCase
from uw_panopto.sessions import get_session, session_search
from uw_panopto.util import fdao_panopto_override


@fdao_panopto_override
class TestSessions(TestCase):

    def test_get_scheduled_recordings(self):
        session = get_session('00000000-0100-0100-0100-010000000000')

        self.assertTrue(session.id == "00000000-0100-0100-0100-010000000000")

    def test_session_search(self):
        sessions = session_search('foobar')

        self.assertTrue(len(sessions) == 1)
