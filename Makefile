.PHONY: docs

RM = rm -rf
AUTHOR := $(shell git config user.name)
EMAIL  := $(shell git config user.email)


bin/buildout:
	/usr/bin/env python bootstrap.py
	bin/buildout

clean:
	@find . \( \
		-iname "*.pyc" \
		-or -iname "*.pyo" \
		\) -delete

distclean: clean
	@$(RM) \
		bin/ \
		build/ \
		develop-eggs/ \
		dist/ \
		eggs/ \
		parts/ \
		src/*.egg-info/ \
		MANIFEST \
		.installed.cfg

release: distclean
	#rpmdev-bumpspec --comment="Initial RPM release" --userstring="$(AUTHOR) $(EMAIL)"
	/usr/bin/env python setup.py sdist
	/usr/bin/env python setup.py bdist_egg

