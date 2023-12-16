from django.shortcuts import render, get_object_or_404

from reviews.models import Book, Contributor
from reviews.utils import average_rating, contributors_books
from reviews.forms import SearchForm


def index(request):
    return render(request, "base.html")


def book_search(request):
    search_text = request.GET.get("search", "")
    form = SearchForm(request.GET)
    books = set()

    if form.is_valid() and form.cleaned_data["search"]:
        search = form.cleaned_data["search"]
        search_in = form.cleaned_data.get("search_in") or "title"
        if search_in == "title":
            books = Book.objects.filter(title__icontains=search)
        else:
            first_names_contributors = Contributor.objects.filter(first_names__icontains=search)
            contributors_books(books, first_names_contributors)

            last_names_contributors = Contributor.objects.filter(last_names__icontains=search)
            contributors_books(books, last_names_contributors)

    return render(
        request,
        "reviews/search-results.html",
        {"form": form, "search_text": search_text, "books": books}
    )


def books_list(request):
    books = Book.objects.all()
    books_list = []

    for book in books:
        reviews = book.review_set.all()

        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0

        books_list.append({'book': book,
                           'book_rating': book_rating,
                           'number_of_reviews': number_of_reviews})

    context = {
        'books_list': books_list
    }

    return render(request, 'reviews/books_list.html', context)


def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.review_set.all()

    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
    else:
        book_rating = None

    context = {
        'book': book,
        'reviews': reviews,
        'book_rating': book_rating
    }

    return render(request, 'reviews/book_details.html', context)
