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

### Windows

Download the [latest RBLX Targeter EXE](https://github.com/Gr8Potato/RBLX-Targeter/releases). All relevant dependencies and runtimes should be installed upon running the program.
> [!NOTE]
> Windows Defender WILL trigger upon attempting to run the program. This is because the hash isn't signed by Microsoft. Windows Defender should scan the program and function normally.

### Other Operating Systems

You will need to install the Python `requests` package to use RBLX Targeter. Also, make sure you have Python installed on your system (I made this in version `3.12.3`).

### Providing a Cookie

You can optionally provide a cookie to bypass Roblox's strict API limits. You can provide a `.ROBLOSECURITY` cookie during the program's runtime.

To find cookies for most Chrome/Chromium browsers, `F12/Ctrl + Shift + I > Application > Cookies > ...roblox.com...`.

> [!NOTE]
> You will need to get a new cookie each time you log out (i.e.: when the cookie expires).

> [!WARNING]  
> **DO NOT SHARE THIS COOKIE WITH OTHERS** (it tells you not to put it in the cookie).

## Updating the Tool

I don’t plan to maintain this indefinitely, but you can easily keep it current by updating the users, groups, and role containers whenever the Spectre target board changes.

**In the meantime, it would help me if you pinged me in the [Spectres Discord](https://discord.gg/zkXy3HbTKZ) server whenever the target board changes!**

---

Yo dudes, Spectres is pretty chill. Maybe you could like, [join it or something](https://discord.gg/zkXy3HbTKZ).

[![Red Cell Spectre Icon](media/images/red-cell-spectre.png)](https://www.roblox.com/groups/4236314/Red-Cell-Spectres)
