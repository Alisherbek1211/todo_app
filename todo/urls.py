from django.urls import path
from .views import delete, homepage,loginpage, logoutuser,registerpage, todo, update

urlpatterns = [
    path('',homepage,name="homepage"),
    path('todo/',todo,name="todo"),
    path('login/',loginpage,name="login"),
    path('register/',registerpage,name="registerpage"),
    path('logout/',logoutuser,name="logoutuser"),
    path('delete/<str:user>/<int:id>/',delete,name='delete'),
    path('update/<str:user>/<int:id>/',update,name='update'),
    
]
