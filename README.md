# RBLX-Targeter

RBLX Targeter is a tool designed to identify whether a user is a Red Cell Spectre target in the Roblox roleplaying game, **The Grand Crossing**. It leverages the [Users](https://users.roblox.com/docs/index.html) and [Groups](https://groups.roblox.com/docs/index.html) web APIs to perform its checks.


## Updating the Tool

I don’t plan to maintain this indefinitely, but you can easily keep it current by updating the users, groups, and role containers whenever the Spectre target board changes.

## Rate Limiting

Roblox imposes strict rate limits on their APIs. Currently there's a delay between how many searches you can make in a given time (60 seconds). Here are some potential workarounds:

- **Rotating Proxies**: Host the program through a roating proxy service to spoof your IP. This will cost you if you're not using multiple free proxies.
- **Targeter+**: Another version made for increased performance and signifciantly alleviates the built in rate limiting.

    In order to bypass the rate limit via Targeter+, you must provide a `.ROBLOSECURITY` cookie during the program's runtime. To find cookies for most Chrome/Chromium browsers, `F12/Ctrl + Shift + I > Application > Cookies > ...roblox.com...`.

    [!NOTE]
    You will need to get a new cookie each time you log out (i.e.: when the cookie expires).

    [!WARNING]  
    **DO NOT SHARE THIS COOKIE WITH OTHERS** (it literally tells you not to in the cookie).

## Contributors

<div style="display: inline-block; text-align: center;">
  <a href="https://www.roblox.com/users/291119265/profile">
    <img src="media/images/Gr8P0tat0.png" alt="Gr8P0tat0 Profile Icon">
  </a>
  <br>
  <strong>Gr8P0tat0</strong>
</div>

---

Yo dudes, Spectres is pretty chill. Maybe you could like, [join it or something](https://www.roblox.com/groups/4236314/Red-Cell-Spectres).

[![Red Cell Spectre Icon](media/images/red-cell-spectre.png)](https://www.roblox.com/groups/4236314/Red-Cell-Spectres)