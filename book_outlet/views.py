from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {"books": books})


def book_detail(request, book_id):
    # try:
    #     book = Book.objects.get(pk=book_id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, pk=book_id)
    return render(
        request,
        "book_outlet/book_detail.html",
        {
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "is_bestselling": book.is_bestselling,
        },
    )
