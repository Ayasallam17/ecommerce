
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpRequest
from django.views.decorators.http import require_http_methods

from user.models import product,user
from user.serializers import userSerializer,productSerializer
#Create your views here.


@csrf_exempt
def productApi(request):
    if request.method == 'GET':
        print(request)
        products = product.objects.all()
        products_serializer = productSerializer(products , many = True)
        return HttpResponse(products_serializer.data) 
    if request.method == 'POST':
        print("dkfif")
        print(request)
        productData = JSONParser().parse(request)
        print(productData)
        products_serializer = productSerializer(data=productData)
        if products_serializer.is_valid():
            products_serializer.save()
            return HttpResponse("added successfully") 
        return HttpResponse("failed to add")
    elif request.method == 'PUT':
        productData = JSONParser().parse(request)
        producti = product.objects.get(productId = productData['productId'])
        products_serializer = productSerializer(producti , data=productData)
        if products_serializer.is_valid():
            products_serializer.save()
            return HttpResponse("success updating")
        return HttpResponse("failed update")

@csrf_exempt
def deleteProduct(request , id):
    print(id)
    if request.method == 'GET':
        producti = product.objects.get(productId = id)
        producti.delete()
        return HttpResponse("deleted successfully")
    return HttpResponse("failed delete")
    
