#!/usr/bin/env python3 
from flask import Flask, request 
import logging, os 
app = Flask(__name__) 
os.makedirs('/var/log/honeypot', exist_ok=True) 
logging.basicConfig(filename='/var/log/honeypot/bait.log', level=logging.INFO, format='%(asctime)s %(message)s') 
 
@app.route('/', methods=['GET']) 
def index(): 
    return "Thanks for visiting", 200 
 
@app.route('/submit', methods=['POST']) 
def submit(): 
    data = request.form.to_dict() or request.get_data(as_text=True) 
    logging.info("Submission from %s: %s", request.remote_addr, data) 
    return "Thank you", 200 
 
if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=8080) 
