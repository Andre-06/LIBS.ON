from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse
from posts.models import Book, Genre, User
from .models import PurchaseOrder
from datetime import datetime

def search_books(request):
    if request.method == "GET":
        books = Book.objects.filter(status='V')
        genres = Genre.objects.all
        
        genre = request.GET.get("genre")
        city = request.GET.get("city")

        if city:
            books = books.filter(city__icontains=city)
        if genre:
            books = books.filter(genres=genre)
            genre = int(genre)

        return render(request, 'search_books.html', {'books': books, 'genres': genres, 'selected_genre': genre, 'city':city})

def purchase_order(request, id):
    book = Book.objects.filter(id=id).filter(status='V')

    if not book.exists():
        messages.add_message(request, constants.ERROR, 'Esse livro já foi solicitado')
        return redirect('/purchase')

    po = PurchaseOrder(
        book = book.first(),
        user = request.user,
        data = datetime.now()
    )

    po.save()
    messages.add_message(request, constants.SUCCESS, 'Solicitação concluída')
    return redirect('/purchase')