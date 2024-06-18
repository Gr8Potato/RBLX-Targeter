# RBLX Targeter

RBLX Targeter is a tool designed to identify whether a user is a Red Cell Spectre target in the Roblox roleplaying game, **The Grand Crossing**. It leverages the [Users](https://users.roblox.com/docs/index.html) and [Groups](https://groups.roblox.com/docs/index.html) web APIs to perform its checks.

## Table of Contents

- [Contributors](#contributors)
- [Using the Tool](#using-the-tool)
- [Updating the Tool](#updating-the-tool)
- [Rate Limiting](#rate-limiting)

## Contributors

<div style="display: inline-block; text-align: center;">
  <a href="https://www.roblox.com/users/291119265/profile">
    <img src="media/images/Gr8P0tat0.png" alt="Gr8P0tat0 Profile Icon">
  </a>
  <br>
  <strong>Gr8P0tat0</strong>
</div>

## Using the Tool

There are two ways I've used the tool:

- **Google Colab** - This was the way I originally did it and is far easier to set up. You can create a Google Colab or Jupyter Notebook instance and copy + paste `targeter.py` into a code cell.

- **Running Locally** - This is the way I do it now due to performance improvements and bypassing the harsh rate limiting Roblox has set for external, naked API calls. You can run `targeter+.py` or `targeter.py`, but the latter will impose the aforementioned restrictions.

> [!NOTE]
> You will need to install the Python `requests` package in order to use either program. To install it, execute `pip install --user requests` in either Command Prompt, PowerShell, or Bash terminal. Also, make sure you have Python installed on your system (I made this in version `3.12.3`).


## Updating the Tool

I don’t plan to maintain this indefinitely, but you can easily keep it current by updating the users, groups, and role containers whenever the Spectre target board changes.

## Rate Limiting

Roblox imposes strict rate limits on their APIs. Currently, there's a delay between how many searches you can make in a given time (60 seconds). Here are some potential workarounds:

- **Rotating Proxies**: Host the program through a rotating proxy service to spoof your IP. This will cost you if you're not using multiple free proxies.
- **Targeter+**: Another version made for increased performance and significantly alleviates the built-in rate limiting.

    In order to bypass the rate limit via Targeter+, you must provide a `.ROBLOSECURITY` cookie during the program's runtime. To find cookies for most Chrome/Chromium browsers, `F12/Ctrl + Shift + I > Application > Cookies > ...roblox.com...`.

> [!NOTE]
> You will need to get a new cookie each time you log out (i.e.: when the cookie expires).

> [!WARNING]  
> **DO NOT SHARE THIS COOKIE WITH OTHERS** (it tells you not to put it in the cookie).

---

Yo dudes, Spectres is pretty chill. Maybe you could like, [join it or something](https://www.roblox.com/groups/4236314/Red-Cell-Spectres).

[![Red Cell Spectre Icon](media/images/red-cell-spectre.png)](https://www.roblox.com/groups/4236314/Red-Cell-Spectres)
