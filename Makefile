resume-export:
	cp build/resume.json resume.json
	resume export --theme ${THEME} build/resume.pdf

.venv/bin/python:
	poetry install

resume.json: .venv/bin/python update.py
	poetry run python update.py

.make:
	mkdir .make

.make/image-${THEME}: Dockerfile .make Makefile
	docker build --build-arg THEME . -t resume-theme-${THEME}
	touch $@

resume.pdf: resume.json .make/image-${THEME}
	docker run -v $(shell pwd)/build:/resume/build resume-theme-${THEME} make resume-export

