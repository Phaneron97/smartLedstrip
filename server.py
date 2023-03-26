# server.py
import http.server # Our http server handler for http requests
import socketserver # Establish the TCP Socket connections
import RPi.GPIO as GPIO
import json
import urllib
# import gpio

Red = 12
Green = 13
Blue = 18
 
# Set the pin numbering scheme
GPIO.setmode(GPIO.BCM)

# Set up pin 12 as an output pin
GPIO.setup(Red, GPIO.OUT)
GPIO.setup(Green, GPIO.OUT)
GPIO.setup(Blue, GPIO.OUT)

PORT = 9010
 
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    # def getUserState():
    #     query = path.split('?')[1]
    #     pin, state = query.split('&')
    #     pin = int(pin.split('=')[1])
    #     state = int(state.split('=')[1])
    # return state

    def do_GET(self):
        if self.path == '/gpio_states.json':
            # const url = `gpio_states.json?cache=${Date.now()}`;
            self.path = 'gpio_states.json'
        if self.path.startswith('/gpio'):
            query = self.path.split('?')[1]
            pin, state = query.split('&')
            pin = int(pin.split('=')[1])
            state = int(state.split('=')[1])
            if state == 1:
                GPIO.output(pin, GPIO.HIGH)
            else:
                GPIO.output(pin, GPIO.LOW)
            self.send_response(200)
            self.end_headers()
            # self.wfile.write(b'GPIO request processed')

            gpio_states = {"gpio12": GPIO.input(12)}
            with open('gpio_states.json', 'w') as f:
                json.dump(gpio_states, f)
        # if self.path.startswith('/submit'):
        #     query = urllib.parse.parse_qs(self.path.split('?')[1])
        #     name = query['name'][0] if 'name' in query else ''
        #     email = query['email'][0] if 'email' in query else ''
        #     self.send_response(200)
        #     self.end_headers()
        #     self.wfile.write(f"Python Name: {name}, Email: {email}".encode())
        else:
            # Handle other URLs with the default SimpleHTTPRequestHandler
            http.server.SimpleHTTPRequestHandler.do_GET(self)
 
Handler = MyHttpRequestHandler
 
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Http Server Serving at port", PORT)
    httpd.serve_forever()