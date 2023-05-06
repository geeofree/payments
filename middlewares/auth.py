from flask import session, request, current_app
from utils.http import json_response
from services import AuthService
import jwt

class AuthMiddleware:
    @staticmethod
    def validate_token():
        """
        Validates the bearer token in the request header.

        :return: Returns a JSON response if there are errors during token decoding:

                 - No Authorization Header: If the request has no Authorization header, 
                   return a 400 JSON response.

                 - Not 'Bearer' Schema: If the Authorization header isn't using the 'Bearer' 
                   schema, return a 400 JSON response.

                 - No Token: If no token is provided, return a 400 JSON response.

                 - Malformed Token: If the token is malformed, return a 406 JSON response.

                 - Expired Token: If the token has expired, return a 406 JSON response.
        """
        authorization = request.headers.get("authorization")

        if authorization == None:
            return json_response("No authorization header given.", 400)

        try:
            scheme, token = authorization.split()

            if scheme.lower() != "bearer":
                return json_response("Authorization header only accepts 'Bearer' scheme", 400)

            AuthService.decode_token(token)
        except jwt.DecodeError as decode_error:
            return json_response("Could not decode token: {}".format(decode_error), 406)
        except jwt.ExpiredSignatureError:
            return json_response("Token is expired. Please sign-in again.", 406)
        except ValueError:
            return json_response("No token given.", 400)
