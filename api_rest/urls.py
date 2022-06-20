from django.urls import path
from api_rest.views import agregarP,controlP
from api_rest.viewsLogin import login

urlpatterns = [
    path('agregarP/',agregarP,name="agregarP"),
    path('controlP/<idP>/',controlP,name="controlP"),
    path('login/',login,name="login"),
]