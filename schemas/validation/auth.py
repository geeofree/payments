class AuthValidationSchema:
    sign_in_schema = {
        'username': {
            'type': 'string',
            'required': True,
        },
        'password': {
            'type': 'string',
            'required': True,
        },
    }


    sign_up_schema = {
        "username": {
            "type": "string",
            "required": True,
        },
        "password": {
            "type": "string",
            "required": True,
        },
        "role": {
            "type": "string",
            "allowed": ["biller", "customer"],
            "required": True,
        }
    }
