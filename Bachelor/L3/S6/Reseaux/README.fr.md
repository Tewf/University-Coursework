# Reseaux informatiques

> [Read in English](README.md)

**Cours :** Reseaux — Licence 3 MIASHS, Semestre 6, Universite Grenoble Alpes

Travaux pratiques sur les reseaux TCP/IP, l'analyse de paquets et la simulation reseau en environnement virtuel.

## Ce que vous apprendrez

- Pile protocolaire TCP/IP : adresses MAC, adresses IP, resolution DNS
- Protocole ICMP : ping, requetes/reponses echo
- Protocole HTTP : cycle requete/reponse client-serveur
- Cablage reseau : cables droits vs. cables croises
- Capture et analyse de paquets avec Wireshark
- Configuration de VLANs et domaines de diffusion
- Configuration d'interfaces reseau sous Linux

## Vue d'ensemble des TPs

| TP | Theme | Activites principales |
|----|-------|-----------------------|
| **TP1** | Fondamentaux IP | Configuration reseau, ping, capture de paquets avec Marionnet |
| **TP2** | IP avance & Routage | Traceroute, VLANs, routage inter-reseaux |

## Mise en place de l'environnement

Les TPs utilisent **Marionnet**, un simulateur reseau, fonctionnant sur une machine virtuelle Debian.

### Configuration de la VM

Le dossier `debian/` contient une image VM Debian 11 pre-configuree (`.qcow2`) et les instructions d'installation pour KVM/virt-manager.

```sh
# Lancer la VM avec virt-manager (suivre les instructions dans debian/instrction)
virt-manager
```

### Dans la VM

- Marionnet est pre-installe pour la simulation reseau
- Wireshark disponible pour l'analyse de paquets
- Outils reseau Linux standard (`ifconfig`, `ping`, `traceroute`)

## Structure du dossier

```
Reseaux/
|-- TP/
|   |-- TP1/
|   |   |-- TP_IP1.pdf         <- Sujet : fondamentaux IP
|   |   |-- capture1.mar       <- Projet Marionnet
|   |-- TP2/
|       |-- TP_IP2.pdf         <- Sujet : IP avance
|       |-- capture2.mar       <- Simulation reseau
|       |-- traceroute.mar     <- Simulation traceroute
|-- debian/
    |-- debian11-miashs.qcow2  <- Image VM (8.1 Go)
    |-- instrction             <- Guide d'installation
```

## Outils

- **Marionnet** — Simulateur de topologies reseau
- **Wireshark** — Analyseur de paquets
- **KVM/QEMU** — Virtualisation
- **CLI Linux** — `ifconfig`, `ping`, `traceroute`, `ip`
