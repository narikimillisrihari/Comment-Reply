from django.shortcuts import render,redirect
from fbapp.models import Fb_model,Add_post,SignUp,Comment,comment_reply
from fbapp.forms import Fb_model_form,Add_post_form,SignUpForm,CommentForm,comment_reply_form
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail

# from django.core.mail import EmailMessage
from fbproject.settings import EMAIL_HOST_USER
# Create your views here.
def login_view(request):
    username_signup=SignUp.objects.values_list('username',flat=True)
    password_signup=SignUp.objects.values_list('password1',flat=True)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username in username_signup and password in password_signup:
            print("login sucesss")
            # return redirect('dashboard')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("invalid username")
                # login(request, user)
                return redirect('signup')
            else:
                print("valid username")
                subject="Login successfully"
                message=" Fbapp application login successfully by"
            #     recipient_list=['srihari.n@cogentdatasolutions.in']
                # send_mail(subject,message,EMAIL_HOST_USER,recipient_list,fail_silently=False)
                # send_mail.send()
                return redirect('dashboard')
        else:
            return redirect('signup')
    else:
        fm = Fb_model_form()
    return render(request, 'login.html',{'form':fm})

# @login_required(login_url='/main/login/')
def dashboard(request):
    posts=Add_post.objects.all()
    # comments = Comment.objects.filter(addpost=post)
    # comments = Comment.objects.all()
    # post_comments = {}  # A dictionary to store comments for each post

    # for post in obj:
    #     comments = Comment.objects.filter(addpost=post)
    #     # print(comments)
    #     post_comments[post.id] = comments
    # print(post_comments)
    return render(request,"dashboard1.html",{'posts':posts})

def addpost(request):
    if request.method=="POST":
        fm=Add_post_form(request.POST ,request.FILES)
        if fm.is_valid():
            fm.save()
            fm=Add_post_form()
            return redirect('dashboard')
            # obj=Add_post.objects.all()
            # print(obj)
    else:
        fm=Add_post_form()
    return render(request,"addpost.html",{"form":fm})

def signup_view(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form1': fm})

    # return redirect('dashboard')

def logout_view(request):
    logout(request)
    return redirect('login_view')


# views.py

from django.shortcuts import get_object_or_404, render, redirect
from .models import Add_post

def add_comment(request, post_id):
    post = get_object_or_404(Add_post, pk=post_id)
    
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        post.add_comment = comment_text
        post.save()
    
    # else:
        # fm=CommentForm()

    return render('dashboard')


def post_comment(request, post_id):
    post = get_object_or_404(Add_post, pk=post_id)
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        
        print(comment_text)

        post.post_comment = comment_text
        post.save()

    return redirect('dashboard')  # Redirect to the dashboard after adding the comment



def post_details_comment(request, post_id):
    post = get_object_or_404(Comment, pk=post_id)
    
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        post.body = comment_text
        post.save()

    return redirect('dashboard')  



def allpost(request):
    obj=Add_post.objects.all()
    print(obj)
    return render(request, 'allpost.html',{'obj':obj})



def allpostdetail(request, post_id):
    post= get_object_or_404(Add_post, pk=post_id)
    # comments=Comment.objects.select_related('addpost').all()
    comments = Comment.objects.filter(addpost=post)
    print(comments)
    return render(request, 'post_detail.html', {'post':post,'comments':comments})



def addcommentinside(request, post_id):
    post = get_object_or_404(Add_post, pk=post_id)

    if request.method=='POST':
        fm = CommentForm(request.POST)
        if fm.is_valid():
            comment = fm.save(commit=False)
            comment.post = post  # Associate the comment with the specific post
            comment.save()
            return redirect('allpostdetail',post_id=post_id) 
    else:
        fm=CommentForm(initial={'addpost': post})
    return render(request,'commnetform.html',{'form':fm,'post':post})


def main_page_comment(request, post_id):
    post = get_object_or_404(Add_post, pk=post_id)
    if request.method == 'GET':
        # Get the button value from the submitted form
        post_id = request.GET.get('post_id')
        comment_text = request.GET.get('comment')
        comment=Comment()
        comment.addpost=post
        comment.name="srihari"
        comment.body=comment_text

        comment.save()

        return redirect('dashboard')
    
    return redirect('dashboard')

def main_page_reply(request, post_id):
    post = get_object_or_404(Comment, pk=post_id)
    if request.method == 'GET':
        # Get the button value from the submitted form
        post_id = request.GET.get('post_id')
        reply_text = request.GET.get('reply')
        reply=comment_reply()
        reply.comment=post
        reply.text=reply_text

        reply.save()

        return redirect('dashboard')
    
    return redirect('dashboard')


def comment_reply_view(request,id):
    post = get_object_or_404(Comment, pk=id)

    if request.method=="POST":
        fm=comment_reply_form(request.POST)
        if fm.is_valid():
            fm.save()
            fm=comment_reply_form()
            print("add post is successfully completed")
            # reply_data = get_object_or_404(comment_reply, pk=id)
            # reply_data = post.replies.all()
            # reply_data="welcome"
            # return render(request,"reply.html",{"reply_data":reply_data})
            # return redirect(all_post)
            replies = comment_reply.objects.filter(comment=post)
            return render(request,'reply.html',{"replies":replies})
    else:
        fm=comment_reply_form(initial={'comment':post})
    return render(request,"comment_reply.html",{"id":id,"form":fm})

def delete_comment(request,id):
    # return redirect("all_post")
    item = get_object_or_404(Comment, pk=id)
    print(item)
    item.delete()
    print("item is deleted")
    text="item is deleted"
    return render(request,"delete.html",{"id":id,"text":text})

def delete_reply(request,id):
    # return redirect("all_post")
    item = get_object_or_404(comment_reply, pk=id)
    print(item)
    item.delete()
    print("item is deleted")
    text="item is deleted"
    return render(request,"delete.html",{"id":id,"text":text})