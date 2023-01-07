run:
	python3 cmd/main.py

black:
	black ../homestation/cmd
	black ../homestation/config
	black ../homestation/internal

lint: black
	pylama ../homestation/cmd
	pylama ../homestation/config
	pylama ../homestation/internal

mypy: black
	mypy ../homestation/cmd
	mypy ../homestation/config
	mypy ../homestation/internal
