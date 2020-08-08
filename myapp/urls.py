from django.urls import path
from myapp.views import index,detail,PostCreate,like,books

app_name = 'myapp'

urlpatterns = [
	path('',index,name = 'index'),
	path('detail/<int:pk>/',detail,name ='detail'),
	path('create/',PostCreate.as_view(),name = 'create'),
	path('ajax/like/',like,name = 'like'),
	path('books/',books,name="books"),
]