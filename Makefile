profile.yml: profile/*

profile-public:
	@echo "Generating PUBLIC profile..."
	@# todo: rewrite to censor the .private.yml file
	@echo "# generated with files from profile/, do not edit directly" > profile-private.yml
	@cat profile/.private-censored.yml profile/*.yml >> profile-private.yml


profile-private:
	@echo "Generating PRIVATE profile..."
	@echo "# generated with files from profile/, do not edit directly" > profile-public.yml
	@cat profile/.private.yml profile/*.yml >> profile-public.yml
