#!/usr/bin/env python3

import os
import platform
import shutil
import sys

red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
nocolor = "\033[0m"


def install_dotfiles(dotfiles_dir, home_dir):
    # Detect platform
    platform_name = platform.system().lower()
    if platform_name not in ["linux", "darwin"]:
        print(f"{red}ERROR: Platform {platform_name} is not supported by radm{nocolor}")
        exit(1)
    # Install base dotfiles
    # dont install .DS_Store files, delete strays
    os.system(f"find {dotfiles_dir} -name '*.DS_Store' -type f -delete")
    
    # install base dotfiles first
    print(f"{green}Installing base dotfiles{nocolor}")
    print(f"os.system(f\"stow -d {dotfiles_dir}/ -t {home_dir} -v base\")")
    os.system(f"stow -d {dotfiles_dir}/ -t {home_dir} -v base")

    # Install platform-specific dotfiles
    if platform_name == "linux":
        print(f"{green}Platform is linux, installing linux dotfiles{nocolor}")
        os.system(f"stow -d {dotfiles_dir}/ -t {home_dir} -v linux")
    elif platform_name == "darwin":
        print(f"{green}Platform is macOS, installing macOS dotfiles{nocolor}")
        # delete any .DS_Store files that may have been added by macOS
        os.system(f"find {dotfiles_dir} -name '*.DS_Store' -type f -delete")
        os.system(f"stow -d {dotfiles_dir}/ -t {home_dir} -v macos")

    # Backup existing dotfiles
    backup_dir = f"{dotfiles_dir}/backup"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    for file in os.listdir(home_dir):
        if file in os.listdir(dotfiles_dir):
            shutil.move(os.path.join(home_dir, file), backup_dir)


if __name__ == "__main__":
    # assume the users working directory is the 
    # dotfile source folder ('base' 'linux' and 'macos' folders are in the working directory)
    # script dir is the directory of this script, unless script_dir (first argument) is specified
    script_dir = os.path.dirname(os.path.realpath(__file__))
    if len(sys.argv) > 1:
        script_dir = sys.argv[1]
    
    home_dir = os.path.expanduser("~")

    install_dotfiles(script_dir, home_dir)
