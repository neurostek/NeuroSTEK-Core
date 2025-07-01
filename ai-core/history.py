history = {}

def add_to_history(username, role, message):
    if username not in history:
        history[username] = []
    history[username].append({"role": role, "message": message})

def get_last_messages(username, limit=10):
    if username not in history:
        return []
    return history[username][-limit:]
