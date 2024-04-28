import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class PersonChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ESUO Chat Application ")
        self.root.geometry("900x700")  # Width x Height

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.columns = ("Name", "Status")
        self.list_view = ttk.Treeview(self.frame, columns=self.columns, show="headings")
        self.list_view.heading("Name", text="Name")
        self.list_view.heading("Status", text="Status")
        self.list_view.grid(row=0, column=0, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.list_view.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.list_view.configure(yscrollcommand=self.scrollbar.set)

        self.chat_button = tk.Button(self.frame, text="Go to Chat Page", command=self.show_chat_page)
        self.chat_button.grid(row=2, column=0, pady=5)

        self.buttons = {}
        self.populate_list()

    def populate_list(self):
        # Clear the list
        self.list_view.delete(*self.list_view.get_children())

        # Add persons to the list
        persons = ["Emir", "Uygar", "Ömer", "Selim", "Ahmet", "Ayşe", "Sevgi", "Kemal", "Dürdane", "Ziya", "Şefik", "Yılmaz"]
        for person in persons:
            self.list_view.insert("", "end", values=(person, "Available"))

            # Create or update chat buttons next to each person
            if person not in self.buttons:
                button_text = tk.StringVar(value=f"Chat {person}")
                button = tk.Button(self.frame, textvariable=button_text)
                button["command"] = lambda p=person: self.chat_person(p)
                button.grid(sticky="e")
                self.buttons[person] = button, button_text
            else:
                button, button_text = self.buttons[person]
                button_text.set(f"Chat {person}")

    def chat_person(self, person):
        messagebox.showinfo("Chat", f"Chat request has been sent to {person}...")

    def show_chat_page(self):
        # Hide the main page frame
        self.frame.pack_forget()

        # Create the chat page frame
        self.chat_frame = tk.Frame(self.root)
        self.chat_frame.pack(padx=10, pady=10)

        # Add widgets for the chat page
        chat_label = tk.Label(self.chat_frame, text="Chat Page")
        chat_label.pack()

        self.mesaj_alani = tk.Frame(self.chat_frame)
        self.mesaj_alani.pack()

        self.mesajım = tk.StringVar()
        self.mesajım.set("Mesajınızı giriniz ...")

        self.scrollbar = tk.Scrollbar(self.mesaj_alani)
        self.mesaj_listesi = tk.Listbox(self.mesaj_alani, height=20 , width=70 ,yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.mesaj_listesi.pack(side=tk.LEFT, fill=tk.BOTH)
        self.mesaj_alani.pack()

        self.giriş_alanı = tk.Entry(self.chat_frame, textvariable=self.mesajım)
        self.giriş_alanı.bind("<Return>", self.gonder)
        self.giriş_alanı.pack()

        self.gönder_buton = tk.Button(self.chat_frame, text="Gönder", command=self.gonder)
        self.gönder_buton.pack()

        # Add a button to go back to the main page
        back_button = tk.Button(self.chat_frame, text="Go Back", command=self.show_main_page)
        back_button.pack(pady=5)

    def show_main_page(self):
        # Hide the chat page frame
        self.chat_frame.pack_forget()

        # Show the main page frame
        self.frame.pack()

    def gonder(self, event=None):
        # Get the message from the entry field
        message = self.mesajım.get()

        # Add the message to the listbox
        self.mesaj_listesi.insert(tk.END, message)

        # Clear the entry field
        self.mesajım.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = PersonChatApp(root)
    root.mainloop()
