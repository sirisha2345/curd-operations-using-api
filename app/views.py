from django.shortcuts import render

# Create your views here.
from app.models import *
from rest_framework.response import Response
from app.serailizers import *
from rest_framework.views import APIView
class curd(APIView):
    def get(self,request,id):
       empo=emp.objects.all()
       jempo=empModelSerializer(empo,many=True)
       return Response(jempo.data)
    def post(self,request,id):
        empo=request.data
        jempo=empModelSerializer(data=empo)
        if jempo.is_valid():
            jempo.save()
            return Response({'insert':'data inserted sucessfully'})
    def put(self,request,id):
        pdo=emp.objects.get(id=id)
        jpdo=empModelSerializer(pdo,data=request.data) 
        if jpdo.is_valid():
            jpdo.save()
            return Response({'insert':'data inserted successfully by update method'})   
        else:
            return Response({'error':'data is not updated by update method'})

    def patch(self,request,id):
        pdo=emp.objects.get(id=id)
        jpdo=empModelSerializer(pdo,data=request.data,partial=True) 
        if jpdo.is_valid():
            jpdo.save()
            return Response({'insert':'data inserted successfully by patch method'})   
        else:
            return Response({'error':'data is not updated by update method'})
    def delete(self,request,id):
        emp.objects.get(id=id).delete()
        return Response({'deletion':'data deleted successfully'})

