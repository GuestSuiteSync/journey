from rest_framework import views
from rest_framework.response import Response

class Users(views.APIView):
    def get(self, request):
        return Response({"message": "List of users"})

    def post(self, request):
        return Response({"message": "Create a new user"})