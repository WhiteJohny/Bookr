def average_rating(rating_list: list) -> float:
    if not rating_list:
        return 0

    return round(sum(rating_list) / len(rating_list), 1)


def contributors_books(books: set, contributors_list: list) -> None:
    for contributor in contributors_list:
        for book in contributor.book_set.all():
            books.add(book)
