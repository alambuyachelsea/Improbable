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


# Generates new password
def new_password_suggestion():
    return (print("new password"))


# Copy password
def copy_password():
    return (print("copy password"))


# Goes back to password generation area
def generation_area():
    return (print("generation area"))


# Goes back to user profile area
def user_profile():
    return (print("user profile area"))


# 10 rows and 5 columns
# Nav bar area
nav_frame = tk.Frame(app_body, width=400, height=70)
nav_frame.config(bg="#5B6565")
nav_frame.grid(row=0, column=0, padx=0, pady=0)
nav_frame.grid_propagate(False)
nav_frame.grid_columnconfigure(0, weight=1)
nav_frame.grid_rowconfigure(0, weight=1)

# Empty grid cell
empty_cell = tk.Label(nav_frame, text='empty', bg='#5B6565')

# Nav bar buttons
generation_area_img = tk.PhotoImage(file='Improbable/assets/lock-icon.png')
generation_area_button = tk.Button(nav_frame,
                                   command=user_profile,
                                   image=generation_area_img)
generation_area_button.config(bg="#5B6565", bd=0)

user_profile_img = tk.PhotoImage(file='Improbable/assets/user-icon.png')
user_profile_button = tk.Button(nav_frame,
                                command=user_profile,
                                image=user_profile_img)
user_profile_button.config(bg="#5B6565", bd=0)

# Row 1 nav bar buttons
empty_cell.grid(column=0, row=0)
generation_area_button.grid(column=1, row=0)
#empty_cell.grid(column=2, row=0)
user_profile_button.grid(column=3, row=0)

# Main scene area
body_frame = tk.Frame(app_body, width=400, height=530)
body_frame.config(bg="#D9D9D9")
body_frame.grid(row=1, column=0, padx=0, pady=0)
body_frame.grid_propagate(False)
body_frame.grid_columnconfigure(0, weight=1)
body_frame.grid_rowconfigure(0, weight=1)

# suggested password
suggested_password = tk.Label(body_frame, text="new password here")
suggested_password.config(bg="pink")
suggested_password.grid(row=0, column=0, padx=0, pady=0)

# Copy password button
copy_img = tk.PhotoImage(file='Improbable/assets/copy-icon.png')
copy_password_button = tk.Button(body_frame,
                                 command=copy_password,
                                 image=copy_img)
copy_password_button.grid(row=0, column=1)
copy_password_button.config(bg="#D9D9D9", bd=0)

# Regenerate password
regenerate_img = tk.PhotoImage(file='Improbable/assets/shuffle-icon.png')
generate_password_button = tk.Button(body_frame,
                                     command=new_password_suggestion,
                                     image=regenerate_img)
generate_password_button.grid(row=1, column=0)
generate_password_button.config(bg="#D9D9D9", bd=0)

app_body.mainloop()
