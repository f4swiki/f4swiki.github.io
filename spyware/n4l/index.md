---
layout: default
title: N4L
parent: Spyware
nav_order: 1
has_children: true
has_toc: false
---

# N4L

|:-----------------|:-----------------------|
| **Founded**      | 2012                   |
| **Purpose**      | Invade student privacy |
| **Supported by** | Spark NZ, 2degrees     |

Network for Learning, known as N4L, is a piece of software used by schools to limit students' access to educational and non-educational material (such as games), similar to that of North Korea's intranet ([Kwangmyong](https://en.wikipedia.org/wiki/Kwangmyong_%28network%29)). The software is known for being intrusive and blocking educational material, even with the CA certificate installed.

## Provider changeover

N4L is changing their backend spyware from [Fortinet](https://f4swiki.github.io/spyware/fortinet.html) to Palo Alto by the end of March 2026. When this change happens, connections on N4L will become less like [Kwangmyong](https://en.wikipedia.org/wiki/Kwangmyong_%28network%29) alone and more like the [Great Firewall of China](https://en.wikipedia.org/wiki/Great_Firewall) and [Kwangmyong](https://en.wikipedia.org/wiki/Kwangmyong_%28network%29) combined. Less importantly, they are changing their broadband provider from Spark to 2degrees, which was needed to be fair.

## Legality

In no way is N4L legal, even though it is a government-owned enterprise. N4L allows IT admins to view all network traffic, which is against [section 250 of the Crimes Act 1961](https://www.legislation.govt.nz/act/public/1961/0043/170.0/DLM330425.html).

It is also noted that N4L's personal data collection and spying (passwords, other identifying information) is not known to the user, a breach of [section 22 of the Privacy Act 2020](https://www.legislation.govt.nz/act/public/2020/0031/latest/LMS23342.html).

## VPN blocking

N4L is known to block OpenVPN and WireGuard (UDP) and all non meek-azure Tor bridges. Recently, N4L has been blocking consistent connections to ProtonVPN's Stealth protocol. Sadly, due to brainless actions by N4L, Chromebooks are unable to connect to Tor via the Android version,

## What to do

Use a VPN (or Tor!) where available. Remove that spyware known as a "security certificate', which allows them to perform illegal activities. See [here](../../bypassing/bypass-n4l.html) for more details on methods.

## References

[1] [https://www.reseller.co.nz/article/3548418/palo-alto-and-2degrees-displace-spark-as-n4l-network-suppliers.html](https://www.reseller.co.nz/article/3548418/palo-alto-and-2degrees-displace-spark-as-n4l-network-suppliers.html)
