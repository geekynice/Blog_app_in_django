from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from blog_app.models import News
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def index(request):
    news = News.objects.all()
    return render(request, 'blog_app/index.html', {'news' : news})

@login_required()
def delete(request, id):
    news = News.objects.get(id=id)
    news.delete()

    return redirect('index')

@login_required()
def add(request):
    news = News.objects.all()
    if request.method == 'GET':
        return render(request, 'blog_app/edit.html', {'news':news})
    else:
        title = request.POST['title']
        description = request.POST['description']
        News.objects.create(title=title,description=description,user_id=request.user.id)
        
        return redirect('index')

@login_required()
def edit(request, id):
    news = News.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'blog_app/edit.html', {'news':news})
    else:
        news.title = request.POST['title']
        news.description = request.POST['description']
        news.save()

        return redirect('index')
                                                

def register(request):
    if request.method == 'GET':
        return render(request, 'blog_app/register.html')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(first_name=first_name, last_name=last_name, 
                            email=email, username=username, password=password)

        send_mail('Account Created', 
                    f'Your account has been created and registered with username {username}',
                    settings.EMAIL_HOST_USER,
                    ['nicebanjaraa@gmail.com'],
                     fail_silently=False)

        return redirect('index')

def signin(request):
    if request.method == 'GET':
        return render(request, 'blog_app/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url is None:
                return redirect('index')
            else:
                return redirect(next_url)
        else:
            return redirect('signin')

@login_required()
def signout(request):
    logout(request)
    return redirect('signin')