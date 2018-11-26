.PHONY: run clean

index: env
	fab index

env: requirements.txt
	fab setup

clean:
	@rm -rf .setup
	@rm -rf *.egg-info
	@rm -rf env
	@rm -rf build
	@rm -rf dist
	@rm -rf *.pyc