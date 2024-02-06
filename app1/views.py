# from django.shortcuts import render
# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # from rest_framework import status
# from .models import Movie
# from django.http import JsonResponse
# # Create your views here.

# # class CarListCreateAPIView(APIView):
# #     def get(self,request):
# #         cars = Car.objects.all()
# #         serializer = CarSerializer(cars,many=True)
# #         return Response(serializer.data)
    
# #     def post(self, request):
# #         serializer = CarSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors)
    
# # class CarRetrieveUpdateDeleteAPIView(APIView):
# #     def get_object(self,pk):
# #         try:
# #             return Car.objects.get(pk=pk)
# #         except Car.DoesNotExist:


# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {'movies': list(movies.values())}
#     return JsonResponse(data)   

# def movie_details(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         'name': movie.name,
#         'description' : movie.description,
#         'active': movie.active
#     }
#     print(movie.name)
#     return JsonResponse(data)   