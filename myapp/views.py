from django.shortcuts import render,redirect
from myapp.models import Post,Comment
from myapp.forms import CommentForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
# Create your views here.

def index(request):
	# process the request here
	p = Post.objects.all()
	context = {'posts':p}
	return render(request,'index.html',context)

'''def detail(request,pk):
	d = Post.objects.get(pk = pk)
	context = {'post':d}
	return render(request,'detail.html',context)'''

@login_required
def detail(request,pk):
    d = Post.objects.get(pk = pk)
    comments = Comment.objects.filter(post = d)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            comment = form.cleaned_data['comment']
            c = Comment(post = d,comment = comment,user = request.user)
            c.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            context = {'post':d,'form':form,'comments':comments}
            return render(request, 'detail.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CommentForm()
    context = {'post':d,'form':form,'comments':comments}
    return render(request, 'detail.html', context)

class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','description','image']
    success_url = '/'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def like(request):
    if request.is_ajax():
        i = (request.GET.get('i'))
        p = Post.objects.get(pk=i)
        p.likes += 1
        p.save()
        data = {'i':p.likes}
        return JsonResponse(data)

def books(request):
    return render(request,'books.html')