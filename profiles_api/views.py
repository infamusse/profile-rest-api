from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    # Test API View

    def get(self, request, format=None):
        # Return a list of API View
        an_apiview = [
            'Uses HTTP methods as func GET,POST, PATCH, PUT, DELTE',
            'Is similar to traditional Django View',
            'Gives you most control over you app logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
