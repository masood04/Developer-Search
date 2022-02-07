from .models import Profile, Skill
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def paginate_profiles(request, profiles, results):
    
    page = request.GET.get('page')
    paginator = Paginator(profiles, results)
    
    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)
        
    left_idx = (int(page) - 4)
    if left_idx < 1:
        left_idx = 1
    
    right_idx = (int(page)+ 5)
    if right_idx > paginator.num_pages:
        right_idx = paginator.num_pages + 1

    custom_range = range(left_idx, right_idx)    
    
    
    return custom_range, profiles


def search_profiles(request):
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query =  request.GET.get('search_query')
        
    skill = Skill.objects.filter(name__icontains=search_query)
    
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) | 
        Q(short_intro__icontains=search_query) |
        Q(skill__in=skill)
        )
    return profiles, search_query