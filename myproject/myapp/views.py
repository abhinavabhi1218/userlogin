from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.utils.html import escape
from .forms import SignForm, LoginForm, PostForm
from .models import Post
from django.db.models import Q




# Create your views here.
# home
def home(request):
    posts = Post.objects.all()
    # print(User.get_username)
    return render(request, 'myapp/home.html', {'posts': posts})


# about
def About(request):
    return render(request, 'myapp/about.html')


# contact
def contact(request):
    return render(request, 'myapp/contact.html')


# dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'myapp/dashboard.html', {'posts': posts, 'full_name': full_name, 'groups': gps})


# logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


# signup
def user_signup(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            messages.success(request, 'congratulations! you have become an Auther.')
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        form = SignForm()
    return render(request, 'myapp/signup.html', {'form': form})


# login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'you are logged successufully !!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'myapp/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')


# add_posts

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                data = Post(title=title, desc=desc)
                data.save()
                messages.success(request, 'Post added successfully')
                form = PostForm()
        else:
            form = PostForm()
        return render(request, 'myapp/addpost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')

# delete Post
def delete_post(request, id):
    if request.user.is_authenticated:
        pk = Post.objects.get(id=id)
        pk.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

# update post
def update_post(request, id):
    if request.user.is_authenticated:
        pk = Post.objects.get(id=id)
        form = PostForm(request.POST, instance=pk)
        if form.is_valid():
            form.save()
            messages.success(request, 'updated successfully')
            form = PostForm()
        else:
            pk = Post.objects.get(id=id)
            form = PostForm(instance=pk)
        return render(request, 'myapp/update_post.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')

def pagenot_found(request, exception):
    return render(request, "myapp/404.html")


# search view
def search_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            search = request.POST['search']
            if search:
                data = User.objects.filter(Q(username__contains=search)|
                                           Q(first_name__contains=search)|
                                           Q(last_name__contains=search)|
                                           Q(email__contains=search))

                if data :
                    return render(request, 'firstapp/search_user.html', {'users':data})

                else:
                    messages.error(request, 'no user found')
            else:
                return HttpResponseRedirect('/search/')
        else:
            return redirect('/')
    else:
        return HttpResponseRedirect('/login/')


