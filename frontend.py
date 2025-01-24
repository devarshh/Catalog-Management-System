import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk

class CatalogGUI:
    def __init__(self, root, backend):
        self.root = root
        self.backend = backend
        self.catalog = self.backend.read_catalog()

        # Main window setup
        self.root.title("Catalogue Management System")
        self.root.geometry("600x400")
        self.root.configure(bg="#262626")

        title_label = tk.Label(self.root, text="Catalogue Management System", font=("Arial", 20, "bold"), bg="#262626", fg="white")
        title_label.pack(pady=10)

        #Style the Treeview for larger text
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="#262626",
                        foreground="white",
                        fieldbackground="#262626",
                        bordercolor="white",
                        borderwidth=1,
                        font=("Arial", 14), rowheight=30)  # Adjust row height for larger font
        style.configure("Treeview.Heading", font=("Arial", 13, "bold"))  # Adjust column heading font

        # Table
        self.columns = ("ID", "Name", "Description")
        self.tree = ttk.Treeview(self.root, columns=self.columns, show="headings", height=8)
        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=150)
        self.tree.pack(fill="both", expand=True)

        # Populate table
        self.populate_tree()

        # Buttons
        button_frame = tk.Frame(self.root, bg="#262626")
        button_frame.pack(pady=10, fill="x")

        ctk.CTkButton(button_frame, text="Add", corner_radius=20, font=("Arial", 16),
                      fg_color="#FF4B26", text_color="white", command=self.add_entry).pack(side="left", padx=10)
        ctk.CTkButton(button_frame, text="Edit", corner_radius=20, font=("Arial", 16),
                      fg_color="#FF4B26", text_color="white", command=self.edit_entry).pack(side="left", padx=10)
        ctk.CTkButton(button_frame, text="Save", corner_radius=20, font=("Arial", 16),
                      fg_color="#FF4B26", text_color="white", command=self.submit_entry).pack(side="left", padx=10)
        ctk.CTkButton(button_frame, text="Log Out", corner_radius=20, font=("Arial", 16),
                      fg_color="#FF4B26", text_color="white", command=self.logout).pack(side="left", padx=10)

    def populate_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for item in self.catalog:
            self.tree.insert("", tk.END, values=(item["ID"], item["Name"], item["Description"]))

    def add_entry(self):
        def save():
            new_item = {
                "ID": id_entry.get(),
                "Name": name_entry.get(),
                "Description": desc_entry.get()
            }

            #Check if ID already exists
            existing_ids = {item["ID"] for item in self.catalog}
            if new_item["ID"] in existing_ids:
                messagebox.showerror("Error", f"An entry with ID '{new_item['ID']}' already exists!")
                return

            # Validate fields
            if not new_item["ID"] or not new_item["Name"] or not new_item["Description"]:
                messagebox.showerror("Error", "All fields are required.")
                return

            if self.backend.add_item(self.catalog, new_item):
                self.populate_tree()
                add_window.destroy()
            else:
                messagebox.showerror("Error", "All fields are required.")

        add_window = tk.Toplevel(self.root)
        add_window.title("Add Item")
        add_window.geometry("400x300")
        add_window.configure(bg="#262626")
        tk.Label(add_window, text="ID", font=("Arial", 14), bg="#262626", fg="white").pack(pady=5)
        id_entry = tk.Entry(add_window, font=("Arial", 14), bg="#1E1E1E", fg="white", insertbackground="white")
        id_entry.pack(pady=5)
        tk.Label(add_window, text="Name", font=("Arial", 14), bg="#262626", fg="white").pack(pady=5)
        name_entry = tk.Entry(add_window, font=("Arial", 14), bg="#1E1E1E", fg="white", insertbackground="white")
        name_entry.pack(pady=5)
        tk.Label(add_window, text="Description", font=("Arial", 14), bg="#262626", fg="white").pack(pady=5)
        desc_entry = tk.Entry(add_window, font=("Arial", 14), bg="#1E1E1E", fg="white", insertbackground="white")
        desc_entry.pack(pady=5)
        tk.Button(add_window, text="Save", command=save, font=("Arial", 14), bg="#FF4B26", fg="white").pack(pady=10)


    def edit_entry(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "No item selected.")
            return
        item = self.tree.item(selected)["values"]
        item_id = item[0]

        def save():
            new_name = name_entry.get().strip()
            new_description = desc_entry.get().strip()

            # Validate fields
            if not new_name or not new_description:
                messagebox.showerror("Error", "All fields are required.")
                return

            updates = {"Name": name_entry.get(), "Description": desc_entry.get()}
            if self.backend.edit_item(self.catalog, item_id, updates):
                self.populate_tree()
                edit_window.destroy()
            else:
                messagebox.showerror("Error", "Failed to update item.")

        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Item")
        edit_window.geometry("400x300")
        edit_window.configure(bg="#262626")  # Set background color
        tk.Label(edit_window, text="Name", font=("Arial", 14), bg="#262626", fg="white").pack(pady=5)
        name_entry = tk.Entry(edit_window, font=("Arial", 14), bg="#1E1E1E", fg="white", insertbackground="white")
        name_entry.insert(0, item[1])  # Pre-fill with current value
        name_entry.pack(pady=5)
        tk.Label(edit_window, text="Description", font=("Arial", 14), bg="#262626", fg="white").pack(pady=5)
        desc_entry = tk.Entry(edit_window, font=("Arial", 14), bg="#1E1E1E", fg="white", insertbackground="white")
        desc_entry.insert(0, item[2])  # Pre-fill with current value
        desc_entry.pack(pady=5)
        tk.Button(edit_window, text="Save", command=save, font=("Arial", 14), bg="#FF4B26", fg="white").pack(pady=10)

    def submit_entry(self):
        self.backend.save_catalog(self.catalog)
        messagebox.showinfo("Success", "Changes saved successfully.")


    def logout(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        from login_frontend import create_login_screen
        create_login_screen(self.root, lambda: CatalogGUI(self.root, self.backend))

