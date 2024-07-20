class Database:
    def __init__(self):
        self.users = []

    def add_user(self, nick, login, password):
        self.users.append({'nick': nick, 'login': login, 'password': password})

    def find_user(self, login):
        for user in self.users:
            if user['login'] == login:
                return user
        return None


db = Database()
