import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from aggregate import Data


class App:
    file_types = ['Bitwarden', 'Chrome']
    type = None
    data = None

    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title('Password manager')

        # Set geometry
        root_width = 600
        root_height = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width / 2 - root_width / 2)
        center_y = int(screen_height / 2 - root_height / 2)
        self.root.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')

        title = ctk.CTkLabel(self.root, text='Clean your export')
        title.pack(padx=10, pady=10)

        # Set file type
        first_label = ctk.CTkLabel(self.root, text='1. Select the format of the import file')
        first_label.pack(padx=10, pady=10)
        self.file_type = tk.StringVar(self.root)
        self.file_type.set('Select')
        self.file_selector = ctk.CTkOptionMenu(self.root, variable=self.file_type, values=self.file_types,
                                               command=self.get_type)
        self.file_selector.pack(padx=10, pady=10)

        # Upload file
        second_label = ctk.CTkLabel(self.root, text='2. Select the import file')
        second_label.pack(padx=10, pady=10)
        self.file_button = ctk.CTkButton(self.root, text='Choose File', state='disabled', fg_color='transparent',
                                         border_width=2, command=self.handle_file)
        self.file_button.pack(padx=10, pady=10)
        self.file_label = ctk.CTkLabel(self.root, text='No file chosen')
        self.file_label.pack(padx=10, pady=10)

        # Export file
        self.export_button = ctk.CTkButton(self.root, text='Process File', state='disabled', command=self.process_file)
        self.export_button.pack(padx=10, pady=10)

        # Save file
        self.save_button = ctk.CTkButton(self.root, text='Save', state='disabled', fg_color='transparent',
                                         border_width=2, command=self.save_file)
        self.save_button.pack(padx=10, pady=10)

        self.root.mainloop()

    def get_type(self, file_type):
        self.file_button.configure(state='normal')
        self.type = file_type

    def handle_file(self=None):
        filename = filedialog.askopenfilename()
        if filename:
            self.data = Data(filename, self.type)
            try:
                self.data.verify()
                self.file_label.configure(text=filename, text_color='white')
                self.export_button.configure(state='normal')
            except AssertionError:
                self.file_label.configure(text='File does not match selected file type!', text_color='red')
                self.export_button.configure(state='disabled')
            print('Selected:', filename)
        else:
            self.file_label.configure(text='No file chosen', text_color='white')
            self.export_button.configure(state='disabled')

    def process_file(self=None):
        self.data.aggregate()
        self.save_button.configure(state='normal')
        print('Aggregated')
        # todo: display how many rows where concatenated + progressbar

    def save_file(self=None):
        filename = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('csv', '*.csv')],
                                                initialfile='bitwarden_export')
        print('Exporting:', filename)
        if filename:
            self.data.output_df.to_csv(filename, index=False)


def main():
    App()


if __name__ == "__main__":
    main()
