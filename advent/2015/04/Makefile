CFLAGS += -lmhash -g

.PHONY: all
all: solution

.PHONY: clean
clean:
	rm *.o solution

solution: solution.o
	$(CC) $(CFLAGS) -o $@ $^
