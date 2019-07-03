from django.shortcuts import render
from .forms import CommentForm


def index(request):
    return render(request, "shop/product/index.html", {})


def contact(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.save()
    form = CommentForm()
    return render(request, "shop/product/contact.html", {'form': form})
