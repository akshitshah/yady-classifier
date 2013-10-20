from yady_classifier.classifier import Classifier
from yady_classifier.classifier import ClassificationContext

with open('tests/links.txt') as fp:
    for line in fp:
    	context = ClassificationContext()
    	classifier = Classifier(context)
    	classifier.classify()
    	print context.tags