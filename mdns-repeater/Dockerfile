FROM alpine:3.18

RUN apk add --no-cache iproute2 jq

COPY mdns-repeater /usr/bin/mdns-repeater
COPY run.sh /run.sh

RUN chmod +x /usr/bin/mdns-repeater /run.sh

CMD ["/run.sh"]
