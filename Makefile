
PIPENV_MADE = $(shell pipenv --venv)/made

$(PIPENV_MADE): Pipfile Pipfile.lock
	pip3 install --upgrade pipenv
	pipenv install
	pipenv update
	touch $$(pipenv --venv)/made

pipenv: $(PIPENV_MADE)



profiles: profile-public.yml profile-private.yml profile/*
	@echo "Generating profiles..."
	@echo "# generated with files from profile/, do not edit directly" > profile.yml.tmp
	@cat profile/.private.yml profile/*.yml >> profile.yml.tmp
	pipenv run python pyprofile/parsing.py profile.yml.tmp --censored -o profile-public.yml
	pipenv run python pyprofile/parsing.py profile.yml.tmp --uncensored -o profile-private.yml
#	rm profile.yml.tmp


