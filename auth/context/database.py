#database user
class Database:
    def __init__(self):
        self.users = []

    def add_user(self, login, password):
        self.users.append({'login': login, 'password': password})

    def find_user(self, login):
        for user in self.users:
            if user['login'] == login:
                return user
        return None

    def find_user_by_login_and_password(self, login, password):
        for user in self.users:
            if user['login'] == login and user['password'] == password:
                return user
        return None

db = Database()
