python
CopyEdit
class Dispatcher:
 
 def __init__(self):
 self.listeners = []
 
 def register(self, listener):
 self.listeners.append(listener)
 
 def dispatch(self, event_type, payload):
 for l in self.listeners:
 if event_type == "click":
 l.on_click(payload)
 elif event_type == "close":
 l.on_close(payload)
 elif event_type == "error":
 l.on_error(payload)