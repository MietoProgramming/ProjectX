from tkinter import *
import time

def console():
    global console_screen
    console_screen = Tk()
    console_screen.geometry("200x250")
    console_screen.title("Command Window")
    # main_screen.iconbitmap() - path to file.ico

    global command
    command = StringVar()


    Label(console_screen, text="Command").pack()
    username_login_entry = Entry(console_screen, textvariable=command)
    username_login_entry.pack()
    Label(console_screen, text="").pack()

    Button(console_screen, text="Run", width=10, height=1, command=run_file).pack()

    console_screen.mainloop()

def run_file():
    imports = "from load import *"
    def_function = "def command_fun():\n\tglobal my_character\n\tglobal buttons\n\tglobal texts"
    commandr = command.get()
    final_code = "texts = game_interface_text()"
    write_code = f"""{imports}\n{def_function}\n\t{commandr}\n\t{final_code}"""
    file = open("command_file.py","w")
    file.write(write_code)
    file.close()
    console_screen.destroy()
    console_screen.quit()
    time.sleep(1)
    import command_file
    command_file.command_fun()

