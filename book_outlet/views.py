from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.db.models import Avg

from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all().order_by("-rating")[:3]
    total_number_of_books = books.count()
    average_rating = books.aggregate(Avg("rating"))
    return render(
        request,
        "book_outlet/index.html",
        {
            "books": books,
            "total_number_of_books": total_number_of_books,
            "average_rating": average_rating,
        },
    )


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
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
