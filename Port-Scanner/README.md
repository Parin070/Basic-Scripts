# Multithreaded Port Scanner

A fast Python-based port scanner that checks 100 commonly used ports using multithreading.

> ⚠️ Educational purposes only. Only scan systems you own or have explicit permission to test. Unauthorized port scanning may be illegal.

## How it Works

- Takes a target IP as input
- Uses a queue to distribute ports across 20 threads simultaneously
- Attempts a TCP connection on each port with a 1 second timeout
- Reports all open ports at the end

## How to Run
```bash
python3 port_scanner.py
```

Enter the target IP when prompted. For practice you can use:
```
scanme.nmap.org
```

## Ports Scanned

100 commonly used ports including:

- **Web:** 80, 443, 8080, 8443
- **Remote access:** 22 (SSH), 23 (Telnet), 3389 (RDP)
- **Databases:** 3306 (MySQL), 5432 (PostgreSQL), 27017 (MongoDB)
- **Mail:** 25, 465, 587, 993, 995
- And many more...

## Known Limitations

- ❌ TCP only — no UDP scanning
- ❌ No banner grabbing or service detection
- ❌ Contains a predefined list of 100 commonly used ports for testing purposes — edit `portList` in the script to add more ports as needed