CFLAGS=-Wall -Wextra -std=gnu99
SRC=qcgc.c arena.c bump_allocator.c

lib: $(SRC)
	$(CC) $(CFLAGS) -fpic -shared -o qcgc.so $^

support:
	cd test && make $@

.PHONY: test
test:
	cd test && make $@

.PHONY: doc
doc:
	doxygen Doxyfile

.PHONY: clean
clean:
	$(RM) -f *.so *.o *.gcov *.gcda *.gcno
	cd test && make $@
