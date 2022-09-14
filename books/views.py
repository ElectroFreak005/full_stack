from django.shortcuts import render
from books.models import Book, User
from django.http import HttpResponse , HttpResponseRedirect
# Create your views here.

def home(request):
    return render(request, "home.html")

def viewbooks(request):
    books = Book.objects.all()
    return render(request, "viewbooks.html", {"books": books})

def reservebooks(request):
    if request.method == 'POST':
        isbn = request.POST['book_isbn']
        email = request.POST['user_email']
        phoneno = request.POST['phono']
        username = request.POST['user_name']
        try:
            user = User(isbn=isbn, mail_id=email, phno=phoneno, name=username)
            book = Book.objects.get(isbn=isbn)
            book.av_count-=1
            book.save()
            user.save()
            return HttpResponseRedirect("/guest/reserve_success/")
        except:
            return HttpResponseRedirect("/guest/reserve_failed/")
    else:
        return render(request, "reservebooks.html")

def viewreservations(request):
    users = User.objects.all()
    return render(request, "viewreservations.html", {"users": users})

def success(request):
    return render(request, "success.html")

def failed(request):
    return render(request, "failed.html")

def cancel(request):
    if request.method == 'POST':
        reser_id = request.POST['reser_id']
        email = request.POST['user_email']
        phoneno = request.POST['phono']
        try:
            user = User.objects.get(resver_id=reser_id)
            isbn = user.isbn
            user.status = False
            book = Book.objects.get(isbn=isbn)
            book.av_count+=1
            book.save()
            user.save()
            return HttpResponseRedirect("/guest/reserve_success/")
        except:
            return HttpResponseRedirect("/guest/reserve_failed/")
    else:
        return render(request, "cancel.html")