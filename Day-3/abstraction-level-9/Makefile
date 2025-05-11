# Targets
.PHONY: all run build-package publish-package clean

# Default target
all: run

# Run the application locally
run:
	python main.py --watch

# Build the package for distribution (create a tarball or zip of the project)
build-package:
	python setup.py sdist

# Clean up temporary and build files
clean:
	rm -rf build dist *.egg-info
