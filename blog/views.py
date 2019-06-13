from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from .models import Blog

from . import models
from django.contrib import messages
from .forms import SignUpForm, ContactForm
from django.views.generic import ListView, DetailView
from django.views import generic
from django.views import View
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

class Home(View): #class based home View
	def get(self, request):
		# data = Blog.objects.all().order_by('-id')
		# data1 = Category.objects.all()
		context = {
		'data' : Blog.objects.all().order_by('-id'),
		'data1' : models.Category.objects.all()
		}
		return render(request, 'home.html', context)
# class Cate(View):
# 	# template_name = base.html
# 	def get(self, request):	
def detail_category(request,id):
	category_detail = Blog.objects.filter(category_id=id)
	return render(request, 'detail_category.html', {'category_detail':category_detail})


def Category(request, category_slug):
	Categories = Category.objects.all()
	post = Post.objects.all()
	if category_slug:
		Category = get_object_or_404(Category, slug=category_slug)
		post = post.filter(category=category)
	context = {'categories':categories, 'post':post, 'category':category}	
	return render(request, 'category.html', context)

		# return render(request, 'home.html', {'data': data})

# class ArticleListView(ListView): #generic list view
	# template_name = 'home.html'
	# queryset = Blog.objects.all().order_by('-id')

def latest(request): #function based view
	latest = Blog.objects.all().order_by('id')[:3]
	return render(request, 'home.html', {'latest':latest})

# class Latest(View): #class based views latest
# 	def get(self, request, *args, **kwargs):
# 		return render(request, 'home.html', {'latest': latest})

def detail(request, id):
	detail_content = Blog.objects.get(id=id)
	if request.user.is_authenticated:
		return render(request, 'detail.html', {'data': detail_content})
	else:
		messages.success(request, "please login to access full article.")
		return redirect('login')

# class ArticleDetailView(DetailView):
# 	template_name = 'detail.html'
	

def list_categories(request):
	cate = Blog.ogjects.filter(category)
	return render(request, 'detail.html', {'data': cate})

# def register(request):
# 	if request.method == "POST":
# 		form = UserCreationForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			username = form.cleaned_data.get('username')
# 			messages.success(request, f"New account created: {username}")
# 			login(request, user)
# 			return redirect("/")
# 		else:
# 			for msg in form.error_messages:
# 				print(form.error_messages[msg])

# 			return render(request, 'register.html', {'form':form})
# 	form = UserCreationForm
# 	return render(request, 'register.html', {'form':form})

# def SignUp(request):
# 	if request.method == 'POST':
# 		form = SignUpForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			username = form.cleaned_data.get('username')
# 			raw_password = form.cleaned_data.get('password1')
# 			# user = authenticate(username=username, password=raw_password)
# 			# login(request, user)
# 			messages.success(request, "User registered successfully.")
# 			return redirect('login')
# 	else:
# 		form = SignUpForm()
# 	return render(request, 'register.html', {'form':form})

class SignUp(View):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			# return HttpResponseRedirect(self.request.path_info)
			return redirect("/")
		else:
			form = SignUpForm()
			hello = 'get request'
			return render(request, 'register.html', {'form':form, 'mess': hello })
	def post(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			# return HttpResponseRedirect(self.request.path_info)
			return redirect("/")
		else:
			form = SignUpForm(request.POST)
			print(request.POST)
			if form.is_valid():
				# hello = 'valid'
				# print('valid')
				form.save()
				# username = form.cleaned_data.get('username')
				# raw_password = form.cleaned_data.get('password1')
				# user = authenticate(username=username, password=raw_password)
				# login(request, user)
				return redirect('login')
			return render(request, 'register.html', {'form': form})

class ContactUs(View):
	def get(self, request, *args, **kwargs):
		form = ContactForm()
		return render(request, 'contact.html', {'form':form})
	def post(self, request, *args, **kwargs):
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Message submitted successfully")
			return redirect('contact')
		return render(reuqest, 'contact.html', {'form': form})


# class signup(FormView):
# 	form_class = SignUpForm
# 	# initial = {'key': 'value'}
# 	template_name = 'register.html'

# 	def form_valid(self, form):
# 		form.save()
# 		username = form.cleaned_data.get('username')
# 		raw_password = form.cleaned_data.get('password1')
# 		messages.success(request, "user registerd successfully")
# 		return redirect('login')

#----------------------------signup form------------------------
# class Signup(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     # messages.success("User registered successfully.")
#     template_name = 'register.html'
#----------------------------signup form------------------------

	# def get(self, request, *args, **kwargs):
	# 	form = self.form_class(initial=self.initial)
	# 	return re


	# 	nder(request, self.template_name, {'form': form})

	# def post(self, request, *args, **kwargs):
	# 	form = self.form_class(initial=self.initial)
	# 	if form.is_valid():
	# 		form.save()
	# 		username = form.cleaned_data.get('username')
	# 		raw_password = form.cleaned_data.get('password1')
	# 		messages.success(request, "User registered successfully.")
	# 		return redirect('login')
	# 	else:
	# 		form = SignUpForm()
	# 	return render(request, self.template_name, {'form':form})




# def login_request(request):
# 	form = AuthenticationForm()
# 	# return redirect('/')
# 	return render(request, 'login.html', {'form':form})
# def logout_request(request):
# 	logout(request)
# 	messages.info(request, "logged out Successfully!")
# 	return redirect('/')


#------------------------admin --------------------------------------------------------------------
