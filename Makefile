init:
	pip install -r requirements.txt

test:
	nosetests tests --with-coverage --cover-erase --cover-branches --cover-package=FeatureFileProcessor --cover-html

watch_test:
	nosetests --with-watch