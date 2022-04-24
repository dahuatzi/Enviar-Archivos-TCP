import socket

host = '127.0.0.1'
puerto = 1000
FORMAT = "utf-8"

def main():
    print("El servidor esta arrancando...")
    servertcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servertcp.bind((host, puerto))
    servertcp.listen(3)
    print("El servidor está escuchando...")

    while True:
        conn, address = servertcp.accept()
        print(f"La conexión desde: {address}")

        filename = conn.recv(1024).decode(FORMAT)
        print("Archivo recibido:")
        file = open(filename, "w")
        conn.send("El archivo se recibió de manera exitosa".encode(FORMAT))

        data = conn.recv(1024).decode(FORMAT)
        print(f"Se recibió: ")
        file.write(data)
        conn.send("File data recibido.".encode(FORMAT))

        file.close()
        conn.close()
        print("Desconectado")


if __name__ == "__main__":
    main()