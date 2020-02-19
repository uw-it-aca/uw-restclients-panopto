from restclients_core import models
import json


class RecordingFolder(models.Model):
    id = models.CharField(max_length=32)
    name = models.CharField(max_length=256)

    def __init__(self, *args, **kwargs):
        data = kwargs.get("data")
        if data is None:
            return super(RecordingFolder, self).__init__(*args, **kwargs)

        self.id = data.get("Id")
        self.name = data.get("Name")

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def __str__(self):
        return json.dumps(self.to_json())


class RemoteRecorder(models.Model):
    RECORDING_STATE_STOPPED = "Stopped"
    RECORDING_STATE_PREVIEWING = "Previewing"
    RECORDING_STATE_PAUSED = "Paused"
    RECORDING_STATE_FAULTED = "Faulted"
    RECORDING_STATE_Disconnected = "Disconnected"
    RECORDING_STATE_RECORDERRUNNING = "RecorderRunning"

    RECORDING_STATE_CHOICES = (
        (RECORDING_STATE_STOPPED, "Stopped"),
        (RECORDING_STATE_PREVIEWING, "Previewing"),
        (RECORDING_STATE_PAUSED, "Paused"),
        (RECORDING_STATE_FAULTED, "Faulted"),
        (RECORDING_STATE_Disconnected, "Disconnected"),
        (RECORDING_STATE_RECORDERRUNNING, "RecorderRunning"),
    )

    id = models.CharField(max_length=32)
    name = models.CharField(max_length=256)
    state = models.CharField(max_length=16, choices=RECORDING_STATE_CHOICES)
    default_recording_folder = models.ForeignKey(RecordingFolder,
                                                 on_delete=models.PROTECT)

    def __init__(self, *args, **kwargs):
        data = kwargs.get("data")
        if data is None:
            return super(RemoteRecorder, self).__init__(*args, **kwargs)

        self.id = data.get("Id")
        self.name = data.get("Name")
        self.state = dict(self.RECORDING_STATE_CHOICES)[data.get("State")]
        self.default_recording_folder = RecordingFolder(
            data=data.get("DefaultRecordingFolder"))

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'state': dict(self.RECORDING_STATE_CHOICES)[self.state],
            'default_recording_folder': self.default_recording_folder.to_json()
        }

    def __str__(self):
        return json.dumps(self.to_json())
