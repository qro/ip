<p align="center">
	<a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/python-3.10.2+-3776AB">
     </a>
     <a href="https://github.com/qro/ip/blob/master/LICENSE">
    	<img src="https://img.shields.io/badge/License-WTFPL-3776AB">
     </a>
</p>

<h1 align="center">
	<img src="https://www.svgrepo.com/show/28319/magnifying-glass.svg" width="150px"><br>
    🔎 ip - a IP multifunctional tool.
</h1>
<p align="center">
    Simple ICMP ping, detailed lookup and local IP check.
 </p>

## 🛠️ Installation
[Releases](https://github.com/qro/ip/releases) are available in this project, if you want to skip the whole installation process.

[Python](https://www.python.org/downloads/) must be installed on your computer; please get the most recent version.

### Windows 🪟
If you're running Windows, you can [download](https://codeload.github.com/qro/ip/zip/refs/heads/master) the .zip file directly from GitHub. In this case, you can still use [Git](https://github.com/git-for-windows/git/releases) to clone my repository. 

Extract the Zip file and then open your command prompt in the same directory
```
$ py main.py
```

### Linux 🐧
If you're running Linux, clone my repository into your own directory by using this command
```
$ sudo apt install git
$ git clone https://github.com/qro/ip.git
$ cd ip
```
From there,
```
$ python3 main.py
```

## ℹ️ Information
- Removed the port scanner from `v1` because it's extremely unstable, but everything else should be cleaned up.
- Added a function to create a `.txt` file and save all your sent ip's with the date and time, pretty useless but yeah.
- If you need any support, pm my [telegram](https://t.me/afqro).