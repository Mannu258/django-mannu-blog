from django.shortcuts import render
from blog.models import Post,Category
from django.views.generic import CreateView

# Create your views here.
def home(request):
    cats = Category.objects.all()
    post = Post.objects.all()[:10]
    data = {
        'cats':cats,
        'post':post
    }
    return render(request,'blog/home.html',data)


def post(request,url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    return render(request,'blog/post.html',{'post':post,'cats':cats})

def category(request,url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request,'blog/category.html',{'cat':cat,'posts':posts})

class createpost(CreateView):
    model = Post
    fields = ('__all__')
    success_url = ('/')
    template_name = 'blog/create_post.html'