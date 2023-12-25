from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def test_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'test.html')