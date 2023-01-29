# http://localhost:3000/
"""Example app to login to GitHub using the StatefulBrowser class.

NOTE: this is practice only."""

import argparse
from getpass import getpass

import mechanicalsoup


parser = argparse.ArgumentParser(description="Login to Practice.")

browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent='MyBot/0.1: mysite.example.com/bot_info',
)
browser.open("http://localhost:3000/")
print(browser.get_current_page())
# browser.follow_link("login")
