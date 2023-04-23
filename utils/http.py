def json_response(message, status_code=200, data=None):
    """
    Utility for returning JSON responses for flask routes.

    :param str message: The message of the JSON response.
    :param int [status_code]: The status code of the JSON response.
    :param any [data]: A JSON-serializable data value for the JSON response.
    :return: A 2-tuple where the first item is the response dictionary 
             and the last item is the status code.
    """
    res = { 'status': status_code, 'message': message }
    if data != None:
        res['data'] = data
    return (res, status_code)
