from django.shortcuts import render,redirect
from django.contrib import messages
from .models import user

def index(req):
    return render(req, 'Semi_rest_User/index.html')


def create(req):    
    errors = user.objects.validate(req.POST)
    if errors:
       for error in errors:
           messages.error(req, error)
    
       return redirect("/index/")
    
    Users = user.objects.create_user(req.POST)
    req.session['user_id'] = Users.id   
    return redirect('/success/')


def success(req):
    context = {
        'users': user.objects.all()
    }
    return render(req, 'Semi_rest_User/success.html', context)

def update(req, id):
    if 'user_id' not in req.session:
        return redirect('/index')

    
    context ={
            'user': user.objects.get(id = id)
        }    
    return render(req, 'Semi_rest_User/update.html', context)


def show(req, id):
    if 'user_id' not in req.session:
        return redirect('/index')
   
    context ={
            'user': user.objects.get(id = id)
        }    
    return render(req, 'Semi_rest_User/show.html', context)

def delete(req, id):
    b = user.objects.get(id=id)
    b.delete()
    return redirect("/success")
