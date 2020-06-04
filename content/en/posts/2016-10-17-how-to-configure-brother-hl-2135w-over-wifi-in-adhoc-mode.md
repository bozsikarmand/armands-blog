---
author: bozsikarmand
comments: true
date: 2016-10-17 19:51:58+00:00
layout: post
link: https://blog.bozsikarmand.hu/2016/10/17/how-to-configure-brother-hl-2135w-over-wifi-in-adhoc-mode/
slug: how-to-configure-brother-hl-2135w-over-wifi-in-adhoc-mode
title: How to configure Brother HL-2135W over wifi in adhoc mode
wordpress_id: 430
categories:
- How-to
tags:
- brother
- hl-2135w
- linux
- ubuntu
- wifi
---

In case you would like to avoid using the pre-built driver package provided by Brother please do the following in order to configure the printer on a secure wifi network:



 	
  1. Find an OS which is capable of creating ad-hoc network ([current version of Ubuntu](http://releases.ubuntu.com/16.04.1/ubuntu-16.04.1-desktop-amd64.iso) will suffice)

 	
  2. Find a compatible USB wifi stick (e.g.: [ASUS USB-N13](https://www.amazon.com/USB-N13-Wireless-N-Adapter-802-11b-Wireless/dp/B002UVNW5W))

 	
  3. Do a factory reset on the printer. (To do this please refer to the user manual)

On my device I had to do the following:
- Had to turn off the printer
- Held GO button while turned on the printer
- Held the GO button until all the LEDs lit up and the Ready LED light turned off
- Released GO, all the LEDs turned off
- Pressed GO ten times. The printer automatically restarted.

 	
  4. To enable WIFI hold down GO button until (~10s) the network configuration page is being printed.

 	
  5. In the Node Type field the word "Active" should be shown.

 	
  6. After that install wine by this command:

    
    `sudo apt install wine`




 	
  7. Then download BRAdmin Light from [here](http://www.softpedia.com/get/Network-Tools/Misc-Networking-Tools/BRAdmin-Light.shtml#download), which helps configuring the printer.

 	
  8. Connect to the SSID called "SETUP" created by the printer:
[![connsetup1](/images/connsetup1.png)](/images/connsetup1.png)[![connsetup2](/images/connsetup2.png)](/images/connsetup2.png)

 	
  9. Start BRAdmin Light. It should find the device.
[![bradmin](/images/bradmin.png)](/images/bradmin.png)

 	
  10. Connect to the printer web interface from the program (Right click / Device Home Page).
[![brwebstart](/images/brwebstart.png)](/images/brwebstart.png)

 	
  11. Under Network configuration (default user: admin, default pass: access) > TCP/IP set the correct Subnet mask and Gateway and set Boot method to DHCP and leave Enable APIPA checked, then press Submit button.
[![netconf](/images/netconf.png)](/images/netconf.png)[![netconf-settings](/images/netconf-settings)](/images/netconf-settings.png)

 	
  12. Press Network configuration > Configure Wireless
[![netconf-prewl](/images/netconf-prewl.png)](/images/netconf-prewl.png)

 	
  13. Set Infrastructure mode, provide your network SSID, Channel, Authentication and encryption method, password (all of these information can be seen on routers web interface which may vary depending on manufacturer) then press Submit
[![netconf-wl](/images/netconf-wl.png)](/images/netconf-wl.png)

 	
  14. The printer should reboot.

 	
  15. Now connect to your router and check if printer is present.

 	
  16. If so, add it in any OS you would like.

__Source:__ [PC1MH techlog](https://pc1mh-weblog.blogspot.com/2015/03/brother-hl-2135w-on-ubuntu-via-secure.html)