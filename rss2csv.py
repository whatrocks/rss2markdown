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
    # parse the feed
    print(book)
    # filename = f'{title}-{book["author_name"]}.md'
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
    

    # TODO: determine if we should skip it or not based on if we have the file or not
    # since we don't want to overwrite existing things
    
    # save the cover art
    # r = requests.get(img_url, stream=True)
    # if r.status_code == 200:
    #     r.raw.decode_content = True
    #     with open(f'{ROOT_DIR}{ASSETS_DIR}/Books/{title}.jpg', 'wb') as img:
    #         shutil.copyfileobj(r.raw, img)
    
    # # write our markdown file
    # with open(f'{ROOT_DIR}{BOOKS_DIR}/{filename}', 'w') as f:
    #     short_name = f'{title}.jpg'
    #     review = book["user_review"]
    #     if review == None:
    #         review = ""
    #     f.write(f'# {title}\n## {book["author_name"]}\n\n{book["user_review"]}\n\n![[{short_name}]]')
    #     f.close()

# print("now fetching blog posts...")

# BLOG_RSS_URL="https://www.charlieharrington.com/rss.xml"
# BLOG_DIR="/Blog"

# maybe i should just get this directly from the other directory when i publish things
# make a script to do this.

# posts = json.loads(json.dumps(xmltodict.parse(requests.get(BLOG_RSS_URL).text)))
# for post in posts["rss"]["channel"]["item"]:
#     # parse the feed
#     title = post["title"].split(' (', 1)[0]
#     filename = f'{title}.md'
#     # write our markdown file
#     with open(f'{ROOT_DIR}{BLOG_DIR}/{filename}', 'w') as f:
#         f.write(f'# {title}\n\n{post["content:encoded"]}\n')
#         f.close()

print("DONE!")
