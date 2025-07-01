from toga import App, MainWindow, Label

def build(app):
    main_window = MainWindow(title=app.formal_name)
    main_window.content = Label("SpectraSight is ready.")
    main_window.show()
    return main_window

def main():
    return App("SpectraSight", "com.spectrasight", startup=build)