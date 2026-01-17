class RuleEngine:
    def __init__(self, threshold: int):
        self.threshold = threshold

    def evaluate(self, data: dict) -> dict:
        payload = data.get("payload", {})
        vaule = payload.get("vaule", 0)

        if vaule > self.threshold:
            return{
                "decision": "ALERT",
                "reason": "Vaule exceeded threshold({self.threshold})",
                "confidence": 1.0
            }
        
        return{
            "decision": "OK",
            "reason": "Value within normal range",
            "confidence": 1.0
        }