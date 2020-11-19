import json


# class Book:
#     def __init__(self, title, isbn, pageCount, publishedDate, thumbnailUrl, shortDescription, longDescription, status,
#                  authors, categories):
#         self.title = title
#         self.title = isbn
#         self.title = pageCount
#
#     @classmethod
#     def from_json(cls, jsonImport):
#         jsonL = json.loads(jsonImport)
#         return cls(**jsonL)

class Book:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    @classmethod
    def from_json(cls, json_import):
        le_json = json.loads(json_import)
        return cls(**le_json)
