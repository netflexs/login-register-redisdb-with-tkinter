
import tkinter
import redis

# Create window
window = tkinter.Tk()
window.title("Login Register System")
window.geometry('400x300')

# Connect Redis
r = redis.Redis(
  host='mwtawu ajah',
  port=13475,
  password='mwtawu ajah')

# Login Function
def login():
    username = user_name.get()
    password = user_password.get()
    if r.exists(username):
        if r.get(username).decode('utf-8') == password:
            # show success
            success = tkinter.Tk()
            success.title("Success")
            success_label = tkinter.Label(success, text="Login Success").pack()
            success_button = tkinter.Button(success, text="Ok", command=success.destroy).pack()
        else:
            # show wrong password
            wrong_password = tkinter.Tk()
            wrong_password.title("Failed")
            fail_label = tkinter.Label(wrong_password, text="Wrong Password").pack()
            fail_button = tkinter.Button(wrong_password, text="Ok", command=wrong_password.destroy).pack()
    else:
        # show wrong username
        wrong_username = tkinter.Tk()
        wrong_username.title("Failed")
        fail_label = tkinter.Label(wrong_username, text="Wrong Username").pack()
        fail_button = tkinter.Button(wrong_username, text="Ok", command=wrong_username.destroy).pack()

# Register Function
def register():
    username = user_name.get()
    password = user_password.get()
    if r.exists(username):
        # show username exist
        exist = tkinter.Tk()
        exist.title("Failed")
        exist_label = tkinter.Label(exist, text="Username Exist").pack()
        exist_button = tkinter.Button(exist, text="Ok", command=exist.destroy).pack()
    else:
        # save username and password
        r.set(username, password)
        # show success
        success = tkinter.Tk()
        success.title("Success")
        success_label = tkinter.Label(success, text="Register Success").pack()
        success_button = tkinter.Button(success, text="Ok", command=success.destroy).pack()

# Username
user_name = tkinter.StringVar()
name_label = tkinter.Label(window, text="Username").place(x=50, y=50)
name_entry = tkinter.Entry(window, textvariable=user_name).place(x=120, y=50)

# Password
user_password = tkinter.StringVar()
password_label = tkinter.Label(window, text="Password").place(x=50, y=100)
password_entry = tkinter.Entry(window, textvariable=user_password).place(x=120, y=100)

# Login Button
login_button = tkinter.Button(window, text="Login", command=login).place(x=120, y=150)

# Register Button
register_button = tkinter.Button(window, text="Register", command=register).place(x=180, y=150)

# Start
window.mainloop()
