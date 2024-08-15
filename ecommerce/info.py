from random import randint
from db import UserDb

class Info:
    def __init__(self, fullname) -> None:
        self.fullname = fullname
        self.username = None
        self.password = None
        self.pin = '0000'
        self.customer_Id = None
        self.user_db = fullname + '.txt'
        self.db = 'users.db'

    def register(self):
        print(f'Welcome {self.username}')
        username =input('Enter username: ') 
        password: str = input('Create password: ')
        pin: str = input('Create new PIN(default: 0000)\nPin: ')
        
        if len(password) >= 8:
            if username not in UserDb:
                self.username = username
                # add username to UserDb
            else:
                print('Username must be unique!')
                self.register()
            self.password = password
        else:
            print('Password must be more than 8 characters!')
            self.register()

        
