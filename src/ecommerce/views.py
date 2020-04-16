from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model

from .forms import ContactForm

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    context  = {
        "title": "Contact Us",
        "content": "Welcome to contact page",
        "form": contact_form,
    }
    return render(request, 'contact/view.html', context)

