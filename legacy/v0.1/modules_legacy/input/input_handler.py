class InputHandler:
  def process(self, raw_input: dict) -> dict:
    return {
      "source": raw_input.get("source"),
      "type": raw_input.get("type"),
      "payload": raw_input.get("payload", {})
    }
