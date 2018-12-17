init:
	pip3 install -r requirements.txt

test:
	nosetests tests --exe --with-coverage --cover-erase --cover-branches --cover-package=FeatureFileProcessor --cover-html

watch_test:
	nosetests --with-watch