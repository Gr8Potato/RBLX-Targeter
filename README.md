# RBLX-Targeter

This is a program I made that uses the [Users](https://users.roblox.com/docs/index.html) and [Groups](https://groups.roblox.com/docs/index.html) web APIs to determine whether a user is a Red Cell Spectre target in the Roblox roleplaying game, The Grand Crossing.

I don't plan on updating this forever, but you can simply update the users, groups, and role containers whenever the Spectre target board changes.

Sadly, I haven't found a solution to the strict rate limiting roblox provides. The simplest solution is to use a rotating proxy service (or multiple proxies to spoof your IP). You can try to find alternative endpoints that don't have such a strict limit, but I wasn't able to find an endpoint that handles user searching. If you can tolerate only being able to search users every >30 seconds, this tool works as intended.

Feel free to contribute to this if you want to improve it!

![Red Cell Spectre Icon](red-cell-spectre.png)
