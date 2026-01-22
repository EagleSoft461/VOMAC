class EventDispatcher:
    """
    Blind event dispatcher.

    Responsible only for delivering events
    to subscribed modules.
    """

    def __init__(self, logger):
        self.logger = logger
        self.subscribers = []

    def subscribe(self, module):
        if hasattr(module, "on_event"):
            self.subscribers.append(module)
            self.logger.info(
                "EVENT_DISPATCHER",
                f"Module subscribed: {module.__class__.__name__}"
            )
    
    def emit(self, event):
        self.logger.info(
            "EVENT_DISPATCHER",
            f"Dispatching event: {event.type}"
        )

        for module in self.subscribers:
            try:
                module.on_event(event)
            except Exception as e:
                self.logger.error(
                    "EVENT_DISPATCHER",
                    f"Module failed on event {event.type}: {e}"
                )