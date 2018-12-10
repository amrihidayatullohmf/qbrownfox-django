from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from home.models import Guestbook

def index(request):
    thumbnails = [
        'home/images/menus/01.jpg',
        'home/images/menus/02.jpg',
        'home/images/menus/03.jpg',
        'home/images/menus/04.jpg',
        'home/images/menus/05.jpg',
        'home/images/menus/06.jpg',
        'home/images/menus/07.jpg',
        'home/images/menus/08.jpg',
        'home/images/menus/09.jpg',
    ]

    menus = [
        {'name': 'Coffee', 'thumb': 'home/images/menus/01.jpg', 'desc': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum a magna non elit porta tincidunt et eget odio. '},
        {'name': 'Tea', 'thumb': 'home/images/menus/02.jpg', 'desc': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum a magna non elit porta tincidunt et eget odio. '},
        {'name': 'Bread', 'thumb': 'home/images/menus/03.jpg', 'desc': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum a magna non elit porta tincidunt et eget odio. '},
        {'name': 'Cake', 'thumb': 'home/images/menus/05.jpg', 'desc': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum a magna non elit porta tincidunt et eget odio. '},
    ]

    context = {
        'thumbs': thumbnails,
        'menus': menus
    }

    return render(request, 'home/index.html', context)

def guestbook(request):
    gname = request.POST['gname']
    gmail = request.POST['gmail']
    gphone = request.POST['gphone']

    if gname == '' or gmail == '':
        return JsonResponse({'code':500,'msg':'Please complete form bellow'})

    q = Guestbook(name=gname,email=gmail,phone=gphone,pub_date=timezone.now())
    q.save()

    return JsonResponse({'code':200,'msg':'Success'})
