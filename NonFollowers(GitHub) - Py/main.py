from bs4 import BeautifulSoup
import requests


class Follow:

    def __init__(self, username):
        self.username = username
        self.following_URL = f"https://github.com/{self.username}?tab=following"
        self.followers_URL = f"https://github.com/{self.username}?tab=followers"

    def get_following(self):
        following_list = set()
        response = requests.get(self.following_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        usernames = soup.find_all("span", class_="Link--secondary pl-1")
        for username in usernames:
            following_list.add(username.text)
        return following_list
    
    def get_traitors(self):
        traitors = set()
        following_list = self.get_following()
        response = requests.get(self.followers_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        usernames = soup.find_all("span", class_="Link--secondary pl-1")
        for username in usernames:
            if username not in following_list:
                traitors.add(username.text)
        traitors = following_list - traitors 
        for traitor in traitors:
            print(traitor, end=" -\t- ")
            print(f"https://github.com/{traitor}")
            print("- - -")
            
        
