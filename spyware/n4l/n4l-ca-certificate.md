---
layout: default
title: N4L CA Certificate
parent: N4L
nav_order: 1
has_children: true
has_toc: false
---

# N4L CA Certificate

Network for Learning employs a CA certificate to undertake its illegal activities. 

## How it works

When you connect to a network with the N4L software, your uplink requests are unmodified, but you connect to a proxy sever instead of the ISP's gateway. This proxy server forwards it on to the website you requested, and then when the website returns its content, it decrypts it, similar to that of a web browser. N4L's software then signs iSee N4L's section on "What to do" t with all 4 of the certificates, and sends it to the user. To decrypt it, one must have the CA certificate. For networks using Palo Alto, a different certificate is required.

## Misinformation

N4L's CA certificate is sometimes branded as a "security certificate", particularly staff of schools educated by IT admins to believe that it's only to "authenticate" on the networks. The CA certificate is in fact used to perform an **illegal** man-in-the-middle (MITM) attack on network traffic, allowing network staff to view all your data, even passwords and sensitive information such as bank details.

## Known variants

There are 4 known certificates used by N4L when using Fortinet, with only one confirmed variant publicly available. When using Palo Alto, only one certificate is known.

**Update 25/02/2026:** All certificates when using Fortinet are now known.

| **Variant (Fortinet)** | **Description** | **File** |
|:-------------------|:------------|:-----|
| Root CA | Publicly-available variant of CA certificate for **Fortinet**, used to spy on students | [N4L-SSL-Certificate.crt](https://cert.n4l.co.nz/download/N4L-SSL-Certificate.crt) |
| N4L Intermediate Certificate | *Research still needed* | - |
| N4L xxx xxxx | Unknown purpose, issued by Spark. Each school rebrands this certificate, no definite original | [N4L_552_1818.crt](https://drive.google.com/file/d/1aJDFUDm4Bs4qK9jpy3DwYh-jCXysXNse/view?usp=drive_link) (One variant) |
| Fortiguard SDNS Blocked Page | Used to hijack Secure DNS at network level | - |

---

| **Variant (Palo Alto)** | **Description** | **File** |
|:-------------------|:------------|:-----|
| Root CA | Publicly-available variant of CA certificate for **Palo Alto**, used to spy on students | [N4L-PA-SSL-Certificate.crt](https://cert.n4l.co.nz/download/N4L-PA-TLS-Certificate.crt) |

## Known Root CA variants

Schools are able to modify the details of the Root CA certificate to create a "new certificate", with known variants listed in the table below. These certificates are identical in functionality to the original Root CA.

| **Root CA Variant** | **Description** | **File** |
|:-------------------|:------------|:-----|
| James Hargest College Root CA | Duplicate of Root CA for Fortinet | [JHC-Security-Certificate.crt](https://www.jameshargest.school.nz/crt/JHC-Security-Certificate.crt) |