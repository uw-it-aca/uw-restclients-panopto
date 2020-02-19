from unittest import TestCase
from uw_panopto.scheduled_recordings import get_scheduled_recordings
from uw_panopto.util import fdao_panopto_override


@fdao_panopto_override
class TestRemoteRecorders(TestCase):

    def test_get_scheduled_recordings(self):
        recorderings = get_scheduled_recordings(
            '00000000-1000-1000-1000-000000000000')

        self.assertTrue(len(recorderings.recorder_schedule_entries) == 1)
