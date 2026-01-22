import time

class Event:
    """
    Infrastructure-level event message.
    Carries data only — no behavior.
    """

    def __init__(self, type, payload=None, source=None):
        self.type = type
        self.payload = payload or {}
        self.source = source
        self.timestamp = time.time()