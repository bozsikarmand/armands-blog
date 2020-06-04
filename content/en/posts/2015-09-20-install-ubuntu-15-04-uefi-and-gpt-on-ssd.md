---
author: bozsikarmand
comments: true
date: 2015-09-20 10:32:13+00:00
layout: post
link: https://blog.bozsikarmand.hu/2015/09/20/install-ubuntu-15-04-uefi-and-gpt-on-ssd/
slug: install-ubuntu-15-04-uefi-and-gpt-on-ssd
title: Install Ubuntu 15.04 (UEFI and GPT on SSD)
wordpress_id: 341
categories:
- Desktop
- Install
tags:
- '15.04'
- install
- ubuntu
---

I was searching for days to answer all of my questions related to this topic, but I had no success, until I asked it on PROHARDVER!.

At first: I was afraid what will happen with the wearing level on my Samsung 830 SSD, will the partition alignment and TRIM be OK...
Then: I did not know anything about current hardware support of Ubuntu.

**A short how to how I installed Ubuntu on my system:**



	
  1. Since I was using Windows 10 I have disabled "Fast Startup", checked BitLocker is off and turned off hibernation (_powercfg /h off_).
[![81834_bl](https://blog.bozsikarmand.hu/wp-content/uploads/2015/09/81834_bl-300x74.png)](https://blog.bozsikarmand.hu/wp-content/uploads/2015/09/81834_bl.png)[![81834_powercfga](https://blog.bozsikarmand.hu/wp-content/uploads/2015/09/81834_powercfga-251x300.png)](https://blog.bozsikarmand.hu/wp-content/uploads/2015/09/81834_powercfga.png)[![81834_nof](https://blog.bozsikarmand.hu/wp-content/uploads/2015/09/81834_nof-300x211.png)](https://blog.bozsikarmand.hu/wp-content/uploads/2015/09/81834_nof.png)

	
  2. Disabled Fastboot in UEFI
[![81834_fastboot](https://blog.bozsikarmand.hu/wp-content/uploads/2015/09/81834_fastboot-300x225.png)](https://blog.bozsikarmand.hu/wp-content/uploads/2015/09/81834_fastboot.png)

	
  3. Also disabled Secure Boot (Switched to "Other OS")
[![81834_secboot](https://blog.bozsikarmand.hu/wp-content/uploads/2015/09/81834_secboot-300x225.png)](https://blog.bozsikarmand.hu/wp-content/uploads/2015/09/81834_secboot.png)

	
  4. Booted from UEFI pendrive.

	
  5. Created an 1024MB fat32 primary partition (with the label "EFI") with a free space of 1MiB preceding

	
  6. I have 16GB of RAM so I created a 16384MB swap partition with linux-swap file system.

	
  7. The rest (without the 10-15% provisioning space) went for / (root) with ext4.

	
  8. Agreed the UEFI install warning
[![Force-UEFI-Installation](https://blog.bozsikarmand.hu/wp-content/uploads/2015/09/Force-UEFI-Installation-300x225.jpeg)](https://blog.bozsikarmand.hu/wp-content/uploads/2015/09/Force-UEFI-Installation.jpeg)

	
  9. Then the install method was the same like on a BIOS machine.

	
  10. I have installed fglrx for my Radeon R9 270X

	
  11. Turned volume to maximum in alsamixer for my Xonar DS in Master Front
[![alsamixer](https://blog.bozsikarmand.hu/wp-content/uploads/2015/09/alsamixer-300x177.png)](https://blog.bozsikarmand.hu/wp-content/uploads/2015/09/alsamixer.png)

	
  12. That's all!


Thanks for reading!

__Sources:__ [UEFI settings (Image)](http://www.eightforums.com/tutorials/17058-secure-boot-enable-disable-uefi-2.html), [Message (Image)](http://www.tecmint.com/wp-content/uploads/2015/04/Force-UEFI-Installation.jpeg)