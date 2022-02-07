from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Project, Tag
from .utils import search_project, paginate_projects
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm, ReviewForm


def projects(request):
  
    projects, search_query = search_project(request)
    
    custom_range, projects = paginate_projects(request, projects, results=6)
 
    
    context =  {
                'projects':projects,
                'search_query':search_query,
                'custom_range':custom_range 
                }
    
    return render(request, 'projects/projects.html', context)

def project(request, pk):
  projectObj = Project.objects.get(id=pk)
  tags = projectObj.tags.all()
  form = ReviewForm()
  
  if request.method == "POST":
    form = ReviewForm(request.POST)
    review = form.save(commit=False)
    review.project = projectObj
    review.owner = request.user.profile
    review.save()
    
    projectObj.get_vote_count
    
    
    messages.success(request, 'Your review sumbited sucs')
    return redirect('project', pk=projectObj.id)
    
    
  return render(request, 'projects/single-project.html', {'project':projectObj, 'tags':tags, 'form':form, 'reviewers':projectObj.reviewers})

@login_required(login_url='login')
def create_project(request):
    
    profile = request.user.profile
    form = ProjectForm()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')
    
    context = {'form':form}
    
    return render(request, 'projects/projects_form.html', context)

@login_required(login_url='login')
def update_project(request, pk):
    profile = request.user.profile
    
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        
        if form.is_valid():
            
            form.save()
            return redirect('account')
    
    context = {'form':form}
    
    return render(request, 'projects/projects_form.html', context)

@login_required(login_url='login')
def delete_project(request, pk):
    profile = request.user.profile
    
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('account')
    context = {'object':project}
    return render(request, 'delete_template.html', context)


