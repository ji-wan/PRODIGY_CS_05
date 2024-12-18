import scapy.all as scapy

def packet_callback(packet):
    if packet.haslayer(scapy.IP):
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto 
        
        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {protocol}")
        
        if packet.haslayer(scapy.TCP):
            try:
                payload = packet[scapy.Raw].load
                decode_payload = payload.decode('utf-8', 'ignore')
                print(f"Payload: {decode_payload}")
            except(IndexError, UnicodeDecodeError):
                print("unable to decode TCP payload.")
            
        elif packet.haslayer(scapy.UDP):
            try:
                payload = packet[scapy.Raw].load
                decode_payload = payload.decode('utf-8', 'ignore')
                print(f"Payload: {decode_payload}")
            except(IndexError, UnicodeDecodeError):
                print("unable to decode UDP payload.")
                
def start_sniffing():
    scapy.sniff(prn=packet_callback, store=False)
    
start_sniffing()
               
            