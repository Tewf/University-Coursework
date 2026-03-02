# Computer Networks

> [Lire en francais](README.fr.md)

**Course:** Reseaux — Licence 3 MIASHS, Semester 6, Universite Grenoble Alpes

Practical sessions on TCP/IP networking, packet analysis, and network simulation using virtual environments.

## What You'll Learn

- TCP/IP protocol stack: MAC addresses, IP addresses, DNS resolution
- ICMP protocol: ping, echo requests/replies
- HTTP protocol: client-server request/response cycle
- Network cabling: straight vs. crossover cables
- Packet capturing and analysis with Wireshark
- VLAN configuration and broadcast domains
- Linux network interface configuration

## TP Overview

| TP | Topic | Key Activities |
|----|-------|----------------|
| **TP1** | IP Networking Fundamentals | Network configuration, ping, packet capture with Marionnet |
| **TP2** | Advanced IP & Routing | Traceroute, VLANs, routing between networks |

## Environment Setup

The practical sessions use **Marionnet**, a network simulator, running on a Debian virtual machine.

### VM Setup

The `debian/` folder contains a pre-configured Debian 11 VM image (`.qcow2`) and setup instructions for KVM/virt-manager.

```sh
# Launch the VM with virt-manager (follow instructions in debian/instrction)
virt-manager
```

### Inside the VM

- Marionnet is pre-installed for network simulation
- Wireshark available for packet analysis
- Standard Linux networking tools (`ifconfig`, `ping`, `traceroute`)

## Folder Structure

```
Reseaux/
|-- TP/
|   |-- TP1/
|   |   |-- TP_IP1.pdf         <- Subject: IP fundamentals
|   |   |-- capture1.mar       <- Marionnet project
|   |-- TP2/
|       |-- TP_IP2.pdf         <- Subject: Advanced IP
|       |-- capture2.mar       <- Network simulation
|       |-- traceroute.mar     <- Route tracing simulation
|-- debian/
    |-- debian11-miashs.qcow2  <- VM image (8.1 GB)
    |-- instrction             <- Setup guide
```

## Tools

- **Marionnet** — Network topology simulator
- **Wireshark** — Packet analyzer
- **KVM/QEMU** — Virtualization
- **Linux CLI** — `ifconfig`, `ping`, `traceroute`, `ip`
