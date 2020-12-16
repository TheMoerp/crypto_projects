#############################################
##     PROJECT OPTIONS (do not touch)      ##
#############################################

# C source files
SRC_FILES = skinny.c testbench.c

# Compiler options
OPTS = -Wall -Wextra -Wshadow -pedantic -pedantic-errors -O3 -fomit-frame-pointer -std=c99

# Build directory (auto generated)
BUILD_DIR = build

# Output file
OUTPUT = out

# Minimum allowed GCC version
GCC_MINIMUM_VERSION = 7.4.0

#############################################
##          CORE (do not touch)            ##
#############################################
GCC_VERSION := $(shell echo `gcc -dumpfullversion`)
GCC_VERSION_INT := $(shell echo `echo $(GCC_VERSION) | sed -e 's/\.\([0-9][0-9]\)/\1/g' -e 's/\.\([0-9]\)/0\1/g' -e 's/^[0-9]\{3,4\}$$/&00/'`)
GCC_MINIMUM_VERSION_INT := $(shell echo `echo $(GCC_MINIMUM_VERSION) | sed -e 's/\.\([0-9][0-9]\)/\1/g' -e 's/\.\([0-9]\)/0\1/g' -e 's/^[0-9]\{3,4\}$$/&00/'`)

.PHONY: all compile clean

OBJ_FILES = $(addprefix $(BUILD_DIR)/,$(SRC_FILES:.c=.o))

all: compile $(BUILD_DIR)/$(OUTPUT)
	@echo '__________Executing__________'
	@echo
	@$(BUILD_DIR)/$(OUTPUT)

compile:
	@echo '__________Compiling__________'
# ifeq ($(shell expr $(GCC_VERSION_INT) \< $(GCC_MINIMUM_VERSION_INT)), 1)
# 	$(error Your GCC is outdated! Your version: $(GCC_VERSION), minimum allowed version: $(GCC_MINIMUM_VERSION))
# endif
	@mkdir -p $(BUILD_DIR)

$(BUILD_DIR)/$(OUTPUT): $(OBJ_FILES)
	gcc $(OPTS) $(OBJ_FILES) -o $(BUILD_DIR)/$(OUTPUT)

clean:
	@echo  Removing build aritfacts...
	rm -rf $(BUILD_DIR)
	rm -rf *.stackdump

$(BUILD_DIR)/%.o: %.c
	gcc $(OPTS) -c $< -o $@
