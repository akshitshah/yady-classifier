import yady_classifier.utils


classifiers = ['title_classifier', 'domain_classifier']


class ClassificationContext:
	contentTokens = []
	titleTokens = []
	link = ""
	title = ""
	domain = ""
	tags = []


class Classifier:
	def __init__(self, classification_context = None):
		self.context = classification_context

	def classify(self):
		for classifier_name in classifiers:
			c = yady_classifier.utils.class_for_class_name(classifier_name)
			classifier = c(self.context)
			classifier.classify()