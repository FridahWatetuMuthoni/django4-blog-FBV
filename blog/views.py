from django.shortcuts import get_object_or_404, render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def post_list(request):
    posts_list = Post.published.all()
    paginator = Paginator(posts_list, 5)
    #get the page number and if its not provided we use 1
    page_number = request.GET.get('page',1)
    
    try:
        posts = paginator.page(page_number)

    except PageNotAnInteger:
         # If page_number is not an integer deliver the first page
         posts = paginator.page(1)

    except EmptyPage:
         # If page_number is out of range deliver last page of results
          posts = paginator.page(paginator.num_pages)
    
    context = {
        'posts':posts
    }
    return render(request, 'blog/post/list.html', context)

"""
We have modified the post_detail view to take the year, month, day, and post arguments 
and retrieve a published post with the given slug and publication date. 
By adding unique_for_date='publish' to the slug field of the Post model before, 
we ensured that there will be only one post with a slug for a given date. 
Thus, you can retrieve single posts using the date and slug.
we are using slug = post beacause post returns the title as a string from the __str__
method.
Basically we want the post that is published, has a specific slug and published date
"""

def post_detail(request,year, month, day, post):
    post = get_object_or_404(Post, status = Post.Status.PUBLISHED,
                             slug=post,
                             publish__year = year,
                             publish__month = month,
                             publish__day = day
                             )
    
    context = {
        'post':post
    }
    return render(request, 'blog/post/detail.html', context)