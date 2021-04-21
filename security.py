from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authentication(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


# this function is unique to Flask-JWT
# payload is the context of JWT token
def identity(payload):
    userid = payload['identity']
    return UserModel.find_by_userid(userid)
