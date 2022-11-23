# AdminGrabber
AdminGrabber is a simple admin panel finder script which find admin panels of any site using a wordlist

**Requirements**
- Python27

**Tested on**
- Windows 7/8/10 
- Ubuntu 14.04.4 LTS

**Installation**

You can download the latest version of AdminGrabber by cloning the GitHub repository:

`git clone https://github.com/shariqmalik/AdminGrabber.git`

**Useage**

`$ python adgrab.py`

**Output:**

```bash
user@box:~$python adgrab.py
  ___      _           _       _____           _     _
 / _ \    | |         (_)     |  __ \         | |   | |
/ /_\ \ __| |_ __ ___  _ _ __ | |  \/_ __ __ _| |__ | |__   ___ _ __
|  _  |/ _` | '_ ` _ \| | '_ \| | __| '__/ _` | '_ \| '_ \ / _ \ '__|
| | | | (_| | | | | | | | | | | |_\ \ | | (_| | |_) | |_) |  __/ |
\_| |_/\__,_|_| |_| |_|_|_| |_|\____/_|  \__,_|_.__/|_.__/ \___|_|

        Author: Shariq Malik

Enter URL: http://example.com
```

**Load wordlist.txt**

```bash
user@box:~$python adgrab.py
  ___      _           _       _____           _     _
 / _ \    | |         (_)     |  __ \         | |   | |
/ /_\ \ __| |_ __ ___  _ _ __ | |  \/_ __ __ _| |__ | |__   ___ _ __
|  _  |/ _` | '_ ` _ \| | '_ \| | __| '__/ _` | '_ \| '_ \ / _ \ '__|
| | | | (_| | | | | | | | | | | |_\ \ | | (_| | |_) | |_) |  __/ |
\_| |_/\__,_|_| |_| |_|_|_| |_|\____/_|  \__,_|_.__/|_.__/ \___|_|

        Author: Shariq Malik

Enter URL: http://example.com
---------------------------------------------------------------------
[Connecting] : http://example.com...
[Connected]  : http://example.com is connected
---------------------------------------------------------------------

Enter Wordlist: wordlist.txt
---------------------------------------------------------------------
[Loading] : Loading Panels..
[Loaded]  : 7 Panels Loaded..
[Using]   : 5/7 Panels being used (2 duplicates)..
---------------------------------------------------------------------

[Checking] : Checking Admin Panels
---------------------------------------
| Resp  :       Results               |
---------------------------------------
[OK] : http://example.com/admin/

```

**Note**
This is just for educational purposes I'll not responsible of any harm!
