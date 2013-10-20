from yady.classifier.web.classifier import Classifier
from yady.classifier.web.classifier import ClassificationContext

with open('links.txt') as fp:
    for line in fp:
    	context = ClassificationContext()
    	classifier = Classifier(context)
    	classifier.classify()
    	print context.tags