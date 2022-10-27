from django.shortcuts import HttpResponseRedirect, redirect, render
from django.urls import reverse
from .forms import UserForm, NewTodoForm
from django.contrib.auth import authenticate, login, logout
from .models import User, Todo
import json

# Create your views here.

def get_current_user(request):
    current_user_obj= User.objects.filter(username=request.session["user"])
    for current_user in current_user_obj:
        current_user = current_user

    return current_user


def index(request, auth=False):
    if 'user' not in request.session:
        return render(request, "todo/index.html")
    
    # current_user_obj= User.objects.filter(username=request.session["user"])
    # for current_user in current_user_obj:
    #     current_user = current_user

    current_user = get_current_user(request)

    todos_completed = Todo.objects.filter(user=current_user, completed=True)
    todos_not_completed = Todo.objects.filter(user=current_user, completed=False)

    return render(request, "todo/index.html", {
        "todos_completed": todos_completed,
        "todos_not_completed": todos_not_completed,
        "form": NewTodoForm(),
        "current_user": current_user,
    })


def signup_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        print("form is post")
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("todo:login"))
    else:
        form = UserForm()

    return render(request, "todo/signup.html", {
        "form": form,
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        check_user = User.objects.filter(username=username, password=password)
            
        if check_user:
            request.session["user"] = username
            return HttpResponseRedirect(reverse("todo:home"))
        else:
            return render(request, "todo/login.html", {
                "message": "Invalid credentials",
                })


    return render(request, "todo/login.html")

def logout_view(request):
    try:
        del request.session['user']
    except:
        return redirect('todo:login')

    return redirect('todo:home')


def profile_view(request):
    if "user" in request.session:
        
        current_user = get_current_user(request)

        return render(request, "todo/profile.html", {
            "current_user": current_user,
        })
    
    return HttpResponseRedirect(reverse("todo:home"))


def add(request,):
    if request.method == "POST":
        form = NewTodoForm(request.POST)
        
        current_user = get_current_user(request)

        if form.is_valid():
            todo = form.cleaned_data["text"]

            newtodo = Todo(text=todo, completed=False, user=current_user)
            newtodo.save()

            return HttpResponseRedirect(reverse("todo:home"))

        else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "todo/index.html", {
                "form": form
            })
    
    return render(request, "todo/index.html", {
        "form": NewTodoForm()
    })

def check(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo:home')

def uncheck(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = False
    todo.save()
    return redirect('todo:home')

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo:home')