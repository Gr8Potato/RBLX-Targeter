# RBLX Targeter

RBLX Targeter is a tool designed to identify whether a user is a Red Cell, Chimera, or Spectre target in the Roblox roleplaying game, **The Grand Crossing**. It leverages the [Users](https://users.roblox.com/docs/index.html) and [Groups](https://groups.roblox.com/docs/index.html) web APIs to perform its checks.

# Table of Contents

- [Using the Tool](#using-the-tool)
- [Updating the Tool](#updating-the-tool)
- [Output Sample](#output-sample)

## Using the Tool

### Installation Guide

First, make sure you have Python installed on your system. I made this in version `3.12.3`, but Python is backward compatible, so any version later than that will work. 

You can download [the latest version of Python on their website](https://www.python.org/downloads/).

> [!NOTE]
> Make sure you check off the PATH option, as shown in the image below.

![Python PATH Option Enabled](media/images/PythonPATH.png)

You will also need to install the Python `requests` package to use RBLX Targeter. This can be done by executing the command `pip install requests` in the terminal (Command Prompt, PowerShell, MacOS Terminal, etc).

Once you've done that, find [the latest release](https://github.com/Gr8Potato/RBLX-Targeter/releases) and download the `targeter.py` file.

### Providing a Cookie

You can optionally provide a cookie to bypass Roblox's strict API limits. You can provide a `.ROBLOSECURITY` cookie during the program's runtime.

To find cookies for most Chrome/Chromium browsers, `F12/Ctrl + Shift + I > Application > Cookies > ...roblox.com...`.

> [!NOTE]
> You will need to get a new cookie each time you log out (i.e.: when the cookie expires). This includes `_|WARNING:-DO-NOT-SHARE...`

## Updating the Tool

If you're interested in maintaining the tool, feel free to reach out to me on Discord (`Gr8Potato`). I can also add you as a contributor to the project, and you can make your own edits to the repo (if you mess something up, we can always revert it)!

To give a short summary for the latter, you'll primarily be working with the [`TNI-ranks.txt`](https://github.com/Gr8Potato/RBLX-Targeter/blob/main/media/documents/TNI-ranks.txt) document and, of course, the [`targeter.py`](https://github.com/Gr8Potato/RBLX-Targeter/blob/main/src/targeter.py) file. The text file is just for reference. As high command, officer, etc. targets get added to the target board, you'll need to know the ranks that count as a valid target. That's where that file comes in handy.

From there, you'll want to edit the relavent Python containers to accurately reflect the Chimera, Red Cell, and/or Spectre target boards. If you don't know what a Python container is, [here is a short read from one of my former professor's textbooks](https://www.softcover.io/read/92780ad5/python_book/containers). Now that you know what that is, the containers you'll be editing often are `perm_spectre_targets`, `perm_spectre_targets`, `phantom_spectre_groups`...`weekly_chimera_roles`, `chimera_morphs`, you get the idea. Pattern recognition should kick in, allowing you to fill in the rest.

## Output Sample
The program runs entirely from the terminal. The output may be slightly different as the project carries on. This is taken from RBLX Target v2.0.
```
========================================
Enter .ROBLOSECURITY cookie (or leave blank to skip):
========================================
Enter user: Gr8P0tat0
----------------------------------------
Username: Gr8P0tat0, DisplayName: Gr8Potato, Id: 291119265
----------------------------------------
SPECTRES
XXXXXXXXXX

RED CELL
XXXXXXXXXX

CHIMERA
Nighthawk Commandos, Gr8P0tat0 | MUST BE IN MORPH!
========================================
Cooldown: 0 seconds remaining
========================================
Enter user: Ciphren
----------------------------------------
Username: Ciphren, DisplayName: Ciphren, Id: 68966801
----------------------------------------
SPECTRES
Nighthawk Manticore, Ciphren | Phantom Assigned
Nighthawk Manticore, Auxilior, Ciphren | Permanent Hit
Nighthawk Military Police: Cerberus, | C | Council, Ciphren | Permanent Hit
Nighthawk Imperial Peacekeeper Corps, Ciphren | Permanent Hit

RED CELL
Nighthawk Manticore, Ciphren
Nighthawk Imperial Peacekeeper Corps, Ciphren

CHIMERA
Nighthawk Military Police: Cerberus, Ciphren | MUST BE IN MORPH!
========================================
Enter user: MeowTentatioNN
----------------------------------------
Username: MeowTentatioNN, DisplayName: Furball, Id: 871501766
----------------------------------------
MeowTentatioNN is not a target in any group.
========================================
Enter user: nokia3310achi
----------------------------------------
Username: nokia3310achi, DisplayName: 1AzOrion_02XL, Id: 888267834
----------------------------------------
nokia3310achi is not in The Nighthawk Imperium. Not a target. Are you sure you typed the name in correctly?
========================================
Enter user: thisusersimplydoesnotexist
----------------------------------------
No exact match found for username: thisusersimplydoesnotexist
========================================
```

---

Yo dudes, Spectres is pretty chill. Maybe you could like, [join it or something](https://discord.gg/zkXy3HbTKZ).

[![Red Cell Spectre Icon](media/images/red-cell-spectre.png)](https://www.roblox.com/groups/4236314/Red-Cell-Spectres)
