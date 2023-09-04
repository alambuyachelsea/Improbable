import tkinter as tk


# create app_body window, title, size, background color
app_body = tk.Tk()
app_body.title("Improbable ")
app_body.geometry("400x600")
app_body.maxsize(400, 600)
small_img = tk.PhotoImage(file='Improbable/assets/lock-icon.png')
# large_img = tk.PhotoImage(file='Improbable/assets/lock-icon-large.ico')
app_body.iconphoto(False, small_img)
# TODO find out how to change window taskbar icon
# app_body.iconbitmap("lock-icon-large.ico")

# Create nav bar scene widget
nav_frame = tk.Frame(app_body, width=400, height=70)
nav_frame.config(bg="#5B6565")
nav_frame.grid(row=0, column=0, padx=0, pady=0)


# Create main scene widget
body_frame = tk.Frame(app_body, width=400, height=530)
body_frame.config(bg="#D9D9D9")
body_frame.grid(row=1, column=0, padx=0, pady=0)
app_body.mainloop()
