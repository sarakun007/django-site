from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member, Pictures
from django.shortcuts import render
from django.core.paginator import Paginator
from .csgotm_parser import kn_pr


def members(request):
    mymembers = Member.objects.all()
    template = loader.get_template('all_members.html')

    paginator = Paginator(mymembers, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'mymembers': mymembers,
        "page_obj": page_obj
    }

    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    myphoto = Member.objects.all()
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
        'myphoto': myphoto,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    nau_info = Member.objects.all()
    phot = Pictures.objects.all()
    template = loader.get_template('main.html')
    context = {
        'nau': nau_info,
        'phot': phot,

    }
    return HttpResponse(template.render(context, request))


def testing(request):
    mydata = Member.objects.all()
    template = loader.get_template('template.html')
    context = {
        'mydata': mydata
    }
    return HttpResponse(template.render(context, request))


def mypage(request):
    template = loader.get_template('mypage.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def item_price(request):
    template = loader.get_template('price.html')
    context = {
        'kn_pr': kn_pr

    }
    return HttpResponse(template.render(context, request))
