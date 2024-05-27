from flask_login import UserMixin


# class User(UserMixin):
#     def __init__(self, username):
#         self.username = username
#         self.is_authenticated = False  # 默认未认证
#
#     def get_id(self):
#         return self.username
#
#     def authenticate(self):
#         self.is_authenticated = True


class User(UserMixin):
    def __init__(self, username):
        self.username = username

    def get_id(self):
        return self.username
