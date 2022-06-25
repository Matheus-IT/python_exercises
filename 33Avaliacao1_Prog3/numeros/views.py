from random import randint
from django.shortcuts import render
from numeros.forms import FormNum

# Using in-memory storage
chosen_number = None  # Number to be guessed, will be assigned when game starts
num_chances = None


def choose_random_number():
    return randint(1, 100)


def start_game_view(request):
    global chosen_number, num_chances

    chosen_number = choose_random_number()
    num_chances = 5
    form = FormNum(None)

    return render(request, 'escolha.html', {'form': form})


def tentativa_view(request):
    global chosen_number, num_chances

    form = FormNum(request.POST)
    if form.is_valid():
        num = form.cleaned_data['num']

        player_win = True if num == chosen_number else False

        if player_win is False:
            num_chances -= 1

        return render(
            request,
            'result.html',
            {
                'player_win': player_win,
                'num': num,
                'form': form,
                'chosen_number': chosen_number,
                'num_chances': num_chances,
            },
        )
    else:
        return render(
            request,
            'result.html',
            {
                'player_win': False,
                'num': None,
                'form': form,
                'chosen_number': chosen_number,
                'num_chances': num_chances,
            },
        )
