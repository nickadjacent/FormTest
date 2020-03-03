from django.shortcuts import render, redirect


def index(request):
    return render(request, "index.html")


def create_user(request):
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    context = {
        "name_on_template": name_from_form,
        "email_on_template": email_from_form
    }
    return redirect("/success")


def success(request):
    return render(request, 'success.html')


def some_function(request):
    request.session['name'] = request.POST['name']
    request.sessions['counter'] = 100
