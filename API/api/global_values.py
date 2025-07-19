"""Global values and constants"""

# HTTP response codes
HTTP_RESPONSES = {
    '400': 'Bad Request: Request cannot be processed by the API',
    '401': 'Not Authorized: Request without successful login session',
    '403': 'Forbidden: Request is missing CSRF token or administrator is missing access profile permissions.',
    '404': 'Resource Not Found: Unable to find the specified resource.',
    '405': 'Method Not Allowed: Specified HTTP method is not allowed for this resource. ',
    '424': 'Failed Dependency: Fail dependency can be duplicate resource, missing required parameter, missing required attribute, invalid attribute value',
    '200': 'OK: Request returns successful',
    }
