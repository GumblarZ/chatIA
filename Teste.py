import socket
from module.config import caminho, porta

# Configuração do socket
server_address = (caminho, porta)

# Cria um novo socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Conecta ao servidor
    sock.connect(server_address)
    print("Conectado ao servidor.")
    
    # Envia uma solicitação HTTP/1.1 (exemplo simples)
    request = f'GET / HTTP/1.1\r\nHost: {caminho}\r\nConnection: close\r\n\r\n'
    sock.sendall(request.encode())
    
    # Recebe a resposta do servidor
    data = sock.recv(1024)
    print(data.decode())
    
finally:
    # Fecha o socket
    sock.close()
    print("Conexão fechada.")
