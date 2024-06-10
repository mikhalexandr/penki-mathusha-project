from flask import request
from functools import wraps
from keycloak import KeycloakOpenID
import consts


keycloak_openid = KeycloakOpenID(
    server_url=consts.KEYCLOAK_SERVER_URL,
    client_id=consts.KEYCLOAK_CLIENT_ID,
    realm_name=consts.KEYCLOAK_USER_REALM_NAME,
    client_secret_key=consts.KEYCLOAK_CLIENT_SECRET_KEY
)


def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return {"message": "Authentication required"}, 401

        token = auth_header.split(" ")[1]

        try:
            token_info = keycloak_openid.introspect(token)
            if not token_info.get("active"):
                print("Invalid token active")
                return {"message": "Invalid token"}, 401
        except Exception as e:
            print("Auth error:", e)
            return {"message": "Invalid token"}, 401

        if token_info["realm_access"]["roles"][0] != "admin":
            print("Not admin")
            return {"message": "Not admin"}, 401

        return func(*args, **kwargs)

    return wrapper
