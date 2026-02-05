from typing import Callable, Dict, Optional, Any

class TaskRouter:
    """
    TaskRouter is responsible for mapping events to tasks.

    - It does NOT execute tasks.
    - It does NOT make decisions.
    - It only translates events into task submissions.
    """

    def __init__(self, event_dispatcher, task_manager, logger):
        self._dispatcher = event_dispatcher
        self._task_manager = task_manager
        self._logger = logger
        self._routes: Dict[str, Callable[[Any], Optional[dict]]] = {}

    def add_route(self, event_type: str, handler: Callable[[Any], Optional[dict]]):
        self._routes[event_type] = handler
        self._logger.info("ROUTER", f"Route registered: {event_type}")

    def start(self):
        self._dispatcher.subscribe(self)
        self._logger.info("ROUTER", "TaskRouter started")

    def on_event(self, event):
        event_type = getattr(event, "type", None)
        if not event_type:
            return

        handler = self._routes.get(event_type)
        if not handler:
            return

        self._logger.info("ROUTER", f"Event received: {event_type}")

        data = handler(event)
        if data is None:
            return

        task_name = data.get("task_name")
        task_payload = data.get("payload", {})

        if not task_name:
            self._logger.warning("ROUTER", f"Route for {event_type} returned no task_name")
            return

        self._logger.info("ROUTER", f"Submitting task: {task_name}")
        self._task_manager.submit(task_name, task_payload)