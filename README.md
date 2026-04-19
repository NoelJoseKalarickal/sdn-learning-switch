# SDN Learning Switch using POX and Mininet

## Problem Statement

Implement a Software Defined Networking (SDN) learning switch controller that dynamically learns MAC addresses and installs flow rules to optimize packet forwarding.

## Tools Used

* POX Controller
* Mininet
* Open vSwitch

## How It Works

* Switch initially does not know where to forward packets
* Sends packet to controller (PacketIn)
* Controller learns MAC → port mapping
* Installs flow rule (match-action)
* Future packets are forwarded directly

## Setup & Execution

1. Start controller:
   cd ~/pox
   python3 pox.py forwarding.my_switch

2. Start Mininet:
   sudo mn --topo single,3 --controller remote

3. Test:
   pingall
   iperf h1 h2

## Results

* Successful communication (0% packet loss)
* Flow rules dynamically installed
* Reduced controller involvement after learning

## Screenshots

(Add your screenshots here)

## Conclusion

The project demonstrates SDN concepts including controller-switch interaction, packet handling, and dynamic flow rule installation using the match-action paradigm.
