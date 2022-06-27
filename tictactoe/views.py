from django.http import HttpResponse
from .models import Games
from .models import Moves
from .models import Users


def index(request):
    game_list = Games.objects.order_by('-ended_on')[:5]
    output = ', '.join([g.id for g in game_list])

    return HttpResponse(output)


def user(request, username):
    return HttpResponse('Found user %s' % username)


def game(request, game_id):
    moves_list = Moves.objects.filter(game_id=game_id).order_by('-moved_on')
    moves_list_length = moves_list.__len__()
    return HttpResponse('Game ID %d found has %d moves.' % (game_id, moves_list_length))
