from core.decision.decision_context import DecisionContext
class TaskRouter:
    """
    v0.5.0 TaskRouter

    - listens to events
    - builds DecisionContext
    - asks DecisionEngine for a DecisionResult
    - submits tasks via TaskManager
    """

    def __init__(self, event_dispatcher, task_manager, decision_engine, logger):
        self._dispatcher = event_dispatcher
        self._task_manager = task_manager
        self._decision_engine = decision_engine
        self._logger = logger

    def start(self):
        self._dispatcher.subscribe(self)
        self._logger.info("ROUTER", "TaskRouter started (v0.5.0)")

    def on_event(self, event):
        event_type = getattr(event, "type", None)
        payload = getattr(event, "payload", None) or {}

        if not event_type:
            return

        self._logger.info("ROUTER", f"Event received: {event_type}")

        ctx = DecisionContext(
            event_type=event_type,
            event_payload=payload,
            memory_snapshot=None,
            context_snapshot=None
        )

        result = self._decision_engine.decide(ctx)

        if not result.task_name:
            self._logger.info("ROUTER", f"No task selected for event: {event_type}")
            return

        self._logger.info(
            "ROUTER",
            f"Decision selected task: {result.task_name} (rule={result.matched_rule})"
        )

        self._task_manager.submit(result.task_name, result.payload)