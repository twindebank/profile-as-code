.PHONY: pipenv

yaml-profile-targets := $(wildcard profile/*.yml)

PIPENV_MADE = $(shell pipenv --venv)/made

$(PIPENV_MADE): Pipfile Pipfile.lock
	pip3 install --upgrade pipenv
	pipenv install
	pipenv update
	touch $$(pipenv --venv)/made

pipenv: $(PIPENV_MADE)

profile-private.yml: $(yaml-profile-targets) $(PIPENV_MADE)
	@echo "Generating private profile..."
	pipenv run python -m pyprofile.parsing profile/ --uncensored -o profile-private.yml


profile-public.yml: $(yaml-profile-targets) $(PIPENV_MADE)
	@echo "Generating public profile..."
		pipenv run python -m pyprofile.parsing profile/ --censored -o profile-public.yml


yaml-profiles: profile-private.yml profile-public.yml

tex-cv-%: yaml-profiles
	pipenv run python -m pyprofile.transformers.texcv.generate profile-$*.yml tex-cv-$*
	docker run --rm -v $(shell pwd)/tex-cv-$*:/source schickling/latex xelatex resume.tex

