"""
The web server for the Gydonim camp website
By, Maya Vaksin
"""

"""
Libraries
"""
# libraries for html & python communication.
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
import asyncio
import webbrowser

# import json
# import socket

"""
Main Database
"""
app = Flask(__name__, template_folder='templates')

# take from a different file?
mador_list = [["מחשוב", "it_symbol"], ["לוגיסטיקה", "logic_symbol"], ["מרפאה", "clinic_symbol"],
              ["רס״ר", "sergeant_symbol"],
              ["מב״ס", "command_symbol"], ["מספרה", "hair_symbol"], ["נשקייה", "weapon_symbol"],
              ["מטבח", "kitchen_symbol"],
              ["רבנות", "jewish_symbol"], ["שלישות", "adjutancy_symbol"], ["אבטחה ואישורים", "security_symbol"],
              ["אירועים", "event_symbol"]]

"""
Web Functions
"""


@app.route("/", methods=["POST", "GET"])
def main_page():
    return render_template('main_page.html', mador_list=mador_list)


@app.route("/madors", methods=['GET'])
def madors_page():
    return render_template('madors_page.html', mador_list=mador_list)


@app.route("/people", methods=['GET'])
def people_page():
    return render_template('people_page.html')


if __name__ == '__main__':
    """
    PORT, HOST = 45002, "172.17.74.124"  # gets the host's IP manually (will be changed)
    BUFSIZ = 1024  # the buff size of the message.
    ADDR = (HOST, PORT)  # the server's address.

    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating a client socket.
    client_sock.settimeout(2)  # the client waits 2 seconds for an answer.
    try:  # try to connect to the server's socket.
        client_sock.connect(ADDR)

    except (ConnectionRefusedError, OSError):
        print("The server is closed")

    except socket.timeout:
        print("Time ran out. Please try again later")

    else:"""
    try:
        app.secret_key = 'super secret key'
        app.config['SESSION_TYPE'] = 'filesystem'
        app.run(port=8000, debug=False, host="0.0.0.0",
                threaded=True)  # application will start listening for web request on port 5000

    except Exception as e:
        print(e)
        # client_sock.close()
