# AdminGrabber
<p>AdminGrabber is a simple admin panel finder script which find admin panels of any site using a wordlist</p>

**Requirements**<br/>
	<li>Python27</li><br/>
**Tested on**<br/>
	<li> Windows 7/8/10 </li>
	<li> Ubuntu 14.04.4 LTS </li><br/>
**Installation**
<p>You can download the latest version of AdminGrabber by cloning the GitHub repository:</p>
<pre><code>git clone https://github.com/shariqmalik/AdminGrabber.git</code></pre>
**Useage**<br/>
<pre><code>$python adgrab.py</code></pre>
**Output:**<br/>
<pre><code>
user@box:~$python adgrab.py
  ___      _           _       _____           _     _
 / _ \    | |         (_)     |  __ \         | |   | |
/ /_\ \ __| |_ __ ___  _ _ __ | |  \/_ __ __ _| |__ | |__   ___ _ __
|  _  |/ _` | '_ ` _ \| | '_ \| | __| '__/ _` | '_ \| '_ \ / _ \ '__|
| | | | (_| | | | | | | | | | | |_\ \ | | (_| | |_) | |_) |  __/ |
\_| |_/\__,_|_| |_| |_|_|_| |_|\____/_|  \__,_|_.__/|_.__/ \___|_|

        Author: Shariq Malik

Enter URL: http://example.com
</code></pre>
**Load wordlist.txt**
<pre><code>
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
Enter Wordlist: hex.txt
</code></pre>
**Script will load list and show results**
<pre><code>
Enter Wordlist: wordlist.txt
---------------------------------------------------------------------
[Loading] : Loading Panels..
[Loaded]  : 4 Panels Loaded..
---------------------------------------------------------------------

[Checking] : Checking Admin Panels
---------------------------------------
| Resp  :       Results               |
---------------------------------------
[OK] : http://example.com/admin/
</code></pre>
**Note**
<p>This is just for educational purposes I'll not responsible of any harm!<p>
