FROM python:3.9-slim

RUN pip install scapy

COPY mdns_repeater.py /usr/local/bin/mdns_repeater.py
COPY run.sh /usr/local/bin/run.sh

RUN chmod +x /usr/local/bin/mdns_repeater.py /usr/local/bin/run.sh

CMD [ "/usr/local/bin/run.sh" ]