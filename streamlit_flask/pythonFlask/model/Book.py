class Book:
    def __init__(self, title, isbn, pageCount, publishedDate, thumbnailUrl, shortDescription, longDescription, status,
                 authors, categories):
        self.title = title
        self.isbn = isbn
        self.pageCount = pageCount
        self.publishedDate = publishedDate
        self.thumbnailUrl = thumbnailUrl
        self.shortDescription = shortDescription
        self.longDescription = longDescription
        self.status = status
        self.authors = authors
        self.categories = categories
