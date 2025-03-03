CC=gcc
CFLAGS=-Wall -Wextra -O2

mdns-repeater: mdns-repeater.o
	$(CC) $(CFLAGS) -o mdns-repeater mdns-repeater.o

mdns-repeater.o: mdns-repeater.c
	$(CC) $(CFLAGS) -c mdns-repeater.c

clean:
	rm -f mdns-repeater mdns-repeater.o