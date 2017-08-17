.PHONY: build clean dev

NPM_BINS = ./node_modules/.bin

build:
	@echo "# Building production bundle"
	${NPM_BINS}/webpack

clean:
	rm -rf ./dist

dev:
	@echo "# Starting development server"
	${NPM_BINS}/webpack-dev-server
