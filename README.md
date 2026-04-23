# 📦 Multi-Platform Media Downloader using Gallery-dl

**Professional Multi-Platform Media Downloader** – a robust Windows batch script wrapper for `gallery-dl` featuring an interactive menu, automated folder management, session logging, and cookie support. Download media seamlessly from Twitter, TikTok, YouTube, Instagram, Reddit, and many other platforms.

![Batch](https://img.shields.io/badge/Windows-Batch_script-0078D6?style=flat&logo=windows&logoColor=white)
![gallery-dl](https://img.shields.io/badge/gallery--dl-powered-4CAF50?style=flat)
![Version](https://img.shields.io/badge/version-2.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Table of Contents

- [Key Features](#-key-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Cookie Configuration](#-cookie-configuration-for-private-content)
- [Settings Menu](#️-settings-menu)
- [Folder Structure](#-auto-created-folder-structure)
- [Logging](#-logging)
- [Important Notes](#⚠️-important-notes)
- [Contributing](#-contributing)
- [License](#-license)
- [Credits](#-credits)

---

## ✨ Key Features

- **Multi‑platform support** – Twitter/X, TikTok, YouTube, Instagram, Reddit, and any site compatible with `gallery-dl`
- **Auto‑organised folders** – Each platform stores downloads in a dedicated subfolder under `Downloads/`
- **Download archive** – Prevents duplicate downloads automatically using archive files
- **Cookie management** – Enables access to private content (likes, saved posts, stories)
- **Session logging** – Every run is logged with locale‑independent timestamps
- **Configuration menu** – Reset archives, update `gallery-dl`, open folders, view current settings
- **Clean text‑based UI** – Colour‑coded, professional layout with intuitive sub‑menus
- **Retry & delay** – Built‑in `--retries 3 --sleep 2-4` to avoid rate limiting

---

## 📋 Prerequisites

| Requirement | Details |
|-------------|---------|
| **Operating System** | Windows 7, 8, 10, or 11 |
| **gallery-dl** | Installed and available in `PATH` (see below) |
| **Python** (if using pip) | Python 3.7 or higher |

### Installing gallery-dl

You can install `gallery-dl` using either method:

```bash
# Using pip (recommended)
pip install gallery-dl

# Or download the standalone executable
# from https://github.com/mikf/gallery-dl/releases
# Place gallery-dl.exe in the script folder or add to PATH

## 🚀 Installation
Clone the repository or download the batch file directly:

bash
git clone https://github.com/username/gallery-dl-ultimate-pro.git
cd gallery-dl-ultimate-pro
Then simply run:

bash
Gallery-dl ULTIMATE Pro v2.0.bat
No administrator rights are required under normal circumstances.

## 🖥️ Usage
First Run
On first execution, the script automatically creates the following directories:

Downloads/ – main download folder

Config/ – stores archive files and cookies

Logs/ – stores session logs

If gallery-dl is not found, an error message is displayed and the script exits.

Main Menu
text
+=========================================================+
:         GALLERY-DL ULTIMATE PRO v2.0                    :
:         Professional Media Downloader                    :
+=========================================================+
:   [1]  Twitter / X Manager                               :
:   [2]  TikTok Manager                                    :
:   [3]  YouTube Manager                                   :
:   [4]  Instagram Manager                                 :
:   [5]  Reddit Manager                                    :
:   [6]  Generic URL Download                              :
:   [S]  Settings and Configuration                        :
:   [L]  View Download Logs                                :
:   [Q]  Exit Program                                      :
+=========================================================+
Example: Twitter Manager
After selecting 1, you will see a sub‑menu:

[1] Photos Only (JPG, PNG)

[2] Videos Only (MP4, MOV)

[3] All Media

[4] Liked Posts (requires cookies)

[5] User Timeline

[6] Twitter List

Simply enter the URL or username, and the script executes gallery-dl with the appropriate parameters.

## 🍪 Cookie Configuration (for private content)
Certain features (Liked Posts, Stories, Saved Posts) require authentication cookies.

Setup Instructions
Install the "Get cookies.txt LOCALLY" browser extension for Chrome or Firefox.

Log into your account (Twitter, Instagram, TikTok, etc.).

Export cookies in Netscape format.

Save the file as Config\cookies.txt (or place it inside the Config folder).

Alternatively, use the Settings → Update / Set Cookie File menu to copy a cookie file from another location.

## 🛠️ Settings Menu
Option	Description
Update / Set Cookie File	Manage cookies.txt
Clear Download Archive	Delete all archive files (forces re‑download of all items)
Check gallery-dl Version	Display the installed version of gallery-dl
Update gallery-dl	Run pip install --upgrade gallery-dl
Open Downloads Folder	Open Downloads in Windows Explorer
Open Config Folder	Open Config folder
View Current Configuration	Show summary of paths, arguments, and archive status

## 📂 Auto‑created Folder Structure
text
Gallery-dl ULTIMATE Pro v2.0/
│
├── Gallery-dl ULTIMATE Pro v2.0.bat
│
├── Downloads/
│   ├── Twitter/
│   │   ├── Liked/
│   │   └── Lists/
│   ├── TikTok/
│   │   ├── Liked/
│   │   └── Tags/
│   ├── YouTube/
│   │   ├── Playlists/
│   │   ├── Channels/
│   │   └── Shorts/
│   ├── Instagram/
│   │   ├── Stories/
│   │   ├── Reels/
│   │   └── Saved/
│   ├── Reddit/
│   │   ├── Subreddits/
│   │   └── Users/
│   └── Other/
│
├── Config/
│   ├── cookies.txt
│   ├── twitter_arch.txt
│   ├── tiktok_arch.txt
│   ├── youtube_arch.txt
│   ├── instagram_arch.txt
│   └── ... (other archive files)
│
└── Logs/
    └── session_YYYYMMDD_HHMM.log

## 📜 Logging
Every session is logged to Logs/session_YYYYMMDD_HHMM.log. Each log entry includes:

Timestamp

Download actions

Error messages (if any)

You can view logs via the View Download Logs menu or by opening the Logs folder directly.

## ⚠️ Important Notes
This script is a wrapper for gallery-dl. Please respect the gallery-dl license and the Terms of Service of each platform.

Use responsibly – avoid excessive scraping or any activity that may violate platform rules.

Some features (e.g., Instagram Stories) depend heavily on valid cookies and may break if the platform changes its layout or authentication mechanism.

For gallery-dl specific issues, refer to the official documentation.

## 🤝 Contributing
Contributions are welcome! Feel free to:

Fork the repository

Open issues for bugs or feature requests

Submit pull requests

Suggested Enhancements
Support for additional platforms (Pixiv, Flickr, DeviantArt)

Simple GUI mode

Integration with yt-dlp for richer YouTube features

Multi‑threaded parallel downloads

## 📄 License
This project is licensed under the MIT License – free to use and modify. However, you must comply with each platform's Terms of Service when downloading content.

## 🙏 Credits
gallery-dl – The core download engine

Made with ❤️ for the digital archiving community

For questions or support, please open an issue on GitHub.
