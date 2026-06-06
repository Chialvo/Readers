import requests
from django.conf import settings

GOOGLE_BOOKS_URL = "https://www.googleapis.com/books/v1/volumes"

def search_books(query):
    response = requests.get(GOOGLE_BOOKS_URL, params={
        "q": query,
        "maxResults": 12,
        "key": settings.GOOGLE_BOOKS_API_KEY
    })
    data = response.json()
    books = []
    for item in data.get("items", []):
        info = item.get("volumeInfo", {})
        books.append({
            "google_books_id": item["id"],
            "title":       info.get("title", "Sin título"),
            "author":      ", ".join(info.get("authors", ["Desconocido"])),
            "cover_url":   info.get("imageLinks", {}).get("thumbnail", ""),
            "pages":       info.get("pageCount"),
            "published":   info.get("publishedDate", "")[:4],
            "description": info.get("description", ""),
        })
    return books

def get_book_detail(google_books_id):
    response = requests.get(f"{GOOGLE_BOOKS_URL}/{google_books_id}", params={
        "key": settings.GOOGLE_BOOKS_API_KEY
    })
    item = response.json()
    info = item.get("volumeInfo", {})
    return {
        "google_books_id": google_books_id,
        "title":       info.get("title", "Sin título"),
        "author":      ", ".join(info.get("authors", ["Desconocido"])),
        "cover_url":   info.get("imageLinks", {}).get("thumbnail", ""),
        "pages":       info.get("pageCount"),
        "published":   info.get("publishedDate", "")[:4],
        "description": info.get("description", ""),
    }