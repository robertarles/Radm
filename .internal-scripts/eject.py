#!/usr/bin/env python3

import os
import sys
import platform

def get_platform():
  if platform.system().lower() == "darwin":
    return "macos"
  elif platform.system().lower() == "linux":  
    return "linux"
  else:
    print("Unsupported platform")
    sys.exit(1)

platform = get_platform()

script_dir = os.path.dirname(os.path.realpath(__file__)) 
repo_dir = os.path.dirname(script_dir)
stow_dir = repo_dir

# Check if there are any dotfiles for the platform
stow_packages = ["base", platform]
all_empty = True
for package in stow_packages:
  if os.listdir(f"{stow_dir}/{package}"):
    all_empty = False
    break

if all_empty:
  print(f"No dotfiles found for {platform} platform.")
  print("Please add dotfiles to:")
  for package in stow_packages:
    print(f"- {stow_dir}/{package}")
  sys.exit(1)

# Confirm ejection  
print("Ejecting dotfiles")
print(f"This will create hard copies in your home folder of every file in the dotfile folders for {platform}.") 
print("Your dotfiles will no longer be symlinks. You'll have to manage them manually.")
print("This will not restore your backup. You can run radm restore-backup later.")
print("Do you want to continue? [y/N]")

if input().lower() != "y":
  print("Aborting")
  sys.exit(1)

# Eject dotfiles
os.chdir(stow_dir)
for package in stow_packages:
  for file in [f for f in os.listdir(f"{stow_dir}/{package}") if not f.endswith(".gitkeep")]:
    os.makedirs(os.path.dirname(f"{os.path.expanduser('~')}/{file}"), exist_ok=True)
    os.system(f"cp -f -v --remove-destination {stow_dir}/{package}/{file} {os.path.expanduser('~')}/{file}")

print("Finished ejecting dotfiles")