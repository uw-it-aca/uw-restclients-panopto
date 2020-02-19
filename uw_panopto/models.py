from restclients_core import models
from dateutil.parser import parse
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


class RecorderScheduledEntry(models.Model):
    id = models.CharField(max_length=32)
    name = models.CharField(max_length=256)
    recorder_id = models.CharField(max_length=32)
    suppress_primary_capture = models.BooleanField(default=False)
    suppress_secondary_capture = models.BooleanField(default=False)
    recorder_description = models.CharField(max_length=256)

    def __init__(self, *args, **kwargs):
        data = kwargs.get("data")
        if data is None:
            return super(
                RecorderScheduledEntry, self).__init__(*args, **kwargs)

        self.id = data.get("Id")
        self.name = data.get("Name")
        self.suppress_primary_capture = (
            data.get("SuppressPrimaryCapture", False) == "true")
        self.suppress_secondary_capture = (
            data.get("SuppressSecondaryCapture", False) == "true")
        self.recorder_description = data.get("RecorderDescription")

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'recorder_id': self.recorder_id,
            'suppress_primary_capture': self.suppress_primary_capture,
            'suppress_secondary_capture': self.suppress_secondary_capture,
            'recorder_description': self.recorder_description
        }

    def __str__(self):
        return json.dumps(self.to_json())


class ScheduledRecording(models.Model):
    id = models.CharField(max_length=32)
    name = models.CharField(max_length=256)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)

    def __init__(self, *args, **kwargs):
        data = kwargs.get("data")
        if data is None:
            return super(
                RecorderScheduledEntry, self).__init__(*args, **kwargs)

        self.id = data.get("Id")
        self.name = data.get("Name")
        self.start_time = parse(data.get("StartTime")) if (
            "StartTime" in data) else None
        self.end_time = parse(data.get("EndTime", "")) if (
            "EndTime" in data) else None

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'start_timee': str(self.start_time) if self.start_time else None,
            'start_time': str(self.end_time) if self.end_time else None
        }

    def __str__(self):
        return json.dumps(self.to_json())
