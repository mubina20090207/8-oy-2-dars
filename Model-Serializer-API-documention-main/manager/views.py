from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

from .models import *
from .serializer import *
from .permissions import StaffModelPermissions


class KlassView(APIView):
    queryset = Klass.objects.all()
    permission_classes = [StaffModelPermissions]

    def get(self, request, pk=None):
        if pk:
            try:
                klass = Klass.objects.get(pk=pk)
                return Response(KlassSerializer(klass).data)
            except Klass.DoesNotExist:
                return Response({'error': "Information not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            klass = Klass.objects.all()
            return Response(KlassSerializer(klass, many=True).data)

    def post(self, request, pk=None):
        if pk:
            return Response({'error': "Method POST not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        serializer = KlassSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()

        return Response(KlassSerializer(data).data)

    def put(self, request, pk=None):
        if not pk:
            return Response({'error': "Method PUT not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        try:
            klass = Klass.objects.get(pk=pk)

            serializer = KlassSerializer(data=request.data, instance=klass)
            serializer.is_valid(raise_exception=True)
            data = serializer.save()

            return Response(KlassSerializer(data).data)

        except Klass.DoesNotExist:
            return Response({'error': "Information not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        if not pk:
            return Response({'error': "Method DELETE not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        try:
            klass = Klass.objects.get(pk=pk)
            klass.delete()

            return Response({'message': "The object has been removed."})
        except Klass.DoesNotExists:
            return Response({'error': "Information not found."}, status=status.HTTP_404_NOT_FOUND)


class HotelView(APIView):
    queryset = Hotel.objects.all()
    permission_classes = [StaffModelPermissions]

    def get(self, request, pk=None):
        if pk:
            try:
                hotel = Hotel.objects.get(pk=pk)
                return Response(HotelSerializer(hotel).data)
            except Hotel.DoesNotExist:
                return Response({'error': "Information not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            hotel = Hotel.objects.all()
            return Response(HotelSerializer(hotel, many=True).data)

    def post(self, request, pk=None):
        if pk:
            return Response({'error': "Method POST not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        serializer = HotelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()

        return Response(HotelSerializer(data).data)

    def put(self, request, pk=None):
        if not pk:
            return Response({'error': "Method PUT not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        try:
            hotel = Hotel.objects.get(pk=pk)
            serializer = HotelSerializer(data=request.data, instance=hotel)
            serializer.is_valid(raise_exception=True)
            data = serializer.save()

            return Response(HotelSerializer(data).data)
        except Hotel.DoesNotExist:
            return Response({'error': "Information not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        if not pk:
            return Response({'error': "Method DELETE not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        try:
            hotel = Hotel.objects.get(pk=pk)
            hotel.delete()

            return Response({'message': "The object has been removed."})
        except Hotel.DoesNotExist:
            return Response({'error': "Information not found."}, status=status.HTTP_404_NOT_FOUND)


class TravelView(APIView):
    queryset = Travel.objects.all()
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def get(self, request, pk=None):
        if pk:
            try:
                travel = Travel.objects.get(pk=pk)
                return Response(TravelSerializer(travel).data)
            except Travel.DoesNotExist:
                return Response({'error': "Information not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            travel = Travel.objects.all()
            return Response(TravelSerializer(travel, many=True).data)

    def post(self, request, pk=None):
        if pk:
            return Response({'error': "Method POST not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        serializer = TravelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()

        return Response(TravelSerializer(data).data)

    def put(self, request, pk=None):
        if not pk:
            return Response({'error': "Method PUT not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        try:
            travel = Travel.objects.get(pk=pk)
            serializer = TravelSerializer(data=request.data, instance=travel)
            serializer.is_valid(raise_exception=True)
            data = serializer.save()

            return Response(TravelSerializer(data).data)
        except Travel.DoesNotExist:
            return Response({'error': "Information not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        if not pk:
            return Response({'error': "Method PUT not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        try:
            travel = Travel.objects.get(pk=pk)
            travel.delete()

            return Response({'message': "The object has been removed."})
        except Travel.DoesNotExist:
            return Response({'error': "Information not found."}, status=status.HTTP_404_NOT_FOUND)