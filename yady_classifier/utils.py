import importlib


def class_for_class_name(class_name):
	file_name = class_name
	modified_class_name = ''.join(x.capitalize() or '_' for x in file_name.split('_'))
	return class_for_name('yady_classifier.%s' % (file_name.lower()), modified_class_name)


def class_for_name(module_name, class_name):
	# load the module, will raise ImportError if module cannot be loaded
	m = importlib.import_module(module_name)
	# get the class, will raise AttributeError if class cannot be found
	c = getattr(m, class_name)
	return c