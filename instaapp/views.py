from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Comment
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm, CommentForm, PostForm
from django.contrib import messages
from django .contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from datetime import datetime


# Create your views here.


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            return redirect('login')


    context = {'form': form}
    return render(request,'accounts/register.html',context)

def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username = username,password= password)
        if user is not None:
            login(request,user)
            return redirect('auth')
            
        else:
            messages.info(request,'Username or password is incorrect')
            

    context = {}
    return render(request,'accounts/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
def logincup(request):
    return render(request,'index.html')


def userPage(request):
    context = {}

    return render(request,'accounts/user.html',context)




def profile(request):
    user = request.user
    user = Profile.objects.get_or_create(user= request.user)
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)                         
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated successfully!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user': user

    }

    return render(request, 'accounts/profile.html', context)

@login_required(login_url='login')
def create_post(request):
    current_user = request.user
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid:
            post = form.save(commit= False)
            post.author = current_user
            post.save()
        return redirect('post_list')
    else:
        form = PostForm()
    return render(request,'create_post.html',{'form':form})



    

def add_comment(request,pk):
    post = Post.objects.get(pk = pk)
    form = CommentForm(request.POST,instance=post)
    if request.method == "POST":
        if form.is_valid():
            name = request.user.username
            comment_body = form.cleaned_data['comment_body']
            context = Comment(post=post,name =name,comment_body =comment_body,date_added=datetime.now())

            context.save()
            return redirect('post_list')
        else:
            print('form is invalid')

    else:
        form = CommentForm

    context = {
        'form':form
    }
    return render(request,'tag.html',context)



def delete_comment(request,pk):
    comment =Comment.objects.filter(post = pk).last()
    comment.delete()
    return redirect('post_list')




def search_results(request):
    if 'author' in request.GET and request.GET["author"]:
        search_term = request.GET.get("author")
        searched_articles = Post.search_category(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"categories": searched_articles})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})



def index(request):
    current_user = request.GET.get('user')
    logged_in_user = request.user.username
    return render(request,'index.html',{'current_user':current_user})