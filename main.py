import backend
from frontend import CatalogGUI
import login_frontend
import customtkinter as ctk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Catalog GUI")
        self.show_login()


    def show_login(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        login_frontend.create_login_screen(self.root, self.show_catalog)

    def show_catalog(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        CatalogGUI(self.root, backend)

def main():
    root = ctk.CTk()
    root.geometry('600x400')
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
