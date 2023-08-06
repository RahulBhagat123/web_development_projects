#importing relevant packages/modules
from django.urls import path
from . import views

#urls of each pages containing different operations
urlpatterns = [
    path('bookdetails/',views.add_bookListView.as_view()),
    path('userdetails/', views.add_userListView.as_view()),
    path('home/',views.home.as_view()),
    path('addbook/', views.Add_book),
    path('adduser/', views.Add_user),
    path('rentbook/',views.Rent_book),
    path('returnbook/',views.Return_book),
    path('deletebook/',views.Delete_book),
    path('deleteuser/',views.Delete_user),

]