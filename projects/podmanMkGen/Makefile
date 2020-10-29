BIN ?= $(HOME)/.local/bin

help:
	@echo "USAGE: make [clean|install]..."

$(BIN)/mkgen:
	ln -s $(abspath mkgen) $@

install: $(BIN)/mkgen

clean:
	rm -f --preserve-root $(BIN)/mkgen
