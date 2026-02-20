from core.decision.decision_context import DecisionContext


class TaskRouter:
    """
    v0.5.1 TaskRouter

    - listens to events
    - collects Memory + Context snapshots
    - builds DecisionContext
    - asks DecisionEngine for a DecisionResult
    - submits tasks via TaskManager
    """

    def __init__(
        self,
        event_dispatcher,
        task_manager,
        decision_engine,
        logger,
        snapshot_providers=None
    ):
        self._dispatcher = event_dispatcher
        self._task_manager = task_manager
        self._decision_engine = decision_engine
        self._logger = logger

        self._snapshot_providers = snapshot_providers or {}

    def start(self):
        self._dispatcher.subscribe(self)
        self._logger.info("ROUTER", "TaskRouter started (v0.5.1)")

    def on_event(self, event):
        event_type = getattr(event, "type", None)
        payload = getattr(event, "payload", None) or {}

        if not event_type:
            return

        self._logger.info("ROUTER", f"Event received: {event_type}")

        memory_snapshot = None
        context_snapshot = None

        if "memory" in self._snapshot_providers:
            try:
                memory_snapshot = self._snapshot_providers["memory"].get_snapshot()
                if memory_snapshot:
                    self._logger.info("ROUTER", f"Memory snapshot: {memory_snapshot}")
            except Exception as e:
                self._logger.error("ROUTER", f"Failed to get memory snapshot: {e}")

        if "context" in self._snapshot_providers:
            try:
                context_snapshot = self._snapshot_providers["context"].get_snapshot()
                if context_snapshot:
                    self._logger.info("ROUTER", f"Context snapshot: {context_snapshot}")
            except Exception as e:
                self._logger.error("ROUTER", f"Failed to get context snapshot: {e}")
                
        ctx = DecisionContext(
            event_type=event_type,
            event_payload=payload,
            memory_snapshot=memory_snapshot,
            context_snapshot=context_snapshot
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