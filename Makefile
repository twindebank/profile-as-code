
PIPENV_MADE = $(shell pipenv --venv)/made

$(PIPENV_MADE): Pipfile Pipfile.lock
	pip3 install --upgrade pipenv
	pipenv install
	pipenv update
	touch $$(pipenv --venv)/made

pipenv: $(PIPENV_MADE)



profiles: profile-public.yml profile-private.yml profile/*
	@echo "Generating profiles..."
	pipenv run python pyprofile/parsing.py profile/ --censored -o profile-public.yml
	pipenv run python pyprofile/parsing.py profile/ --uncensored -o profile-private.yml


