#!/usr/bin/env python3
import platform
import psutil
import os
from termcolor import colored, cprint
import sys
import time

def loading_animation(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0001)
    print()

class SystemInfo():
    def __init__(self):
        global ascii_art

        os_info = platform.system()
        os_info = colored(os_info, "green")

        if "Linux" in os_info:
            linux_icon = ("🐧")
        else:
            linux_icon = ("💀")

        kernel = platform.release()
        kernel = colored(kernel, "yellow")
        shell = os.environ.get("SHELL")
        shell = colored(shell, "red")
        terminal = os.environ.get("TERM")
        terminal = colored(terminal, "blue")
        CPU = platform.processor()
        CPU = colored(CPU, "red")

        whoami = os.environ.get('USERNAME') or os.environ.get('USER')
        whoami = colored(whoami, "red")

        memory_info = psutil.virtual_memory()
        memory = memory_info.total

        value = memory / (2 ** 20)
        value_rounded = round(value)
        value_rounded = colored(value_rounded, "yellow")

        self.ascii_art = f"""\
                                                 {whoami}
                                                 --------
        ⢕⢕⢕⢕⢕⠅⢗⢕⠕⣠⠄⣗⢕⢕⠕⢕⢕⢕⠕⢠⣿⠐⢕⢕⢕⠑⢕⢕⠵⢕ OS        {os_info} {linux_icon}
        ⢕⢕⢕⢕⠁⢜⠕⢁⣴⣿⡇⢓⢕⢵⢐⢕⢕⠕⢁⣾⢿⣧⠑⢕⢕⠄⢑⢕⠅⢕ Kernel    {kernel}
        ⢕⢕⠵⢁⠔⢁⣤⣤⣶⣶⣶⡐⣕⢽⠐⢕⠕⣡⣾⣶⣶⣶⣤⡁⢓⢕⠄⢑⢅⢑ Shell     {shell}
        ⠍⣧⠄⣶⣾⣿⣿⣿⣿⣿⣿⣷⣔⢕⢄⢡⣾⣿⣿⣿⣿⣿⣿⣿⣦⡑⢕⢤⠱⢐ Terminal  {terminal}
        ⢠⢕⠅⣾⣿⠋⢿⣿⣿⣿⠉⣿⣿⣷⣦⣶⣽⣿⣿⠈⣿⣿⣿⣿⠏⢹⣷⣷⡅⢐ CPU       {CPU}
        ⣔⢕⢥⢻⣿⡀⠈⠛⠛⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⡀⠈⠛⠛⠁⠄⣼⣿⣿⡇⢔ Memory    {value_rounded} MiB
        ⢕⢕⢽⢸⢟⢟⢖⢖⢤⣶⡟⢻⣿⡿⠻⣿⣿⡟⢀⣿⣦⢤⢤⢔⢞⢿⢿⣿⠁⢕
        ⢕⢕⠅⣐⢕⢕⢕⢕⢕⣿⣿⡄⠛⢀⣦⠈⠛⢀⣼⣿⢗⢕⢕⢕⢕⢕⢕⡏⣘⢕
        ⢕⢕⠅⢓⣕⣕⣕⣕⣵⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣕⢕⢕⢕⢕⡵⢕⣿⣘
        ⢑⢕⠃⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⢕
        """

    def loading(self):
        loading_animation(self.ascii_art)

if __name__ == "__main__":
    system = SystemInfo()
    system.loading()




