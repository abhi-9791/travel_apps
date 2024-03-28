
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler
from rest_framework.response import Response


class Not_Valid_Exception(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Make sure coorect Information.'
    default_code = 'error'

class NotFound_Exception(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Details Not found.'
    default_code = 'not_found'

class Unauthorized_Exception(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'You don"t have permissions.'
    default_code = 'unauthorized'
