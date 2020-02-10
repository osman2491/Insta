from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse
from .models import Image,Profile
from .forms import PostForm
from django.contrib.auth.models import User
from .forms import *
from .models import *

# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    posts = Image.get_all()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.image_profile = request.user.profile
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

@login_required(login_url='login')
def profile(request):
    current_user = request.user
    profile = Profile.objects.all()

    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST,instance=request.user)
        p_form = UpdateUserProfileForm(request.POST, request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
            return render(request,'registration/profile.html')
    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = UpdateUserProfileForm(instance=request.user.profile)


    context = {
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request, 'registration/profile.html',locals())
