# Introduction
This is a simple python script used to automate the process of deleting all your messages in a private Discord conversation. It is slow, but I cannot 
make it faster without triggering 429 response codes (Too Many Requests). To use this script, you need to have Python 3 installed.

On most Linux distributions, you can install it using `sudo apt install python3` if it is not already installed. For Windows, you can download it [here](https://www.python.org/downloads/).

# Usage
- First, you need to get your authorization token. [This guide](https://gist.github.com/MarvNC/e601f3603df22f36ebd3102c501116c6) can help you with that.
- Then, you'll need the ID of the conversation in which you want to delete your messages. To do so, you can right click the conversation and select "Copy Channel Id" (It seems to be only available on the desktop application).
- Finally, you'll need to specify your username (not your display name but your real username

When you have those 3 information, you can specify them at the beginning of the script, and then simply run it using `python3 discord_bulk_delete.py`. 

You can let the script run for a while, it is slow to avoid being blocked for sending too much requests per seconds.
