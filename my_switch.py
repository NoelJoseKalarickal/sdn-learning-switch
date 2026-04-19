from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

mac_to_port = {}

def _handle_PacketIn(event):
    packet = event.parsed
    dpid = event.dpid
    in_port = event.port

    mac_to_port.setdefault(dpid, {})

    src = packet.src
    if str(src) == "00:00:00:00:00:01":
        log.info("BLOCKED: %s", src)
        return
    dst = packet.dst

    # Learn MAC
    mac_to_port[dpid][src] = in_port
    log.info("LEARN: %s on port %s", src, in_port)

    if dst in mac_to_port[dpid]:
        out_port = mac_to_port[dpid][dst]

        # 🔥 Install flow rule (IMPORTANT FIX)
        flow_mod = of.ofp_flow_mod()
        flow_mod.match.in_port = in_port
        flow_mod.match.dl_dst = dst
        flow_mod.actions.append(of.ofp_action_output(port=out_port))
        event.connection.send(flow_mod)

    else:
        out_port = of.OFPP_FLOOD

    # Send packet
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=out_port))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
