from flask import request
from cerberus import Validator
from utils.http import json_response
import functools

class ValidationMiddleware:
    @staticmethod
    def json_schema(schema):
        """
        Middleware for decorating a controller/flask route to validate
        the request body's JSON payload.

        :param dict schema: A dictionary to define the validator schema.
        :return: A JSON response. If the validator is invalid it will return
                 a 406 status code with the errors of properties with erroneous
                 values or inputs.
        """
        def decorator(func):
            @functools.wraps(func)
            def decorated(*args, **kwargs):
                validator = Validator(schema)
                is_valid = validator.validate(request.json)

                if not is_valid:
                    return json_response("Validation error.", status_code=406, data=validator.errors)
                return func(*args, **kwargs)

            return decorated
        return decorator
