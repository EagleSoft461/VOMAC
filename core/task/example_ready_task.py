from core.task.task import Task


class ExampleReadyTask(Task):
    NAME = "EXAMPLE_READY_TASK"

    def execute(self):
        self.logger.info("TASK", "[EXAMPLE_READY_TASK] executed successfully")