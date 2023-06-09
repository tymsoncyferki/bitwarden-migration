import tkinter as tk

root = tk.Tk()
root.title('Password manager')

root_width = 300
root_height = 200

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - root_width / 2)
center_y = int(screen_height/2 - root_height / 2)

# set the position of the root to the center of the screen
root.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')

message = tk.Label(root, text='Export to Bitwarden')
message.pack()

root.mainloop()
