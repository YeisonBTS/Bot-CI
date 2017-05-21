class User():
	def __init__(self, database, collection):
		self.database = database
		self.collection_name = collection_name
		self.collection = database[self.collection_name]

	def save(self, document):
		self.collection.save(document)