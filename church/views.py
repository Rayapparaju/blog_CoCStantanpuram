from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Sermon, Book, Song, GalleryImage
from .forms import ContactForm, RegisterForm


def home(request):
    posts = BlogPost.objects.filter(is_published=True)[:3]
    sermons = Sermon.objects.filter(is_published=True)[:3]
    gallery = GalleryImage.objects.filter(is_published=True)[:6]
    return render(request, 'church/index.html', {
        'posts': posts,
        'sermons': sermons,
        'gallery': gallery,
    })


def post_list(request):
    queryset = BlogPost.objects.filter(is_published=True)
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(author__icontains=query)
        )
    category = request.GET.get('category')
    if category:
        queryset = queryset.filter(category=category)
    paginator = Paginator(queryset, 9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'church/post_list.html', {
        'posts': posts,
        'categories': BlogPost.CATEGORY_CHOICES,
    })


def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    return render(request, 'church/post_detail.html', {'post': post})


def sermon_list(request):
    queryset = Sermon.objects.filter(is_published=True)
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) | Q(preacher_name__icontains=query) | Q(description__icontains=query)
        )
    paginator = Paginator(queryset, 9)
    page = request.GET.get('page')
    sermons = paginator.get_page(page)
    return render(request, 'church/sermon_list.html', {'sermons': sermons})


def book_list(request):
    queryset = Book.objects.filter(is_published=True)
    paginator = Paginator(queryset, 12)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    return render(request, 'church/book_list.html', {'books': books})


def song_list(request):
    queryset = Song.objects.filter(is_published=True)
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(Q(title__icontains=query) | Q(lyrics__icontains=query))
    paginator = Paginator(queryset, 12)
    page = request.GET.get('page')
    songs = paginator.get_page(page)
    return render(request, 'church/song_list.html', {'songs': songs})


def gallery_list(request):
    queryset = GalleryImage.objects.filter(is_published=True)
    paginator = Paginator(queryset, 12)
    page = request.GET.get('page')
    images = paginator.get_page(page)
    return render(request, 'church/gallery_list.html', {'images': images})


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            form = ContactForm()
    return render(request, 'church/contact.html', {'form': form})


def search(request):
    query = request.GET.get('q', '')
    posts = BlogPost.objects.filter(is_published=True, title__icontains=query)
    sermons = Sermon.objects.filter(is_published=True, title__icontains=query)
    return render(request, 'church/search_results.html', {
        'query': query,
        'posts': posts,
        'sermons': sermons,
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'church/login.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}! Registration successful.')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'church/register.html', {'form': form})


def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')
