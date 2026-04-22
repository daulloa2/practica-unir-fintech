.PHONY: all $(MAKECMDGOALS)

run:
	docker run --rm --volume `pwd`:/opt/app --env PYTHON_PATH=/opt/app -w /opt/app python:3.6-slim python3 main.py words.txt yes

run-local:
	PYTHON_PATH=`pwd` python3 main.py words.txt yes