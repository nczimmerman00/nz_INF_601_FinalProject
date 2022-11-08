from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import NewUserForm, SubmitHeadlineForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .models import Article
from transformers import pipeline

# AI content generator
from transformers import pipeline
generator = pipeline('text-generation', model ='EleutherAI/gpt-neo-125M')


# Create your views here.
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form":form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # Check if username and password match
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect(request.POST.get('next', 'home'))
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")


@login_required(login_url='/ai_news/login')
def submit_article(request):
    if request.method == "POST":
        form = SubmitHeadlineForm(request.POST)
        new_article = Article()
        if form.is_valid():
            new_article.article_title = form.cleaned_data.get('headline')
            new_article.article_category = form.cleaned_data.get('category')
            # Submit headline to AI model to write an article
            new_article.article_text = generator(new_article.article_title, max_length=750, do_sample=True, temperature=0.9)[0]['generated_text']
            new_article.article_slug = new_article.article_text[:50]
            if request.user.is_authenticated:
                new_article.article_author = request.user.username
            else:
                messages.error(request, "Error while submitting article!")
                new_article.article_author = 'Unknown_user'
            new_article.save()
            return redirect('home')
        else:
            messages.error(request, "Error while submitting article!")
    form = SubmitHeadlineForm()
    return render(request=request, template_name="submit.html", context={"submit_form": form})


def home_view(request):
    articles = Article.objects.all().order_by('-pub_date')
    return render(request=request, template_name="home.html", context={"articles": articles})
