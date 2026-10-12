import socket, threading, time
import random
import select
import sys
from logger import Logger
CNTR_SERVER_ADDR = "127.0.0.1" # server address
CLIENT_ADDR = "127.0.0.1" # client address
CTRL_PORT = 8000 # control port (server side)
DATA_PORT = 5390 # data port (client side)
QUALITY_PORT = 8220 # quality port (server side)

class Client:
    def __init__(self):
        self.ctrl_socket = {} # socket for control channel
        self.data_socket = {} # socket for data channel
        self.quality_socket = {} # socket for quality channel
        self.state = "INIT" # state of the client
        self.logger = Logger("client_log.txt") # logger for the client
        self.received_data = 0 # number of data packets received
        self.data_thread = None # thread for listening to data channel
        self.feedback_thread = None # thread for sending quality feedback

    def setup(self):
        self.ctrl_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket for control channel
        self.data_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP socket for data channel
        self.quality_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP socket for quality channel
        '''----------P1: Connect to server and bind to port(s) here----------------'''
        









        '''----------------------------------------------------------'''
        self.state = "READY"
    
    def send_ctrl(self, request):
        '''----------P2: Send control request to server----------------'''
        '''massage format: {request} ctrl://{CNTR_SERVER_ADDR}:{CTRL_PORT}'''
        '''Server will reply with a message after TCP connection is established'''
        '''Use logger to print the reply from the server'''



        






        '''----------------------------------------------------------'''

    def play(self):
        print("Press 1 to Pause, 2 to Teardown")
        self.state = "PLAYING"
        self.send_ctrl("PLAY")

        '''----------P3: Start playing----------------'''
        '''Suggestion: Start two threads: one for listening to data channel (UDP) and one for sending quality feedback (UDP)'''










        
        '''----------------------------------------------------------'''

    def pause(self):
        self.send_ctrl("PAUSE")
        self.state = "READY"

    def teardown(self):
        self.send_ctrl("TEARDOWN")
        self.state = "INIT"
    
    def listen_data(self):
        '''----------P4: Listen to data channel----------------'''
        '''Receive data from server'''
        '''Print the received data using logger'''
        '''Update the number of data packets received'''
        '''Handle timeout (e.g., play completed)'''











        '''----------------------------------------------------------'''
        
   
    def feedback_channel(self):
        '''----------P5: Send quality feedback----------------'''
        '''Send quality feedback to server to each data segment received'''
        '''Quality is a random number between 0 and 1'''
        '''message format: QUALITY:{quality:.2f}'''











        '''----------------------------------------------------------'''

    def get_input(self, timeout=0.1):
        # Check if there's input available
        ready, _, _ = select.select([sys.stdin], [], [], timeout)
        if ready:
            return input()
        return None
    def close_sockets(self):
        # close all sockets, can be modified to handle exceptions
        self.data_socket.close()
        self.ctrl_socket.close()
        self.quality_socket.close()

if __name__ == '__main__':
    client = Client()
    while True:
        client.setup() # connect to server and bind to port(s)
        input("Press Enter to start...")
        client.play() # start playing if enter is pressed
        while client.state == "PLAYING":                
            command = client.get_input() # get input from user
            # If no input and state changed, break
            if command is None and client.state != "PLAYING":
                break
            if command == "1":
                client.pause()
                input("Paused. Press Enter to resume...")
                client.play()  # Resume playing
            elif command == "2":
                client.teardown()
                print("Teardown complete!")        
        # Check if state changed to INIT (timeout or error)
        if client.state == "INIT":
            client.close_sockets()
            print("Session ended due to timeout or error")
            print("Press R to start again; Press Q to quit.")
            command = input()
            if command.upper() == "Q":
                break
            elif command.upper() == "R":
                continue
            else:
                print("Invalid command")
                continue
            