# RBLX Targeter

RBLX Targeter is a tool designed to identify whether a user is a Red Cell Spectre target in the Roblox roleplaying game, **The Grand Crossing**. It leverages the [Users](https://users.roblox.com/docs/index.html) and [Groups](https://groups.roblox.com/docs/index.html) web APIs to perform its checks.

# Table of Contents

- [Contributors](#contributors)
- [Using the Tool](#using-the-tool)
- [Updating the Tool](#updating-the-tool)

## Contributors

<div style="display: inline-block; text-align: center;">
  <a href="https://www.roblox.com/users/291119265/profile">
    <img src="media/images/Gr8P0tat0.png" alt="Gr8P0tat0 Profile Icon">
  </a>
  <br>
  <strong>Gr8P0tat0</strong>
</div>

## Using the Tool

### Installation Guide

First, make sure you have Python installed on your system. I made this in version `3.12.3`, but Python is backwards compataible, so any version later than that will work. 

You can download [the latest version of Python on their website](https://www.python.org/downloads/).

> [!NOTE]
> Make sure you check off the PATH option, as shown in the image below.

![Python PATH Option Enabled](media/images/PythonPATH.png)

You will nalso eed to install the Python `requests` package to use RBLX Targeter. This can be done by executing command `pip install requests` in the terminal (Command Prompt, PowerShell, MacOS Terminal, etc).

### Providing a Cookie

You can optionally provide a cookie to bypass Roblox's strict API limits. You can provide a `.ROBLOSECURITY` cookie during the program's runtime.

To find cookies for most Chrome/Chromium browsers, `F12/Ctrl + Shift + I > Application > Cookies > ...roblox.com...`.

> [!NOTE]
> You will need to get a new cookie each time you log out (i.e.: when the cookie expires). This includes `_|WARNING:-DO-NOT-SHARE...`

## Updating the Tool

I don’t plan to maintain this indefinitely, but you can easily keep it current by updating the users, groups, and role containers whenever the Spectre target board changes.

**In the meantime, it would help all of us if you pinged me in the [Spectres Discord](https://discord.gg/zkXy3HbTKZ) server whenever you see the target board change!**

---

Yo dudes, Spectres is pretty chill. Maybe you could like, [join it or something](https://discord.gg/zkXy3HbTKZ).

[![Red Cell Spectre Icon](media/images/red-cell-spectre.png)](https://www.roblox.com/groups/4236314/Red-Cell-Spectres)
