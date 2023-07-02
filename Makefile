run:
	python3 cmd/main.py

black:
	black ../homestation/hs_app.py
	black ../homestation/config
	black ../homestation/internal

lint: black
	pylama ../homestation/hs_app.py
	pylama ../homestation/config
	pylama ../homestation/internal

mypy: black
	mypy ../homestation/hs_app.py
	mypy ../homestation/config
	mypy ../homestation/internal

deploy:
    ./deploy.sh
