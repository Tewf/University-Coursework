# Plain C11, warnings as errors, no dependency outside the standard library.
CC      = gcc
CFLAGS  = -std=c11 -Wall -Wextra -Wpedantic -Werror -O2
LDFLAGS = -lm

LIB_SOURCES = cell.c maze.c region_tree.c generator.c invariants.c solver.c svg.c
LIB_OBJECTS = $(LIB_SOURCES:.c=.o)
PROGRAMS    = maze benchmark tests

.PHONY: all test clean

all: $(PROGRAMS)

maze: main.o $(LIB_OBJECTS)
	$(CC) $^ -o $@ $(LDFLAGS)

benchmark: benchmark.o $(LIB_OBJECTS)
	$(CC) $^ -o $@ $(LDFLAGS)

tests: tests.o $(LIB_OBJECTS)
	$(CC) $^ -o $@ $(LDFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

test: tests
	./tests

clean:
	rm -f *.o $(PROGRAMS) maze.svg
