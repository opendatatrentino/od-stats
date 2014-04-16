OUTPUT_DIR = output
DATA_DIR = data
TARGETS = \
	$(DATA_DIR)/counters.json \
	$(OUTPUT_DIR)/index.html

all: $(TARGETS)

$(DATA_DIR)/counters.json:
	mkdir -p $(DATA_DIR)
	./update_counters.py > $@

$(OUTPUT_DIR)/index.html:
	./generate_stats.py > $@

regen_page: clean_page $(OUTPUT_DIR)/index.html

clean_page:
	rm -f $(OUTPUT_DIR)/index.html

clean:
	rm -f $(TARGETS)

publish: clean all
	ghp-import -p -n ./output
