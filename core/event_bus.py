class EventBus:
    def __init__(self, logger):
        self.logger = logger
        self._subscribers = []

    def register(self, module):
        self._subscribers.append(module)

    def emit(self, event):
        self.logger.info(
            "EVENT_BUS",
            f"Dispatching event: {event.type} from {event.source}"
        )

        for module in self._subscribers:
            try:
                module.on_event(event)
            except Exception as e:
                self.logger.error(
                    "EVENT_BUS",
                    f"{module.__class__.__name__} failed on {event.type}: {e}"
                )