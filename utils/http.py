def json_response(message, status_code=200, data=None):
    res = { 'status': status_code, 'message': message }
    if data != None:
        res['data'] = data
    return (res, status_code)
