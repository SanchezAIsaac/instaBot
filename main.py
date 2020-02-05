from selenium import webdriver
from time import sleep
from getpass import getpass
from bs4 import BeautifulSoup


class InstaBot(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com/accounts/login/")
        sleep(2)
        userInput = self.driver.find_element_by_xpath(
            "//input[@name='username']"
        )
        passInput = self.driver.find_element_by_xpath(
            "//input[@name='password']"
        )
        loginButton = self.driver.find_element_by_xpath(
            "//button[@type='submit']"
        )
        userInput.send_keys(username)
        passInput.send_keys(password)
        loginButton.click()
        sleep(2)

    def get_follower_set(self):
        return self._get_set("followers")

    def get_following_set(self):
        return self._get_set("following")

    def quit(self):
        self.driver.quit()
        print("Goodbye {}.".format(self.username))

    def _get_set(self, destination):
        followSet = set()
        print("Retrieving usernames from \"{}\" tab".format(destination))
        self.driver.get("https://instagram.com/{}".format(self.username))
        sleep(4)
        followsLink = self.driver.find_element_by_xpath(
            "//a[@href='/{}/{}/']".format(self.username, destination)
        )
        followsLink.click()
        sleep(2)
        while True:
            try:
                omwye = self.driver.find_element_by_xpath(
                    "//div[@class='oMwYe']"
                )
            except:
                sleep(4)
                try:
                    omwye = self.driver.find_element_by_xpath(
                        "//div[@class='oMwYe']"
                    )
                except:
                    break
            self.driver.execute_script(
                "document.querySelector('div.isgrP').scrollTo(0, document.querySelector('div.isgrP').scrollHeight);"
            )
            sleep(0.75)
        sleep(2)
        print("done \n")
        content = self.driver.page_source
        soup = BeautifulSoup(content, 'lxml')
        for link in soup.find_all('a'):
            followSet.add(link.get("title"))
        followSet.remove(None)
        return followSet


if __name__ == "__main__":
    username = input("username: ")
    password = getpass(prompt="password: ")

    botty = InstaBot(username, password)

    followingSet = botty.get_following_set()
    followerSet = botty.get_follower_set()

    print("\nThe following users are not following you back:")
    print(followingSet - followerSet)

    botty.quit()
