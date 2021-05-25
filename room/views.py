from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render
from room.models import Room
from django.views import View
from django.db.models import Count



def main_page(request):
    query_set = Room.objects.all().annotate(count_likes=Count('likes'))
    context = {'query_set': query_set}
    return render(request, 'hotel/index.html', context=context)


def room_detail(request, room_id):
    room = Room.objects.get(id=room_id)
    context = {'room': room}
    return render(request, 'hotel/room_detail.html', context=context)


@login_required()
def room_like(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.user in room.likes.all():
        room.likes.remove(request.user)
    else:
        room.likes.add(request.user)
    return redirect('main_page')


class LoginView(View):
    def get(self, request):
        return render(request, 'hotel/login.html')

    def post(self, request):
        user = authenticate(username = request.POST['login'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('main_page')
        return redirect('login')

# def login_view(request):
#     return render(request, 'hotel/login.html')


def logout_view(request):
    logout(request)
    return redirect('main_page')
