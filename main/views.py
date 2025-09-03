from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406414542',
        'name': 'Karla Ameera Raswanda',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)