# RPC Example in Python

This project demonstrates a simple Remote Procedure Call (RPC) implementation using Python's `xmlrpc` library. It consists of a server and a client where the server exposes a function, and the client calls that function remotely.

---

## Project Structure

        RPCExample/ ├── server/ │ └── rpc_server.py ├── client/ │ └── rpc_client.py


---

## Requirements

- Python 3.x
- `xmlrpc.client` and `xmlrpc.server` (These are built-in Python modules, no need to install them separately)

---

## How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone <repository_url>


2. **Start the Server**:

- Navigate to the server folder:

    cd RPCExample/server

- Run the rpc_server.py script:

    python rpc_server.py

- The server will start listening on port 9000.

3. **Run the Client:**

- Open another terminal and navigate to the client folder:
    cd RPCExample/client
- Run the rpc_client.py script:
    
    python rpc_client.py
- The result of the remote procedure call will be printed in the client terminal:
    The result of the sum is: 8

## Code Explanation
- Server Side (rpc_server.py)
We create an XML-RPC server using Python's SimpleXMLRPCServer class.
The server exposes a method add that takes two integers and returns their sum.
The server listens on localhost and port 9000.
- Client Side (rpc_client.py)
The client connects to the XML-RPC server at localhost:9000.
The client calls the add function exposed by the server and prints the result.