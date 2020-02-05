A working Instagram "bot" that scrapes the desktop version of the site using known login credentials. If ran, asks the user from the command line for Instagram username and password. Returns the set of people who the user follows but doesn't have a follow back from.


Documentation:
- New object: InstaBot(username, password)
	- Username and password as required arguments.
	- Methods:
		- "get_follower_set": returns the set of usernames who are found under "followers."
		- "get_following_set": returns the set of usernames who are found under "following."
		- "quit": closes the webdriver and terminates the current bot.

Neccesary libraries needed to run main.py:
- Selenium
- BeautifulSoup4

Other neccesary components:
- Chrome Webdriver (https://chromedriver.chromium.org/downloads)
- Internet connection
