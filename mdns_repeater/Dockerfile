FROM alpine:3.13

RUN apk add --no-cache build-base supervisor

COPY mdns-repeater.c /usr/src/mdns-repeater.c
COPY Makefile /usr/src/Makefile
COPY run.sh /usr/src/run.sh
COPY supervisord.conf /usr/src/supervisord.conf

WORKDIR /usr/src

RUN make

RUN chmod +x /usr/src/run.sh

CMD [ "/usr/src/run.sh" ]
