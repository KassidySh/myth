from django.shortcuts import render, redirect
from .models import Region, Type, Being, Story, FaveGod, FaveStory, Comment
from django.contrib.auth.decorators import login_required
from .forms import StoryForm, CommentForm
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

# def new_fave_story(request, pk):
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
