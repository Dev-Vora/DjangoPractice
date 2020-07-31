from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from crud.models import Book
from crud.form import ContactForm
from django.core.mail import send_mail,get_connection
# Create your views here.

def index(request):
    return render(request,'searchbook.html') 

def searchbook(request):
    error=False
    if 'bookname' in request.POST and request.POST['bookname']:
        book=request.POST['bookname']
        try:
            res = Book.objects.get(bookname = book)
        except:
            res = None
      
        return render(request,'searchresult.html',{'book':res,'query':book})
       
    else:
        error = True
        return render(request,'searchbook.html',{'error':error})

def contact(request):
    if request.method == 'POST':
        print("if")
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            contact = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                data['subject'],
                data['message'],
                data.get('email','techbuckavpt@gmail.com'),
                ['dvora956@gmail.com'], connection=contact
            )
            return HttpResponseRedirect('contact/thanks/')
        else:
            form = ContactForm()
            return render(request,'contact_form.html',{'form':form})