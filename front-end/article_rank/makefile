CC = gcc -std=c99 -g
O ?= 3
CFLAGS = -I. -lm -pthread
DEPS = ranker.h
OBJ = ranker.o

%.o: %.c $(DEPS)
	$(CC) -O$(O) -c -o $@ $< $(CFLAGS)

ranker: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)
