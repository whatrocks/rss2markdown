import json
import requests
import xmltodict

print("fetching goodreads reviews...")

GOODREADS_RSS_URL="https://www.goodreads.com/review/list_rss/8699203?key=zzjLCDUHgkQ9dLi7quJIqTW3cbvSjI2QdHOuwhnUZr0_hYFl&shelf=read"
BOOKS_DIR="Books"
books = json.loads(json.dumps(xmltodict.parse(requests.get(GOODREADS_RSS_URL).text)))
for book in books["rss"]["channel"]["item"]:
    title = book["title"].split(' (', 1)[0]
    filename = f'{title}-{book["author_name"]}.md'
    image = book["book_large_image_url"]
    with open(f'{BOOKS_DIR}/{filename}', 'w') as f:
        f.write(f'# {title}\n## {book["author_name"]}\n{book["user_review"]}\n')
        f.close()

print("now fetching blog posts...")

BLOG_RSS_URL="foo"
BLOG_DIR="Blog"

print("done!")
