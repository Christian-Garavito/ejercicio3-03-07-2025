class Event:
    def __init__(self, payload):
        self.payload = payload

    def handle(self, listener):
        pass


class ClickEvent(Event):
    """dar click a un evento """
    def handle(self, listener):
        if hasattr(listener, "on_click"):
            listener.on_click(self.payload)


class CloseEvent(Event):
    """cerrar el evento"""
    def handle(self, listener):
        if hasattr(listener, "on_close"):
            listener.on_close(self.payload)

class ErrorEvent(Event):
    """Error a el evento"""
    def handle(self, listener):
        if hasattr(listener, "error"):
            listener.on_close(self.payload)


class Dispatcher:
    def __init__(self):
        self.listeners = []

    def register(self, listener):
        self.listeners.append(listener)

    def dispatch(self, event):
        for listener in self.listeners:
            event.handle(listener)


class MyListener:
    def on_click(self, payload):
        print("Click recibido:", payload)

    def on_close(self, payload):
        print("Close recibido:", payload)


# Código de prueba
dispatcher = Dispatcher()
listener = MyListener()
dispatcher.register(listener)

dispatcher.dispatch(ClickEvent("botón azul"))
dispatcher.dispatch(CloseEvent("ventana principal"))
