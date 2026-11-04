#!/usr/bin/env python3

import os
import shlex
import time
from datetime import datetime
from pathlib import Path

HOME = Path.home()
cwd = HOME

EXIT_STAGES = (
    (25, "Closing session..."),
    (50, "Defragging hard-disk..."),
    (100, "Publishing API keys to GitHub..."),
)
EXIT_ERROR = "ERROR: Do not try to bend the spoon."
EXIT_MESSAGE = "Exiting to vanilla Linux... you hope."


def dos_path(path):
    relative = str(path).replace("/", "\\")
    return "C:" + relative.upper()


def error():
    print("Bad command or file name")


def directory():
    print()
    print(" Volume in drive C has no label.")
    print(f" Directory of {dos_path(cwd)}")
    print()

    for item in sorted(cwd.iterdir()):
        try:
            stat = item.stat()
            date = datetime.fromtimestamp(stat.st_mtime)
            timestamp = date.strftime("%m-%d-%y  %H:%M")

            if item.is_dir():
                print(f"{item.name.upper():12} <DIR>       {timestamp}")
            else:
                print(f"{item.name.upper():12} {stat.st_size:10} {timestamp}")
        except OSError:
            continue

    print()


def theatrical_exit():
    width = 30
    previous = 0

    print()
    for target, message in EXIT_STAGES:
        for progress in range(previous + 1, target + 1):
            filled = width * progress // 100
            bar = "#" * filled + "-" * (width - filled)
            print(f"\r[{bar}] {progress:3d}%  {message}", end="", flush=True)
            time.sleep(0.015)
        print()
        previous = target

    print(EXIT_ERROR)
    print()
    print(EXIT_MESSAGE, flush=True)
    time.sleep(0.8)


def main():
    global cwd

    os.system("clear")

    print("Microsoft(R) MS-DOS(R) Version 6.22")
    print("(C)Copyright Microsoft Corp 1981-1994.")
    print()

    while True:
        try:
            command = input(f"{dos_path(cwd)}>").strip()

            if not command:
                continue

            parts = shlex.split(command)
            cmd = parts[0].lower()
            args = parts[1:]

            if cmd == "exit":
                theatrical_exit()
                break

            if cmd == "dir":
                directory()

            elif cmd == "cls":
                os.system("clear")

            elif cmd == "ver":
                print("MS-DOS Version 6.22")

            elif cmd == "cd":
                if not args:
                    print(dos_path(cwd))
                    continue

                target = (cwd / args[0].replace("\\", "/")).resolve()

                if target.is_dir():
                    cwd = target
                else:
                    print("Invalid directory")

            elif cmd == "type":
                if not args:
                    print("Required parameter missing")
                    continue

                target = cwd / args[0]

                try:
                    print(target.read_text())
                except (OSError, UnicodeError):
                    print("File not found")

            elif cmd == "help":
                print(
                    """
Supported commands:

DIR       Displays files and directories
CD        Changes directory
CLS       Clears the screen
TYPE      Displays a text file
VER       Displays DOS version
HELP      Displays this help
EXIT      Returns to Linux
"""
                )

            elif cmd in (
                "ls",
                "pwd",
                "cat",
                "sudo",
                "grep",
                "find",
                "bash",
                "zsh",
                "fish",
                "clear",
            ):
                error()

            else:
                error()

        except (KeyboardInterrupt, EOFError):
            print()
            break
        except ValueError:
            error()


if __name__ == "__main__":
    main()
