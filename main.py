from core.input.input_handler import InputHandler
from core.memory.memory_store import MemoryStore
from core.reasoning.rule_engine import RuleEngine
from core.output.output_formatter import OutputFormatter
from core.config import load_config
from core.logger import setup_logger
import logging


def run():
    setup_logger()
    logger = logging.getLogger("VOMAC")

    config = load_config()
    threshold = config["threshold"]

    logger.info(f"VOMAC started with threshold={threshold}")

    input_handler = InputHandler()
    memory = MemoryStore()
    engine = RuleEngine(threshold)
    output = OutputFormatter()

    raw_input = {
        "source": "system",
        "type": "event",
        "payload": {
            "value": 72
        }
    }

    processed_input = input_handler.process(raw_input)
    memory.set("last_input", processed_input)

    decision = engine.evaluate(processed_input)
    result = output.format(decision)

    logger.info(f"Decision result: {result}")
    print(result)

if __name__ == "__main__":
    run()