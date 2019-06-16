from django.shortcuts import render
from django.views.generic.base import TemplateView
from . models import Article
from django.views.generic.list 	 import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from . forms import ContactForm
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class Home(TemplateView):
	template_name = 'home/home.html'
	article = Article.objects.first_articles()
	
	def get_context_data(self, *args, **kwargs):
		context = super(Home, self).get_context_data(*args, **kwargs)		
		context["bck_image"] = 'images/index_hero.jpg'
		context["active_page"] = 'home'
		context["article"] = self.article
		return context
	

class Search(ListView):
	template_name = 'home/search.html'
	model = Article

	def get_queryset(self, *args, **kwargs):
		search_word = self.request.GET.get('search_word')
		

		
		if search_word:
			qs = super(Search, self).get_queryset(*args, **kwargs).filter(title__contains=search_word.lower())
			return qs
		else:
			qs = Article.objects.all()
			return qs

class Why(TemplateView):
	template_name = 'home/why.html'	
	
	def get_context_data(self, *args, **kwargs):
		context = super(Why, self).get_context_data(*args, **kwargs)		
		context["bck_image"] = 'images/about.jpg'
		context["active_page"] = 'why'
		return context


class How(TemplateView):
	template_name = 'home/how.html'	
	
	def get_context_data(self, *args, **kwargs):
		context = super(How, self).get_context_data(*args, **kwargs)		
		context["bck_image"] = 'images/howmain.jpg'
		context["active_page"] = 'how'
		return context

class Where(TemplateView):
	template_name = 'home/where.html'	
	
	def get_context_data(self, *args, **kwargs):
		context = super(Where, self).get_context_data(*args, **kwargs)		
		context["bck_image"] = 'images/wheremain.jpg'
		context["active_page"] = 'where'
		return context



class Howmuch(TemplateView):
	template_name = 'home/howmuch.html'	
	
	def get_context_data(self, *args, **kwargs):
		context = super(Howmuch, self).get_context_data(*args, **kwargs)		
		context["bck_image"] = 'images/howmuchmain.jpg'
		context["active_page"] = 'howmuch'
		return context
	
class Contact(FormView):
	template_name = 'home/contact.html'
	form_class = ContactForm
	success_url = 'contact'

	def get_context_data(self, *args, **kwargs):
		context = super(Contact, self).get_context_data(*args, **kwargs)		
		context["bck_image"] = 'images/contact.jpg'
		context["active_page"] = 'contact'
		return context
	
	def form_valid(self, form):
		name = form.cleaned_data['name']
		phone = form.cleaned_data['phone']
		email = form.cleaned_data['email']
		subject = form.cleaned_data['subject']
		message =form.cleaned_data['message']
		message = 'Name: ' + name + '\n' + 'Phone: ' + phone + '\n' + 'Email: ' + email + '\n' + message
		email_from = settings.EMAIL_HOST_USER
		recipient_list = ['losgatosrecoverycenter@gmail.com',]
		send_mail( subject, message, email_from, recipient_list )
		return super(Contact, self).form_valid(form)
        
		

	