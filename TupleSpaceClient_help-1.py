import socket
import sys
import os

def main():
    if len(sys.argv) != 4:
        print("Usage: python tuple_space_client.py <server-hostname> <server-port> <input-file>")
        sys.exit(1)

    hostname = sys.argv[1]
    port = int(sys.argv[2])
    input_file_path = sys.argv[3]

    if not os.path.exists(input_file_path):
        print(f"Error: Input file '{input_file_path}' does not exist.")
        sys.exit(1)

    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((hostname, port))
    except socket.error as e:
        print(f"Error connecting to server: {e}")
        sys.exit(1)

    try:
        for line in lines:
            line = line.strip()
            if not line:
                continue

            parts = line.split(" ", 2)
            cmd = parts[0]
            message = ""

            try:
                if cmd in ["READ", "GET"]:
                    if len(parts) < 2: 
                        raise ValueError("Missing key")
                    key = parts[1]
                    if len(key) > 970:
                        print(f"Error: Key too long. Ignoring entry.")
                        continue
                    command_char = "R" if cmd == "READ" else "G"
                    size = 6 + len(key)
                    message = f"{size:03d} {command_char} {key}"
                    
                elif cmd == "PUT":

            response = response_buffer.decode().strip()
            print(f"{line}: {response}")
            

    except (socket.error, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    finally:
        # TASK 4: Close the socket when done (already called for you — explain why
        # finally: is the right place to do this even if an error occurs above).
        sock.close()

if __name__ == "__main__":
    main()
