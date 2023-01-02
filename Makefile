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