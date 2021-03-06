from django.http import Http404, HttpResponseRedirect

from django.shortcuts import render

from django.urls import reverse

from .models import Article

def index(request):
	lasted_articles_list = Article.objects.order_by('-pup_date')[:5]
	return render(request, 'artivles/list.html',{'lasted_articles_list': lasted_articles_list})

def detail(request, article_id):
	try:
		a = Article.objects.get(id = article_id)
	except:
		raise Http404("Статья не найдена!")

	latest_comment_list = a.comment_set.order_by('-id')[:10]

	return render(request, 'artivles/detail.html', {'article': a,'latest_comment_list':latest_comment_list})

def leave_comment(request, article_id):
	try:
		a = Article.objects.get(id = article_id)
	except:
		raise Http404("Статья не найдена!")

	a.comment_set.create(Avtor_name = request.POST['name'], comment_text = request.POST['text'])

	return HttpResponseRedirect(reverse('artivles:detail', args =(a.id,)))