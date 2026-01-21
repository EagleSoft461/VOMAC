class OutputFormatter:
    def format(self, decision: dict) -> dict:
        return {
            "decision": decision.get("decision"),
            "reason": decision.get("reason"),
            "confidence": decision.get("confidence")
        }