import json
from book import Book

class Library:

	@staticmethod
	def get():
		print('Retrieving Library Books...')
		with open('data/data.json', 'r') as data_file:
			data = json.load(data_file)
		return data

	@staticmethod
	def get_books():
		library_books = []
		data = Library.get()
		for item in data:
			library_books.append(Book(item['name'], item['read']))
		print(f'Total books found: {len(library_books)}')
		return library_books

	def get_book(self, request):
		print(f'Searching for library book: {request}')
		for book in self.books:
			if book.get_name().upper() == request.upper():
				print(f'Found book!')
				return book

	@staticmethod
	def update_book_read(request):
		books = Library.get_books()
		for library_book in books:
			if library_book.get_name().upper() == request.upper():
				print(f'Updating Book read: {request}')
				library_book.set_read()
		temp = []
		for book in books:
			temp.append(book.__dict__)
		with open('data/data.json', 'w') as data_file:
			json.dump(temp, data_file, indent=4)
