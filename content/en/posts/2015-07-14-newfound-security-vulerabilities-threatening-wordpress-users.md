---
author: bozsikarmand
comments: true
date: 2015-07-14 16:56:03+00:00
layout: post
link: https://blog.bozsikarmand.hu/2015/07/14/newfound-security-vulerabilities-threatening-wordpress-users/
slug: newfound-security-vulerabilities-threatening-wordpress-users
title: Newfound security vulerabilities threatening WordPress users
wordpress_id: 15
categories:
- IT Security
tags:
- Biztonságportál
- plugins
- security
- security hole
- WordPress
---

**Two widely used extension of WordPress contains pretty severe errors. Unfortunately not every security hole can be fixed.**

Researchers at High-Tech Bridge in the previous weeks two WordPress plugins started to monitor closely. They did a thorough security analysis in the case of TheCartPress plugin which is made to support e-commerce and WP Photo Album Plus which is an extension especially for photo management. In both of them they found risky vulnerabilities, despite the latter received the proper fixes.


#### Errors will stay with us in the next version of TheCartPress?


TheCartPress is serving on more than 5000 WordPress-based websites, but the webshops which relies on it would have turned to be vulnerable since in High-Tech Bridge high number of security holes were revealed in connection with the extension. Principally the errors can give intruders the chance for XSS (Cross-site Scripting) attacks. One of the errors can turn out at the end of the order process namely at that time the application does not supervise all of the output parameters, thereupon – for instance by the manipulation of billing and shipping addresses – arbitrary HTML and/or script codes can be run.

Beside the vulnerability described above researchers had to face with other problems. They discovered four XSS-related errors which could be exploited by the use of specially formatted links and arbitrary codes can be run in consequence of that. As long as a person with elevated administrative rights clicks on a link like the one previously described, the risk could get into a higher level. Furthermore another vulnerability threatens the systems which could give the chance for misusing PHP files in the course of directory traversal-type attacks.

According to High-Tech Bridge they think TheCartPress 1.3.9 surely includes the vulnerability, but the previous versions could be concerned too. The biggest issue is that the developers of TheCartPress indicated by the 1st of May they discard any support in connection with the plugin, so it is far from certain these errors will be corrected in any time.


#### The photo manager is already safe


In the apropos of the WP Photo Album Plus extension it is a bad news that researchers also found an XSS-related error - which they qualified as medium on the scale - in it. On the other hand we can serve you the good news too: though 50000 websites are affected by the security hole, the update is available. The newest version of the plugin does not include the vulnerability.

__Source:__ [Biztonság Portál](http://biztonsagportal.hu/ujabb-biztonsagi-hibak-veszelyeztetik-a-wordpresst.html)