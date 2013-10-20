import yady.utils

classifiers = ['TitleClassifier','DomainClassifier']

class ClassificationContext:
	contentTokens = []
	titleTokens = []
	link = ""
	title = ""
	domain = ""
	tags = []

class Classifier:
	def __init__(self,classification_context=None):
		self.context = classification_context

	def classify(self):
		for classifier_name in classifiers:
			c = yady.utils.class_for_name('yady.classifier.web.%s' % (classifier_name.lower()),classifier_name)
			classifier = c(self.context)
			classifier.classify()