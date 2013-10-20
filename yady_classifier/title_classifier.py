class TitleClassifier:
	def __init__(self, context = None):
		self.context = context

	def classify(self):
		self.context.tags.append('title-tag')
