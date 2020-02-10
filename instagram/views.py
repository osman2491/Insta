from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse
from .models import Image
from .forms import PostForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    posts = Image.get_all()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = PostForm()

    try:
        posts = Image.objects.all()   
    except Image.DoesNotExist:
        posts = None

    return render(request, 'instagrm/index.html', { 'posts': posts, 'form': form })


def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profile = Image.search_by_profile(search_term)
        message = f"{search_term}"

        return render(request, 'instagrm/search.html',{"message":message,"profile": searched_profile})

    else:
        message = "You haven't searched for any term"
        return render(request, 'instagrm/search.html',{"message":message})
