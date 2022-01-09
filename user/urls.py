from django.urls import path
from . import views
urlpatterns = [
    #path('user/' , views.productApi),
    path('new/', views.productApi),
    path('product/<str:id>/' , views.deleteProduct),

]