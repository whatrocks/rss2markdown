import json
import requests
import xmltodict
import csv
import shutil

print("BEGIN running rss2markdown script...")

print("fetching goodreads reviews...")

GOODREADS_RSS_URL="https://www.goodreads.com/review/list_rss/8699203?key=zzjLCDUHgkQ9dLi7quJIqTW3cbvSjI2QdHOuwhnUZr0_hYFl&shelf=2021"
ROOT_DIR="/Users/ch"
BOOKS_DIR="/projects/rss2markdown"
ASSETS_DIR="/Assets"

books = json.loads(json.dumps(xmltodict.parse(requests.get(GOODREADS_RSS_URL).text)))

lines = []
writer = csv.writer(open(f'{ROOT_DIR}{BOOKS_DIR}/2021.csv', 'w'))
for book in books["rss"]["channel"]["item"]:
    # print(book)
    isbn = book['isbn']
    if isbn == None:
        isbn = ""
    cover_img_url = book["book_large_image_url"]
    if cover_img_url == None:
        cover_img_url = ""
    title = book["title"].split(' (', 1)[0]
    if title == None:
        title = ""
    author_name = book['author_name']
    if author_name == None:
        author_name = ""
    read_at = book["user_read_at"]
    if read_at == None:
        read_at = ""
    published_at = book["book_published"]
    if published_at == None:
        published_at = ""
    review = book["user_review"]
    if review == None:
        review = ""
    review_link = book["link"]
    if review_link == None:
        review_link = ""

    writer.writerow([isbn, cover_img_url, title, author_name, read_at, published_at, review, review_link])

print("DONE!")
