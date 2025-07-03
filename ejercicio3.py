class Event:
    """Creacion del evento"""
    def __init__(self, payload):
        self.payload = payload

    def handle(self, listener):
        """manejador """
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
        if hasattr(listener, "on_error"):
            listener.on_close(self.payload)

class LoadEvent(Event):
    """Error a el evento"""
    def handle(self, listener):
        if hasattr(listener, "on_load"):
            listener.on_close(self.payload)

class KeyupEvent(Event):
    """Error a el evento"""
    def handle(self, listener):
        if hasattr(listener, "on_keyUp"):
            listener.on_close(self.payload)

class KeyDownEvent(Event):
    """Error a el evento"""
    def handle(self, listener):
        if hasattr(listener, "on_KeyDown"):
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

    def on_error(self, payload):
        print("Error recibido:", payload)

    def on_load(self, payload):
        print("Load recibido:", payload)

    def on_key_up(self, payload):
        print("KeyUp recibido:", payload)

    def on_key_down(self, payload):
        print("KeyDown recibido:", payload)



dispatcher = Dispatcher()
listener = MyListener()
dispatcher.register(listener)

dispatcher.dispatch(ClickEvent("botón azul"))
dispatcher.dispatch(CloseEvent("ventana principal"))
dispatcher.dispatch(ErrorEvent("archivo no encontrado"))
dispatcher.dispatch(LoadEvent("cargando perfil"))
dispatcher.dispatch(KeyupEvent("tecla A"))
dispatcher.dispatch(KeyDownEvent("tecla B"))
