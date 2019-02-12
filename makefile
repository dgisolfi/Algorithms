# Author: Daniel Nicolas Gisolfi
# Algorithims

init:
	@python3 -m pip install -r requirements.txt

clean:
	@echo "TODO: setup a proper clean function"

# TESTS
test_assignment_1:
	@python3 -m pytest -s ./assignments/assign_1/

test_assignment_2:
	@python3 -m pytest -s ./assignments/assign_2/

.PHONY: init test_assignment_1 test_assignment_2