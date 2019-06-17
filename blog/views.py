from django.shortcuts import render
from django.utils import timezone
from.models import Post

def post_list(request):
	posts=Post.objects.all()
	print(posts)
	return render(request,'blog/post_list.html', {'posts':posts})

def portfolio(request):
	return render(request, 'index3.html')

def main(request):
	return render(request, 'index1-1.html')

def packets(request):
	return render(request,'index2.html')

def portfolio(request):
	return render(request,'index3.html')
def contacts(request):
	return render(request,'index4.html')
def otzyvi(request):
	return render(request,'index5.html')
