from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.core.mail import send_mail
from .forms import MyForm
from .models import Post
from django import forms

def index(request):
	posts = Post.objects.filter(date_pub__lte=timezone.now()).order_by('date_pub')
	context = {'posts':posts}
	return render(request, 'generalapp/index.html', context)

def show_post(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	context = {'post':post}
	return render(request, 'generalapp/show_post.html', context)

def post_add(request):
	if request.method == 'POST':
		form = MyForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.date_pub = timezone.now()
			post.save()
			send_mail('Заявка', 'Заявка', 'aramas36@yandex.ru', ['aramas37@yandex.ru'])
			return redirect('/')
	else:
		form = MyForm()
	return render(request, 'generalapp/form.html', {'form':form})


