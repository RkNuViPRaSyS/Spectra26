import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER


class SpectraSightApp(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER))
        hello_label = toga.Label("SpectraSight Loaded", style=Pack(padding=20))
        main_box.add(hello_label)

        self.main_window = toga.MainWindow(title=self.name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return SpectraSightApp()
