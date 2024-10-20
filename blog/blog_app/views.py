from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Max

from .models import Entries
from .forms import CustomUserCreationForm, AddEntryForm


# Create your views here.


def register_view(request):     # registration
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, "blog_app/register.html", {
        'form': form
    })


def login_view(request):
    if request.method == "POST":
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            login(request, login_form.get_user())
            return redirect('home')
    else:
        login_form = AuthenticationForm()
    return render(request, "blog_app/login.html", {
        'login_form': login_form
    })


def logout_view(request):
    logout(request)
    return redirect('home')


def index(request):
    entries = Entries.objects.all()
    return render(request, 'blog_app/index.html', {
        'entries': entries
    })


@login_required(login_url="login")
def add_entry_view(request):
    if request.method == "POST":
        add_entry_form = AddEntryForm(data=request.POST)
        if add_entry_form.is_valid():
            entry = add_entry_form.save(commit=False)
            max_slug = Entries.objects.aggregate(Max('slug'))['slug__max']
            if max_slug is None:
                max_slug = 0
            entry.slug = int(max_slug) + 1
            entry.user = request.user
            entry.save()
            return redirect('home')
    else:
        add_entry_form = AddEntryForm()

    return render(request, "blog_app/add-entry.html", {
        'add_entry_form': add_entry_form
    })


@login_required
def update_entry(request, slug):
    entry = get_object_or_404(Entries, slug=slug, user=request.user)
    if request.method == "POST":
        form = AddEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddEntryForm(instance=entry)

    return render(request, 'blog_app/update-entry.html', {
        'form': form
    })
