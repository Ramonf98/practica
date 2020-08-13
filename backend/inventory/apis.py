from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status

class UserApi(APIView):


    def post(self):
        serializer = UserSerializers(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data,status =status.HTTP_201_CREATED)
        return Response(serializer.data,stauts=status.HTTP_400_BAD_REQUEST)
