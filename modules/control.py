import pyautogui
import os


def shutdown_pc(when, restart):
    if restart==False:
        os.system(f"shutdown /s /t {when}")
    else:
        os.system(f"shutdown /r /t {when}")

def write_text(text):
    pyautogui.typewrite(text)
    pyautogui.press('enter')
    return text

#doesnt work
def click_coord(x,y, right=False):
    if not right:
        pyautogui.click(x,y)
    else:
        pyautogui.rightClick(x,y)

def run_system_command(command, return_message=None):
    os.system(command)
    return return_message

def create_file(path, content):
    path.replace('\\\\', '\\')
    os.system(f"""echo {content} > {path} """)
    return f"""echo {content} > {path} """