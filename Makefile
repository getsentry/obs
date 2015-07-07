develop: setup-git
	@echo "--> Installing dependencies"
	pip install -e .
	pip install "file://`pwd`#egg=obs[test]"

setup-git:
	@echo "--> Installing git hooks"
	git config branch.autosetuprebase always
	cd .git/hooks && ln -sf ../../hooks/* ./
	@echo ""

test: develop lint-python test-python

test-python:
	@echo "--> Running Python tests"
	py.test
	@echo ""

lint-python:
	@echo "--> Linting Python files"
	PYFLAKES_NODOCTEST=1 flake8
	@echo ""
