profile.yml: profile/*

profile-%:
	@echo "Generating $* profile..."
	@echo "# generated with files from profile/, do not edit directly" > profile-$*.yml
	@cat profile/.$*.yml profile/*.yml >> profile-$*.yml


profiles: profile-public profile-private