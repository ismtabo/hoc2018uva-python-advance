from flask_jwt_extended import create_access_token, JWTManager
from werkzeug.security import check_password_hash, generate_password_hash

from database import get_user, create_user, is_toke_blacklisted, create_blacklist_token

jwt = JWTManager()

@jwt.token_in_blacklist_loader
def token_in_blacklist_loader(decrypted_token):
    jti = decrypted_token['jti']
    return is_toke_blacklisted(jti)

def login_user(username, password):
    user = get_user(username)
    if not check_password_hash(user.password, password):
        return None
    return create_access_token(username)


def register_user(username, password):
    _ = create_user(username, generate_password_hash(password))
    return create_access_token(username)


def logout_user(token):
    create_blacklist_token(token)
