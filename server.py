import socket, threading, time
import os
from logger import Logger

CTRL_PORT = 8000
DATA_PORT = 5390
QUALITY_PORT = 8220

class Server:
    def __init__(self):
        self.ctrl_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket for control channel    
        self.data_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP socket for data channel
        self.quality_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP socket for quality channel
        self.client_info = {}
        self.state = "INIT"
        self.session_id = 123456
        self.frame_id = 0
        self.quality_scale = 1.0
        self.client_ip = None
        self.addr = None
        self.segment_size = 10
        self.quality_socket.settimeout(10)
        # Setup logging
        self.logger = Logger("server_log_P1.txt")
        self.ctrl_socket.settimeout(300)
        # Setup thread coordination
        self.shutdown_event = threading.Event() # event to signal all threads to stop
        self.quality_thread = None # thread for listening to quality feedback
        self.quit_thread = None # thread for checking quit command, you can use this or not

    def close_sockets(self):
        # close all sockets, can be modified to handle exceptions
        self.data_socket.close()
        self.ctrl_socket.close()
        self.quality_socket.close()

    def start(self):
        '''----------P2: Bind sockets and start the server----------------'''
        ''' Open two threads (recv_control_request and listen_quality_feedback) to listen to control and quality feedback'''
        ''' Handle timeout (e.g., client disconnected)'''
        









        

        '''----------------------------------------------------------'''

    def recv_control_request(self, conn):
        '''----------P3: Receive control request----------------'''
        '''Receive control request from client (Setup, Play, Pause, Teardown)'''
        '''Use logger to print the received request'''
        '''Update the state of the client (INIT, READY, PLAYING)'''
        '''Send reply to client using reply_control()'''









        '''----------------------------------------------------------'''

    def reply_control(self, conn, request_type):
        reply = f"[CTRL Server] OK, conducting {request_type} for session: {self.session_id}\n"
        conn.send(reply.encode())
    
    def listen_quality_feedback(self):

        '''----------P4: Listen to quality feedback----------------'''
        '''Receive quality feedback from client'''
        '''Update the quality scale'''
        '''Use logger to print the received quality feedback'''
        '''Handle timeout (e.g., client disconnected)'''







        '''----------------------------------------------------------'''

    def send_data(self):
        '''----------P5: Send data to client----------------'''
        '''Send data to client'''
        '''Use logger to print the sent data'''
        '''Handle timeout (e.g., client disconnected)'''
        '''Sequentially send data to client (<id>/self.segment_size)'''










        '''----------------------------------------------------------'''

if __name__ == '__main__':
    server = Server()
    server.start()
    server.close_sockets()