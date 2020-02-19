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
                ScheduledRecording, self).__init__(*args, **kwargs)

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
            'start_time': str(self.start_time) if self.start_time else None,
            'start_time': str(self.end_time) if self.end_time else None
        }

    def __str__(self):
        return json.dumps(self.to_json())


class Session(models.Model):
    id = models.CharField(max_length=32)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    start_time = models.DateTimeField(null=True)
    folder = models.CharField(max_length=256)

    def __init__(self, *args, **kwargs):
        data = kwargs.get("data")
        if data is None:
            return super(Session, self).__init__(*args, **kwargs)

        self.id = data.get("Id")
        self.name = data.get("Name")
        self.description = data.get("Description")
        self.start_time = parse(data.get("StartTime")) if (
            "StartTime" in data) else None
        self.folder = data.get("Folder")

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'start_time': str(self.start_time) if self.start_time else None,
            'folder': self.folder
        }

    def __str__(self):
        return json.dumps(self.to_json())


class SessionCreator(models.Model):
    id = models.CharField(max_length=32)
    user_name = models.CharField(max_length=128)

    def __init__(self, *args, **kwargs):
        data = kwargs.get("data")
        if data is None:
            return super(SessionCreator, self).__init__(*args, **kwargs)

        self.id = data.get("Id")
        self.user_name = data.get("Username")

    def to_json(self):
        return {
            'id': self.id,
            'user_name': self.name
        }

    def __str__(self):
        return json.dumps(self.to_json())


class SessionUrls(models.Model):
    viewer_url = models.CharField(max_length=256)
    embed_url = models.CharField(max_length=256)
    share_settings_url = models.CharField(max_length=256)
    download_url = models.CharField(max_length=256)
    caption_download_url = models.CharField(max_length=256)
    editor_url = models.CharField(max_length=256)
    thumbnail_url = models.CharField(max_length=256)

    def __init__(self, *args, **kwargs):
        data = kwargs.get("data")
        if data is None:
            return super(SessionUrls, self).__init__(*args, **kwargs)

        self.viewer_url = data.get("ViewerUrl")
        self.embed_url = data.get("EmbedUrl")
        self.share_settings_url = data.get("ShareSettingsUrl")
        self.download_url = data.get("DownloadUrl")
        self.caption_download_url = data.get("CaptionDownloadUrl")
        self.editor_url = data.get("EditorUrl")
        self.thumbnail_url = data.get("ThumbnailUrl")

    def to_json(self):
        return {
            'viewer_url': self.viewer_url,
            'embed_url': self.embed_url,
            'share_settings_url': self.share_settings_url,
            'download_url': self.download_url,
            'caption_download_url': self.caption_download_url,
            'editor_url': self.editor_url,
            'thumbnail_url': self.thumbnail_url
        }

    def __str__(self):
        return json.dumps(self.to_json())


class SessionContext(models.Model):
    text = models.CharField(max_length=128)
    time = models.CharField(max_length=128)
    thumbnail_url = models.CharField(max_length=256)

    def __init__(self, *args, **kwargs):
        data = kwargs.get("data")
        if data is None:
            return super(SessionUrls, self).__init__(*args, **kwargs)

        self.text = data.get("Text")
        self.time = int(data.get("Time"))
        self.thumbnail_url = data.get("ThumbnailUrl")

    def to_json(self):
        return {
            'text': self.text,
            'time': self.time,
            'thumbnail_url': self.thumbnail_url
        }

    def __str__(self):
        return json.dumps(self.to_json())
