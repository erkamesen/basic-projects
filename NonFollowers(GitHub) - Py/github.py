from bs4 import BeautifulSoup
import requests


class Follow:

    def __init__(self, username):
        self.username = username
        self.following_URL = f"https://github.com/{self.username}?tab=following"
        self.followers_URL = f"https://github.com/{self.username}?tab=followers"
        self.following_set = set()
        self.followers_set = set()
        self.get_followers()
        self.get_following()


    @staticmethod
    def _get_request(link):
        response = requests.get(link)
        soup = BeautifulSoup(response.content, "html.parser")
        usernames = soup.find_all("span", class_="Link--secondary")
        return usernames
    
    def _get_usernames(self, track):
        """"sumary_line
        
        Keyword arguments:
        track-- following or followers
        Return: returns a set of users
        """
        usernames_set = set()
        count = 1
        if track == "following":
            link = self.following_URL
        else:
            link = self.followers_URL
        while True:
            if count < 2:
                usernames = self._get_request(link=link)
                for username in usernames:
                    usernames_set.add(username.text) 
                     
                count +=1  
            else:
                link = self.followers_URL[:-13]+f"page={count}&tab={track}"
                
                usernames = self._get_request(link=link)
                if usernames:
                    for username in usernames:
                        usernames_set.add(username.text)
                    count += 1
                else:
                    break
        return usernames_set


    def get_following(self):
        self.following_set = self._get_usernames(track="following")
        return self.following_set

    def get_followers(self):
        self.followers_set = self._get_usernames(track="followers")
        return self.followers_set
    
    def non_followers(self):
        non_followers_set = self.following_set - self.followers_set
        return list(non_followers_set)



if __name__ == "__main__":
    username = input("Please enter your username for analyze: ")
    tracker = Follow(username=username)
    print("Non-Following List: ")
    print(*tracker.non_followers())
    print("URLs : ")
    for username in tracker.non_followers():
        print(f"https://github.com/{username}")
        