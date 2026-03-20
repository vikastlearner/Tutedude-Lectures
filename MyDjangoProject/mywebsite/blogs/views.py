from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Post
from .forms import CommentForm
from django.urls import reverse


# Create your views here.

def home_page(request):
    latest_blogs = Post.objects.all().order_by("-date")[:2]
    return render(request, "blogs/index.html", {"l_blog": latest_blogs})

def blogposts(request):
    blog_details = Post.objects.all()
    return render(request, "blogs/allposts.html", {"blogs_list": blog_details})

def process_blog_name(blog):
    blog_list = blog.split("-")
    return " ".join(blog_list).title()

def blog_post(request, blog):  # same "blog as used in path 'allposts/<blog>'"
    res = Post.objects.get(slug=blog)
    tag_caption = res.tag.all()
    all_comments = res.comments.all()

    if request.method == "POST":
        commented_data = request.POST
        form = CommentForm(commented_data)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = res
            comment.save()
            return HttpResponseRedirect(reverse("blog_post", args=[blog]))
        return render(request, "blogs/post.html", {"post": res,
                          "tag_caption": tag_caption, "comment_form": form, "comments": all_comments})
    else:
        try:
            form_data = CommentForm()
            return render(request, "blogs/post.html", {"post": res,
                      "tag_caption": tag_caption, "comment_form": form_data, "comments": all_comments})
        except Exception:
            raise Http404()