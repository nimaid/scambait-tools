# Scambait Popup Generator
A Python script for quickly getting tech support scam popups.

## Why would I need this for scambaiting?
The short answer is, **you don't**. All this script does is automate the process of trying out various known scam redirect sites. You could simply use a list like [the Scambait Megalist included in this repo](https://github.com/nimaid/scambait-tools/blob/master/scambait_popup_gen/scambait_megalist.txt) and try out sites by hand, like most people do.

But I thought that took too much time, I wanted a quick and easy way to get popups *fast*. There were some TamperMonkey scripts out there, but they didn't prove satisfactory for me as I wanted to use an old version of Internet Explorer, and I also had to install both TamperMonkey and the script. My ideal solution is to have a standalone, portable `.exe` file, preferably easy to modify and super simple. When I couldn't find anything that didn't sketch me out, I decided to make one.

## What exactly does this do?
The script performs the following tasks, in order:
* It displays some information and asks the user if they want to continue (defaults to no).
  * It firstly warns that this is a program that opens malicious links as it's primary purpose, and to only run in a VM.
  * It also gives advice on how to set up ideal conditions to get scam popups, as the redirect sites will only go to popups if you look "dumb and vulnerable".
* If the user choses to continue, links are randomized and `iexplore.exe` will be invoked with the first URL.
  * The compiled version has the URL list built in.
* It will prompt the user if they wish to re-open the current link, open the next link, or to quit (default).
  * If link is re-opened, `iexplore.exe` is first killed and then re-invoked with the same URL.
  * If the next link is opened, `iexplore.exe` is first killed and then re-invoked with the next URL.
  * If the program is quit, then it will quickly close and leave the current `iexplore.exe` processes running.
* If all links are exhausted, the program will inform the user and then close after the user presses any key

## Is it safe?
**Hell no!** It opens malicious links by design. However, that is literally it's only function, and so otherwise it's perfectly safe. [A couple obscure anti-viruses pick the compiled `.exe` up](https://www.virustotal.com/gui/file/8d5450672aac59f93109fee87af0d6eaa4e6a2038641016edbe19161d1c39881/detection), but I'm guessing that's due to it, you know, opening malicious links and all. If you're super paranoid, you can either install Python 3 on your VM or just compile the `.exe` yourself. This repo includes a Conda environment and a `build.bat` script which outputs the `.exe` to the `dist` folder it creates.

## Where do I download the pre-built .exe?
[Here.](https://github.com/nimaid/scambait-tools/releases/latest) All you need is that one `.exe` file.

## I'm not getting any tech support popups! Just "this domain is for sale", "buy this software", or legitimate sites!
These sites are clever, and will not redirect to the live scam popups unless you look "dumb and vulnerable". Otherwise, they will redirect just to squatter sites, scam software sites, affiliate links, or a legitimate website

Read the instructions in the program. I will also reiterate them below:
* **USE A DARN VM FOR THIS!!! THESE ARE DANGEROUS LINKS!!!**
* **Temporarily** disable your VPN (host, don't run on guest)
  * These sites can see if the IP is from a known VPN provider.
  * After finding a popup, **turn that VPN back on!**
* Disable your web shields in your anti-virus (host + optionally guest)
  * Web shields will usually block these sites as soon as a connection attempt is made.
* Disable any popup blockers, including the ones built-in to the browser (guest)

## Good luck, and happy baiting!
If you have suggestions or think you've found a bug, feel free to make a bug report here on GitHub.