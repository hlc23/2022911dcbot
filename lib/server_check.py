from mcstatus import JavaServer
from socket import gaierror

def server_check(ip: str):
    server_ip = ip
    server = JavaServer.lookup(server_ip, timeout=2.5)
    try:
        status = server.status()
    except gaierror:
        # print("Server not found")
        return None
    if status.version.name == "§4● Offline":
        return "Server is offline"
    if status.players.sample is None:
        return {"Version":status.version.name, "NoP":status.players.online, "Players":[]}
    return {"Version":status.version.name, "NoP":status.players.online, "Players":[player.name for player in status.players.sample]}
