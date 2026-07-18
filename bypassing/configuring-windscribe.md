---
layout: default
title: Configuring Windscribe
parent: Bypassing
nav_order: 2
has_children: true
has_toc: false
---

# Configuring Windscribe

Stock Windscribe isn't enough to push through N4L's totalitarian monitoring systems, meaning you'll have to configure it properly to circumnavigate the restrictions.

## Steps

1. Download Windscribe

2. Log into Windscribe

    1. **Windscribe v2.21.3 and later:** It is possible to log in on a network powered by N4L using the 19th endpoint.

    2. **Windscribe v2.21.1 and earlier:** It will be IMPOSSIBLE to log into Windscribe on an N4L-ridden network. Please log in on cellular or a non-N4L network.

3. Go to the hamburger menu and then the "Connections" tab (3rd option down)

4. Scroll until you find "Connection mode". Change this to "Manual"

5. Change protocol to the following depending on the version of Windscribe you are running:

    1. **ALL mobile versions:** "TCP" and port to "80"

    2. **Windscribe v2.22.4 and later:** "UDP" and port to "80" or "WireGuard" and port to "443"

    3. **Windscribe v2.21.3 to v2.21.7:** "WireGuard" and port to "80"

    4. **Windscribe v2.20.4 and earlier:** "TCP" and port to "80"

6. Exit by pressing escape. Now connect.

### Anti-censorship settings are different between Windscribe versions, make sure you follow the correct one.

**Windscribe v2.22.10 and later:**

1. No longer required.

**Windscribe v2.22.4 to v2.22.9:**

1. While these versions are far better at bypassing N4L censorship, they are a bit trickier to configure. If you **are not** using UDP, follow the steps below.

    1. Click on the option "Anti-censorship Settings" at the top of the "Connections" tab.

    2. Click the option "Protocol Tweaks" - turn this on.

    3. Set the "Amnezia Config" to option D - "With Junk Russia Alt".

**Windscribe v2.21.7 and earlier:**

1. Older versions of Windscribe did not have as many options for bypassing censorship, although they work as well.

    1. Scroll down to find "Circumvent Censorship" - turn this on.

    2. **Windscribe v2.20.7 and later:** Set the configuration to option D - "With Junk Alternat4e".