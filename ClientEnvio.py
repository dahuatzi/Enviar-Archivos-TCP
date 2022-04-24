import socket

host = '127.0.0.1'
puerto = 1000
FORMAT = "utf-8"

def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, puerto))

    file = open("mandar/recibido.txt", "r")
    data = file.read()

    cliente.send("recibido.txt".encode(FORMAT))

    mensaje = cliente.recv(1024).decode(FORMAT)
    print(f"Se mando un mensaje: {mensaje} ")

    cliente.send(data.encode(FORMAT))
    mensaje = cliente.recv(1024).decode(FORMAT)
    print(f"Se mando un mensaje: {mensaje} ")

    file.close()
    cliente.close()
    print("Desconectado")


if __name__ == "__main__":
    main()