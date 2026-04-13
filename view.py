import flet as ft

class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2024 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self):
        self._titolo = ft.Text("Indovina il numero",
                               color="blue", size=24)
        self._txtNmax = ft.TextField(label = "Numero Max",
                                     value = self._controller.getNmax(),
                                     disabled = True
                                     )
        self._txtTmax = ft.TextField(label = "Num tentativi max",
                                     value = self._controller.getTmax(),
                                     disabled = True
                                     )
        self._txtT = ft.TextField(label = "Tentativi rimanenti",
                                  disabled = True )
        self._page.update()

    def setController(self,controller):
        self._controller = controller

    def update(self):
        self._page.update()