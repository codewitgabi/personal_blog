from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import CommentForm
from django.core.paginator import Paginator
from django.db.models import Q


def index(request):
	q = request.GET.get("q") if request.GET.get("q") != None else ""
	all_posts = Post.objects.filter(
		Q(title__icontains= q) |
		Q(author__icontains= q),
		is_published= True,
	)
	recent_posts = Post.objects.filter(is_published= True)[:2]
	paginator = Paginator(all_posts, 6)
	page_number = request.GET.get("page")
	posts = paginator.get_page(page_number)
	
	context = {
		"posts": posts,
		"recent_posts": recent_posts
	}
	return render(request, "post/index.html", context)
	
	
def fullpost(request, slug):
	form = CommentForm()
	post = get_object_or_404(Post, slug= slug)
	recent_posts = Post.objects.filter(is_published= True)[:2]
	comments = Comment.objects.filter(post= post).order_by("?")[:3]
	
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			commenter = request.POST.get("commenter") if request.POST.get("commenter") != "" else "Anonymous"
			content = form.cleaned_data["content"]
			Comment.objects.create(
				post = post,
				commenter = commenter,
				content = content
			)
			
			return redirect("post", slug= post.slug)
	
	context = {
		"post": post,
		"comments": comments,
		"recent_posts": recent_posts,
		"form": form
	}
	return render(request, "post/post.html", context)
	

def add_subscriber(request):
	prev_page_url = request.META["HTTP_REFERER"]
	if request.method == "POST":
		email = request.POST.get("email")
		name = request.POST.get("first_name")
		Subscriber.objects.create(
			first_name= name,
			email= email
		)
	return redirect(prev_page_url)
	
	
def view_all_comments(request, slug):
	form = CommentForm()
	post = get_object_or_404(Post, slug= slug)
	recent_posts = Post.objects.filter(is_published= True)[:2]
	comments = Comment.objects.filter(post= post).order_by("?")
	page_name = "all"
	
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			commenter = request.POST.get("commenter") if request.POST.get("commenter") != "" else "Anonymous"
			content = form.cleaned_data["content"]
			Comment.objects.create(
				post = post,
				commenter = commenter,
				content = content
			)
			
			return redirect("post", slug= post.slug)
	
	context = {
		"post": post,
		"comments": comments,
		"recent_posts": recent_posts,
		"form": form,
		"page_name": page_name
	}
	return render(request, "post/post.html", context)