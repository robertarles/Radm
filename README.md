# radm (ra dotfile manager)

## Features

radm is a minimal, UNIX-based, cross-platform, hierarchical dotfiles manager (re)written in python.

Core principles are:

- **Minimal dependencies:** Only Python and [GNU Stow](https://www.gnu.org/software/stow/).
- **Cross-platform:** With built-in platform detection, you can install your
  dotfiles on Linux and MacOS.
- **Hierarchical directory structure:** The `base` directory.
  Then the dotfiles in either the `linux` or `macos` folder will be installed
  too. (A tertiary hierarchy for Linux distros is planned for a future release.)
- **Colorful CLI interface**.
- **Self-contained:** The entire system is in a single folder, making it easy to
  clone and install. The `radm` executable is right next to your dotfiles.
- **Non-destructive:** Your existing dotfiles will not be touched unless you
  explicitly beg radm to do so.
- **Creates symlinks only:** radm just creates the symlinks. It's up to you to
  handle version control for your dotfiles. The .gitignore file ignores your dot
  files in the macos, linux, and base directories. BACK THEM UP. (e.g I sync my radm
  directory, and recommend Syncthing)

## Installation

### Prerequisites

- Install [GNU Stow](https://www.gnu.org/software/stow/)
  - MacOS: `brew install stow`
  - Linux: `sudo apt-get install stow`
  - Arch (btw): `sudo pacman -S stow`

### Install radm

- Clone radm: `git clone https://github.com/robertarles/radm`
- Go into your new dotfiles directory: `cd radm`
- Run `./radm`
  - Or, if you want to fully commit to radm, add it to your path with `make
install` and then run `radm`.
- Follow the instructions.

## File Structure

```
- radm
  - base/    (cross-platform dotfiles)
  - linux/   (linux-only dotfiles)
  - macos/   (macOS-only dotfiles)
  - radm (executable)
  - Makefile
```

## Technical Details

radm is a folder structure and a shell script on top of [GNU Stow](https://www.gnu.org/software/stow/) (a symlink manager). It works like this:

1. Put your dotfiles into the `base`, `linux`, and `macos` folders as needed.
2. Run `./radm install`, which will detect your platform and create
   symlinks in your home directory pointing to the dotfiles. This is done with
   GNU Stow, which also creates folders as needed.
3. If your dotfiles change in any way, run `./radm install` again to sync
   the changes to your home folder.

## The `radm` command

```bash
Usage: radm [-h/--help] [install|restore-backup|eject]

       -h/--help: Show this help message

       install:        Install or sync the dotfiles as symlinks in your home folder.
       restore-backup: Restore the backup of your dotfiles created by install.
       eject:          Replace the symlinks in your home folder with hard copies.
```

## Best practices

When using radm, its dotfile folders are the source of truth. Your home directory contains only symlinks.

This implies the following:

#### If you want to edit a dotfile...

Do it as usual: `vim ~/.config/some-dotfile`. It will follow the symlink and edit the source file.

#### If you want to add, delete, or move dotfiles...

You will need to do it in the source folder, and then run `radm install` to sync the changes. The symlinks for the added, moved and deleted files will be updated.

#### If you want dotfiles in your home folder that are not managed by radm...

You can do it. radm won't touch them. If you want, you can add them to radm later.

## FAQ

#### 1. Should I store my dotfiles in an online repo?

Yas. That way, it's easy to install your dotfiles in any new system with internet access.

We recommend a private repo. If you want to use a public repo, set up a
`.gitignore` file to avoid exposing your secrets.

#### 2. What if there is a conflict between dotfiles in `base` and `linux`?

The dotfiles in `linux` will override the dotfiles in `base` with the same name.

#### 3. What if there is a conflict between radm's dotfiles and my home folder?

The first time you run `radm install`, it will ask you to back up your current dotfiles that conflict with those to be installed. If you accept, a `backup` folder will be created in the `yas-bdsm` folder, which can be restored to your home directory at any time by running `yas-bdsm restore-backup`.

#### 4. Is Windows supported?

Nope. Hopefully I'll never need to.

#### 5. Should I put most of my dotfiles in `base`?

Yes. Overriding files by platform should be kept to a minimum, to ease maintainability.

Indeed, we suggest that Bash scripts within dotfiles perform platform detection by themselves at runtime and use conditional statements.

Dotfiles are lightweight, other than the ugly clutter and possible human confusion finding them, there's no harm in installing unused dotfiles.

#### 6. How does the eject system work?

Its sort of an uninstaller. It will turn all your symlinked dotfiles in your home folder into full-fledged files. Then you are on your own.

#### 9. Can I change the folder name?

Yes. TODO: But how? Just yes? Just change it and it still works?
