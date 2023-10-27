#!/usr/bin/env python3

import os
import platform
import shutil


def install_dotfiles(dotfiles_dir, home_dir):
    # Detect platform
    platform_name = platform.system().lower()

    # Install base dotfiles
    # delete any .DS_Store files that may have been added by macOS
    os.system(f"find {dotfiles_dir} -name '*.DS_Store' -type f -delete")
    os.system(f"stow -d {dotfiles_dir}/ -t {home_dir} -v base")

    # Install platform-specific dotfiles
    if platform_name == "linux":
        os.system(f"stow -d {dotfiles_dir}/ -t {home_dir} -v linux")
    elif platform_name == "darwin":
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
    script_dir = os.path.dirname(os.path.realpath(__file__))
    dotfiles_dir = os.path.dirname(script_dir)
    home_dir = os.path.expanduser("~")

    install_dotfiles(dotfiles_dir, home_dir)
