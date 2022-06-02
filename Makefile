THEME ?= short

resume-export:
	cp build/resume.json resume.json
	resume export --theme $(THEME) resume.pdf
	cp resume.pdf build/resume.pdf

.venv/bin/python:
	poetry install

build/resume.json: .venv/bin/python update.py
	poetry run python update.py

.make:
	mkdir .make

.make/image-$(THEME): Dockerfile .make Makefile
	docker build --build-arg THEME=$(THEME) . -t "resume-theme-$(THEME)"
	touch $@

build/resume.pdf: build/resume.json .make/image-$(THEME) Makefile
	docker run -v $(shell pwd)/build:/resume/build "resume-theme-$(THEME)" make resume-export

resume: build/resume.pdf
