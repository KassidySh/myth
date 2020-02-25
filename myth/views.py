from django.shortcuts import render, redirect
from .models import Region, Type, Being, Story, FaveGod, FaveStory, Comment, God_Of, Author, User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import StoryForm, CommentForm, FaveGodForm, FaveStoryForm
from itertools import chain
# Create your views here.

def region_list(request):
    regions = Region.objects.all()
    return render(request, 'myth/region_list.html', {'regions': regions})

def type_list(request):
    types = Type.objects.all()
    return render(request, 'myth/type_list.html', {'types': types})

def single_region(request, pk):
    region = Region.objects.get(id=pk)
    return render(request, 'myth/single_region.html', {'region': region})

def single_type(request, pk):
    single = Type.objects.get(id=pk)
    return render(request, 'myth/single_type.html', {'single': single})

def single_being(request, pk):
    god = Being.objects.get(id=pk)
    return render(request, 'myth/single_being.html', {'god': god})


@login_required
def new_story(request,pk):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save()
            return redirect('single_being', pk=pk)
    else:
        form = StoryForm()
    return render(request, 'myth/new_story.html', {'form': form})

def edit_story(request, pk):
    story = Story.objects.get(pk=pk)
    if request.method == "POST":
        form=StoryForm(request.POST, instance=story)
        if form.is_valid():
            story = form.save()
            return redirect('single_being', pk=story.god.id)
    else:
        form= StoryForm(instance=story)
    return render(request, 'myth/new_story.html', {'form': form})

def delete_story(request, pk, god_pk):
    Story.objects.get(id=pk).delete()
    return redirect('single_being', pk=god_pk)

@login_required
def new_comment(request, pk, god_pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('single_being', pk=god_pk)
    else:
        form = CommentForm()
    return render(request, 'myth/new_comment.html', {'form': form})

def edit_comment(request, pk, god_pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == "POST":
        form=CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('single_being', pk=god_pk)
    else:
        form= CommentForm(instance=comment)
    return render(request, 'myth/new_comment.html', {'form': form})

def delete_comment(request, pk, god_pk):
    Comment.objects.get(id=pk).delete()
    return redirect('single_being', pk=god_pk)
    
def search_results(request):
    query = request.GET.get('q')
    if query:
        god = Being.objects.filter(title__icontains=query)
        key = God_Of.objects.filter(Q(item__icontains=query))
        results = chain(god, key)
    else:
        results = Being.objects.all()
    return render(request, 'myth/search_results.html', {'results': results})

@login_required
def user(request):
    author = Author.objects.all()
    return render(request, 'myth/user_page.html', {'author': author})

@login_required
def user_stories(request):
    stories = User.objects.all()
    return render(request, 'myth/user_stories.html', {'stories': stories})

# def fave_story(request, pk):

@login_required
def favorite_god(request, pk):
    if request.method == 'POST':
        form = FaveGodForm(request.Post)
        user = request.user
        god = pk
        FaveGod = form.save()
        return redirect('single_being', pk=pk)
    
@login_required
def favorite_story(request, pk, god_pk):
    if request.method == 'POST':
        form = FaveStoryForm(request.Post)
        user = request.user
        story = pk
        FaveStory = form.save()
        return redirect('single_being', pk=god_pk)
