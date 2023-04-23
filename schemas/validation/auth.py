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
