from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest


def number_view(request: HttpRequest, n:int) -> HttpResponse:
    def near_hundred(n):
        return abs(100 - n) <= 10 or abs(200 - n) <= 10
    return HttpResponse(near_hundred(n))


def string_splosion_view(request: HttpRequest, word:str) -> HttpResponse:
    result = ""
    for words in range(len(word)):
        result += word[: words + 1]
    return HttpResponse(result)


def cat_dog_view(request: HttpRequest, animal:str) -> HttpResponse:
    count_cat = animal.count("cat")
    count_dog = animal.count("dog")
    if count_cat == count_dog:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def lone_sum_view(request: HttpRequest, a:int, b:int, c:int) -> HttpResponse:
    if a == b == c:
        return HttpResponse(0)
    elif a == b:
        return HttpResponse(c)
    elif b == c:
        return HttpResponse(a)
    elif c == a:
        return HttpResponse(b)
    elif a != b != c:
        return HttpResponse(a + b + c)
