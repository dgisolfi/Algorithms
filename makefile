# Author: Daniel Nicolas Gisolfi
# Algorithims

init:
	@python3 -m pip install -r requirements.txt

clean:
	@echo "TODO: setup a proper clean function"

# TESTS
test_assignment_1:
	@python3 -m pytest -s ./assignments/1/test/testLinkedList.py

.PHONY: init test