CC = gcc -std=c99 -g
O ?= 0
CFLAGS = -I. -lm
DEPS = ranker.h
OBJ = ranker.o

%.o: %.c $(DEPS)
	$(CC) -O$(O) -c -o $@ $< $(CFLAGS)

ranker: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)
