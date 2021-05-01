from django.shortcuts import render, redirect
from .models import Pizza, Topping, Comment
from .forms import CommentForm
from datetime import datetime, date

# Create your views here.
def index(request):
    """Home Page"""
    return render(request, "PizzeriaApp/index.html")


def pizzas(request):
    pizzas = Pizza.objects.order_by("name")

    context = {"pizzas": pizzas}

    return render(request, "PizzeriaApp/pizzas.html", context)


def pizza(request, name_id):
    pizza = Pizza.objects.get(id=name_id)
    toppings = pizza.topping_set.order_by("name")

    context = {"pizza": pizza, "toppings": toppings}

    return render(request, "PizzeriaApp/pizza.html", context)


def comments(request, name_id):
    if request.method == "GET" and request.GET.get("btn1"):
        comment = request.GET.get("comment")
        Comments.objects.create(
            pizza=name_id,
            text=comment,
            date_added=date.today(),
        )
    comments = Comment.objects.filter(pizza=name_id)
    pizza = Pizza.objects.get(id=name_id)

    context = {"pizza": pizza, "comments": comments}
    return render(request, "PizzeriaApp/comments.html", context)


def new_comment(request):
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_post.save()
            return redirect("PizzeriaApp:pizzas")

    context = {"form": form}
    return render(request, "PizzeriaApp/new_comment.html", context)
    