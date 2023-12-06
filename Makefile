run:
	python3 app.py

black:
	black ../homestation/app.py
	black ../homestation/config
	black ../homestation/internal

lint: black
	pylama ../homestation/app.py
	pylama ../homestation/config
	pylama ../homestation/internal

mypy: black
	mypy ../homestation/app.py
	mypy ../homestation/config
	mypy ../homestation/internal

deploy:
	./deploy.sh
