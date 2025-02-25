from rest_framework import views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.authtoken.models import Token

from utils.response import ApiResponse

from apps.users.models import User


class PinCreateAPIView(views.APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request, format=None):
        """
        User Singup/Login
        required fields: mobile_number(Unique)
        return: 200: {}, 500: Error
        """
        mobile_number = request.data.get("mobile_number")

        try:
            user_obj, is_created_user = User.objects.get_or_create(
                mobile_number=mobile_number,
            )

            pin = 1111

            user_obj.pin = pin
            user_obj.save()

            data = {}

            success_response = ApiResponse(
                success=True,
                code=200,
                data=data,
                message='Pin has been created successfully',
            )

            return Response(success_response, status=HTTP_200_OK)

        except Exception as e:
            response = ApiResponse(
                success=False,
                code=500,
                error={
                    'code': str(e),
                    'detail': 'Server error',
                }
            )

            return Response(response, status=HTTP_200_OK)


class PinVerifyAPIView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        mobile_number = request.data.get("mobile_number")
        pin = request.data.get("pin")

        try:
            user = User.objects.get(mobile_number=mobile_number)

        except User.DoesNotExist as e:
            response = ApiResponse(
                success=False,
                code=404,
                error={
                    'code': 'user_not_found',
                    'detail': 'User not found in the database',
                }
            )
            return Response(response)

        try:
            if pin == user.pin:
                token, _ = Token.objects.get_or_create(user=user)

                data = {
                    'token': token.key,
                }

                success_response = ApiResponse(
                    success=True,
                    code=200,
                    data=data,
                    message='Token has been created successfully',
                )

                return Response(success_response, status=HTTP_200_OK)

            else:
                response = ApiResponse(
                    success=False,
                    code=401,
                    error={
                        'code': 'pin_not_valid',
                        'detail': 'Pin not valid',
                    }
                )
                return Response(response)

        except Exception as e:
            response = ApiResponse(
                success=False,
                code=500,
                error={
                    'code': str(e),
                    'detail': 'Server error',
                }
            )

            return Response(response, status=HTTP_200_OK)
