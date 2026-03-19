# DDoS Simulation Script

A basic Python script that simulates a DDoS attack by flooding a target with HTTP GET requests using multithreading. Built for educational purposes to understand how volumetric attacks work and how they appear in network traffic analysis tools like Wireshark.

>  Educational purposes only. Only run against systems you own or have explicit permission to test. Do not use against external targets. Unauthorized DDoS attacks are illegal.

## How it Works

- Takes a target IP and port as input
- Spawns 500 threads simultaneously
- Each thread continuously sends HTTP GET requests over a TCP connection
- Includes a spoofed Host header to simulate IP spoofing at the application layer

## How to Run

Start a local test server first:
```bash
python3 -m http.server 8080
```

Then run the script:
```bash
python3 ddos.py
```

Enter `127.0.0.1` as the target and `8080` as the port for local testing.

## Testing

Tested locally on Kali Linux using a Python HTTP server as the target. Traffic was captured and analyzed in Wireshark on the loopback interface. Packet count jumped from ~24 packets to 155,000+ in just over 1 minute.

See `WRITEUP.md` for full testing documentation and Wireshark analysis.

## Known Limitations

-  Application layer spoofing only — does not spoof actual source IP at network level
-  TCP based — no UDP flood
-  No randomization of request patterns
-  Easily blocked by rate limiting or firewalls