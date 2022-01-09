from rest_framework import fields, serializers
from user.models import user , product
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('userId', 'Email' , 'firstName' , 'lastName' , 'password')
class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ('productId', 'name' , 'price')