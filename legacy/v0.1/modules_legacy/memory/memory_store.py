class MemoryStore:
    def __init__(self):
        self.state = {}

    def set(self, key: str, vaule):
        self.state[key] = vaule

    def get(self, key: str):
        return self.state.get(key)
    
    def snapshot(self) -> dict:
        return self.state.copy()