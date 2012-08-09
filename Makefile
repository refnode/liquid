# Workaround Makefile for cleanup

RM = rm -rf

.PHONY: clean

bootstrap: distclean
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
		docs/doctrees/ \
		docs/html/ \
		docs/make.bat \
		docs/Makefile \
		eggs/ \
		parts/ \
		src/*.egg-info/ \
		MANIFEST \
		.installed.cfg

