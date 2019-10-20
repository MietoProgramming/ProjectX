from tkinter import *
username_to_load,profession_to_load = "",""
saved = False

def login_menu():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("200x250")
    main_screen.title("Login")
    # main_screen.iconbitmap() - path to file.ico

    global username
    global profession
    global variable
    global variable1

    username = StringVar()
    professions_arr = [
        "Warrior",
        # "Mage",
        # "Archer"
    ]

    Label(main_screen, text="Username(Max 16 marks)").pack()
    username_login_entry = Entry(main_screen, textvariable=username)
    username_login_entry.pack()
    Label(main_screen, text="").pack()

    Label(main_screen, text="").pack()

    Label(main_screen, text="Profession").pack()
    variable = StringVar(main_screen)
    variable.set(professions_arr[0])  # default value
    w = OptionMenu(main_screen, variable, *professions_arr)
    w.pack()

    Label(main_screen, text="").pack()

    Button(main_screen, text="Login", width=10, height=1, command=save_variables).pack()

    main_screen.mainloop()

    return saved

def save_variables():
    global profession_to_load
    global username_to_load
    profession_to_load = variable.get()
    username_to_load = username.get()
    if username_to_load != "" and len(username_to_load) < 16:
        global saved
        saved = True
        main_screen.destroy()
        main_screen.quit()
    else:
        username_exception()


def username_exception():
    global user_not_found_screen
    user_not_found_screen = Toplevel(main_screen)
    user_not_found_screen.title("Warning")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="Username is wrong.").pack()
    Button(user_not_found_screen, text="OK", command=delete_username_exception_screen).pack()

def delete_username_exception_screen():
    user_not_found_screen.destroy()

def move_to_my_character(character_class):
    my_character = character_class(username_to_load,profession_to_load)
    return my_character