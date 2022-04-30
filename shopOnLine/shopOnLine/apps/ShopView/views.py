from django.http import Http404, HttpResponseRedirect, HttpResponse

from django.shortcuts import render

from django.urls import reverse

from .models import product


def index(request):
    lasted_products_list = product.objects.order_by('-pub_date')[:12]
    return render(request, 'ShopView/home.html',{'lasted_products_list': lasted_products_list})

def detail(request, product_id):
	try:
		a = product.objects.get(id = product_id)
	except:
		raise Http404("Статья не найдена!")
	latest_comment_list = a.comment_set.order_by('-id')[:10]

	return render(request, 'ShopView/ViewShop.html', {'product': a,'latest_comment_list':latest_comment_list})

def leave_comment(request, product_id):
	try:
		a = product.objects.get(id = product_id)
	except:
		raise Http404("Статья не найдена!")

	a.comment_set.create(avtor_name = request.POST['name'], comment_text = request.POST['text'], comment_text_positive = request.POST.get('textP', False), comment_text_negative = request.POST.get('textN', False))

	return HttpResponseRedirect(reverse('shopOnLine:detail', args =(a.id,)))