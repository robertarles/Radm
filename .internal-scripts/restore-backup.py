#!/usr/bin/env python3

import os
import sys
import shutil

def restore_backup(backup_dir, home_dir):
  # Confirm restoration
  print("Restoring backup of dotfiles")
  print(f"This will overwrite any conflicting files in {home_dir} with their backed up versions in {backup_dir}.")
  print("Any non-conflicting files will remain unchanged.")  
  print("Do you want to continue? [y/N]")
  
  if input().lower() != "y":
    print("Aborting")
    sys.exit(1)

  # Restore backup
  for file in os.listdir(backup_dir):
    source = os.path.join(backup_dir, file)
    destination = os.path.join(home_dir, file)
    if os.path.exists(destination):
      os.remove(destination)
    shutil.move(source, destination)
  
  print("Backup restored successfully")

if __name__ == "__main__":
  script_dir = os.path.dirname(os.path.realpath(__file__))
  repo_dir = os.path.dirname(script_dir)
  backup_dir = os.path.join(repo_dir, "backup")
  home_dir = os.path.expanduser("~")

  restore_backup(backup_dir, home_dir)