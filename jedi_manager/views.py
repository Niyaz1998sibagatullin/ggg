from django.shortcuts import render


def index(request):
    """
    Выводит на экран 2 кнопки: Для Джедаи, Для кандидата.
    """
    return render(request, "index.html")