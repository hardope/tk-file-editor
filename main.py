import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        self.root.geometry("800x600")

        # Use 'clam' style theme for a modern appearance with rounded corners
        style = ttk.Style()
        style.theme_use('clam')

        # Set custom colors and styles
        style.configure('TFrame', background='#f0f0f0')
        style.configure('TLabel', background='#f0f0f0')
        style.configure('TButton', background='#dcdcdc', relief='flat', borderwidth=0, bordercolor='#f0f0f0', padding=5)
        style.map('TButton', background=[('active', '#c0c0c0')])

        self.create_menu()

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg='#f0f0f0', fg='black', relief='flat')
        self.text_area.pack(side='right', expand=True, fill='both', padx=(0, 5), pady=5)
        self.text_area.bind("<Control-s>", self.save_file_ctrl_s)

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Save", command=self.save_file_menu)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menu_bar)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.file_path = None

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())
            self.file_path = file_path

    def save_file_menu(self):
        if hasattr(self, 'file_path'):
            self.save_file(self.file_path)
        else:
            self.save_file_as()

    def save_file_ctrl_s(self, event):
        if hasattr(self, 'file_path'):
            self.save_file(self.file_path)
        else:
            self.save_file_as()

    def save_file(self, file_path):
        with open(file_path, "w") as file:
            file.write(self.text_area.get(1.0, tk.END))

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            self.save_file(file_path)
            self.file_path = file_path

    def exit_app(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

def main():
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
