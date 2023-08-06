#importing relevant packages/modules
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from .models import add_book,add_user

'''This class is for viewing all the data of books'''
class add_bookListView(ListView):
    model = add_book
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

'''This class is for viewing all the data of users'''
class add_userListView(ListView):
    model = add_user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

''' This class contains the home page of the management system
    It will be convinient to navigate to other pages.
'''
class home(View):
    def get(self,request):
        return render(request, 'home.html')

''' This function add books details to the data base'''
def Add_book(request):
    data = dict(request.POST)
    print(data)
    if (len(data.keys()) > 1):
        row=add_book(book_name=data["book_name"][0],book_serial_number=data["book_serial_number"][0])
        row.save()
    return render(request, 'add_book.html')

''' This function add users details to the data base'''
def Add_user(request):
    data = dict(request.POST)
    print(data)
    if (len(data.keys()) > 1):
        row=add_user(user_name=data["user_name"][0],email=data["email"][0],phone_number=data["phone_number"][0])
        row.save()
    return render(request, 'add_user.html')

''' This function rent books'''
def Rent_book(request):
    data = dict(request.POST)
    print(data)
    msg1 = 'Rented Sucessfully'
    msg2 = 'User Already Rented a book'
    msg3="User not anything"
    if (len(data.keys()) > 1):
        try:
            user_rented = add_user.objects.get(email=data['email'][0])
            book_rented = add_book.objects.get(book_serial_number=data['book_serial_number'][0])
            if book_rented.rented == 0 and user_rented.book_serial_number == "":
                user_rented.book_serial_number = data["book_serial_number"][0]
                user_rented.cost_per_day = data["cost_per_day"][0]
                user_rented.days_of_rent = data["days_of_rent"][0]
                book_rented.rented = 1
                user_rented.save()
                book_rented.save()
                return render(request, "rent_book.html", {"msg1": msg1})
            else:
                return render(request, "rent_book.html", {"msg2": msg2})
        except:
            return render(request, "rent_book.html", {"msg3": msg3})
    return render(request, "rent_book.html")

''' This function is for return of the rented books'''
def Return_book(request):
    data = dict(request.POST)
    print(data)
    msg = 'Sucessfully Returned'
    msg1 = 'Book Not Rented'
    msg3 = "User not exist"
    msg4='User havent rented'
    if(len(data.keys())> 1):
        try:
            user_return = add_user.objects.get(email=data['email'][0])
            book_return = add_book.objects.get(book_serial_number = user_return.book_serial_number)
        except:
            return render(request, "return_book.html", {"msg3": msg3})

        if user_return.book_serial_number != "" :
            if book_return.rented == 1:
                user_return.cost_per_day = 0
                user_return.days_of_rent = 0
                user_return.book_serial_number = ""
                book_return.rented = 0
                user_return.save()
                book_return.save()
                return render(request,"return_book.html",{"msg":msg})
            else:
                return render(request, "return_book.html", {"msg4": msg4})
        else:
            return render(request,"return_book.html",{"msg":msg1})


    return render(request,"return_book.html")


''' This function is for deleting book from the database'''
def Delete_book(request):
    data = dict(request.POST)
    print(data)
    msg = 'Deleted Sucessfully'
    msg1 = 'Book Already Rented'
    if(len(data.keys())> 1):
        delete_row = add_book.objects.get(book_serial_number=data['book_serial_number'][0])
        if delete_row.rented == 0:
            delete_row.delete()
            return render(request,"deletebook.html",{'msg':msg})

        else:
            return render(request,"deletebook.html",{'msg1':msg1})
    return render(request,"deletebook.html")

''' This function is for deleting user from the database'''
def Delete_user(request):
    data = dict(request.POST)
    print(data)
    msg = 'Deleted Sucessfully'
    msg1 = 'Book Already Issued to User'
    if(len(data.keys())> 1):
        delete_row = add_user.objects.get(email=data['email'][0])
        if delete_row.book_serial_number == "":
            delete_row.delete()
            return render(request,"deletebook.html",{'msg':msg})
        else:
            return render(request,"deletebook.html",{'msg1':msg1})
    return render(request,"deleteuser.html")