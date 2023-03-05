from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Tag, Genre, Book
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import redirect

#melhorar, validar, selecionar os estados, formatar telefone etc etc

@login_required
def new_post(request):
    #if not request.user.is_authenticated:
    #    return HttpResponse("acesso negado")
    tags = Tag.objects.all()
    genres = Genre.objects.all()
    
    if request.method == "GET":
        return render(request, 'new_post.html', {'tags': tags, 'genres': genres})
    
    elif request.method == "POST":
        print(request.POST)
        form = [
            request.POST.get('name'),
            request.FILES.get('photo'),
            request.POST.get('description'),
            request.POST.get('state'),
            request.POST.get('city'),
            request.POST.get('telephone'),
            request.POST.getlist('tags'),
            request.POST.getlist('genres')
        ]
        print(form)
        if any([item == None for item in form]):
            messages.add_message(request, constants.ERROR, "Preencha todos os campos")
            return render(request, 'new_post.html', {'tags': tags, 'genres': genres})
        
        book = Book(
            user = request.user,
            name = form[0],
            photo = form[1],
            description = form[2],
            state = form[3],
            city = form[4],
            telephone = form[5]
        )

        book.save()

        for tag_id in form[6]:
            print(tag_id)
            tag = Tag.objects.get(id=tag_id)
    
            book.tags.add(tag)

        book.save()

        for genre_id in form[7]:
            genre = Genre.objects.get(id=genre_id)
    
            book.genres.add(genre)

        book.save()

        books = Book.objects.filter(user_id=request.user.id)
        messages.add_message(request, constants.SUCCESS, "Novo livro postado com sucesso")
        return render(request, 'your_posts.html', {'books': books})

@login_required
def your_posts(request):
    if request.method == "GET":
        books = Book.objects.filter(user_id=request.user.id)
        return render(request, 'your_posts.html', {'books': books})

def remove_book(request, id): 

    book = Book.objects.get(id=id)
    
    if request.user != book.user:
        messages.add_message(request, constants.ERROR, "Erro")
    else:
        book.delete()
        messages.add_message(request, constants.SUCCESS, "Livro removido com sucesso")
    
    return redirect('/posts/your_posts')

def show_book(request, id):
    
    if request.method == "GET":
        book = Book.objects.get(id = id)
        return render(request, 'show_book.html', {'book' : book})
