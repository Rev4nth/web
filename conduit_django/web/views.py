from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from .models import Article, Favourite
from .forms import ArticleForm

# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('user_feed')
    else:
        form = UserCreationForm()
        context = {
                'form': form,
                }
    return render(request, 'web/sign_up.html', context)


@login_required()
def global_feed(request):
    articles = Article.objects.all().order_by('-created_on')
    context = {
            'articles': articles,
            }
    return render(request, 'web/global_feed.html', context)


@login_required()
def user_feed(request):
    current_user = request.user
    user_articles = current_user.article_set.all().order_by('-created_on')
    context = {
            'user_articles': user_articles,
            }
    return render(request, 'web/user_feed.html', context)


@login_required()
def article_new(request):
    current_user = request.user
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            title = article_form.cleaned_data['title']
            about = article_form.cleaned_data['about']
            content = article_form.cleaned_data['content']
            current_user.article_set.create(title=title, about=about, content=content)
            return redirect('user_feed')
    else:
        article_form = ArticleForm()
    context = {
            'form': article_form,
            }
    return render(request, 'web/article_new.html', context)


@login_required()
def article_detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Question does not exist")

    context = {
            'article': article,
            }
    return render(request, 'web/article_detail.html', context)


@login_required()
def make_favourite(request, article_id):
    current_user = request.user
    article = Article.objects.get(id=article_id)
    if Favourite.objects.filter(article=article).filter(user=current_user).first():
        if Favourite.objects.filter(article=article).filter(user=current_user).first().is_favourite:
            Favourite.objects.filter(article=article).filter(user=current_user).update(is_favourite=False)
        else:
            Favourite.objects.filter(article=article).filter(user=current_user).update(is_favourite=True)
    else:
        f = Favourite.objects.create(article=article, user=current_user, is_favourite=True)
        f.save()

    return redirect('global_feed')
