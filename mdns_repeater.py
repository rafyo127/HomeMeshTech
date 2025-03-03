from scapy.all import sniff, sendp, UDP

def handle_packet(packet, iface_out):
    # Check if the packet is an mDNS packet
    if packet.haslayer(UDP) and packet[UDP].sport == 5353 and packet[UDP].dport == 5353:
        print(f"Captured mDNS packet: {packet.summary()}")
        # Send the packet out on the specified interface
        sendp(packet, iface=iface_out, verbose=False)
        print("Packet forwarded")

def main(iface_in, iface_out):
    print(f"Starting mDNS Repeater: {iface_in} -> {iface_out}")
    # Start sniffing on the input interface
    sniff(iface=iface_in, filter="udp port 5353", prn=lambda pkt: handle_packet(pkt, iface_out))

if __name__ == "__main__":
    import sys
    iface_in = sys.argv[1]
    iface_out = sys.argv[2]
    main(iface_in, iface_out)
