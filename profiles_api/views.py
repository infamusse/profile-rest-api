from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers, models, permissions


class HelloApiView(APIView):
    # Test API View
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        # Return a list of API View
        an_apiview = [
            'Uses HTTP methods as func GET,POST, PATCH, PUT, DELTE',
            'Is similar to traditional Django View',
            'Gives you most control over you app logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        # Create hello message with our name
        print('request', request)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        # Handle updating an obj
        serializer = self.serializer_class(data=request.data)
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        # Handle a partial update an obj
        serializer = self.serializer_class(data=request.data)
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        # Handle del an obj
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    # Test Viewset

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        # Return hello message

        a_viewset = [
            'Provides more funcionality with less code',
            'Automaticly maps to URLs using Routes'
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        print('request', request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrive(self, request, pk=None):
        # Handle getting obj by ID
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        # Handle udpt obj
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        # Handle updt partt obj by ID
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        # Handle rmv
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    # Handle creating and updt profiles
    serializer_class = serializers.UserProfilesSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email', )


class UserLoginApiView(ObtainAuthToken):
    # Handle user auth tokens
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
