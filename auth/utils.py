import jwt
import datetime

jwt_secret_key = '123'


def generate_token(user_info):
    payload = {
        'user_info': user_info,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30)
    }
    token = jwt.encode(payload, jwt_secret_key, algorithm='HS256')
    return token


def decode_token(token):
    try:
        payload = jwt.decode(token, jwt_secret_key, algorithms=['HS256'])
        return payload['user_info']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

