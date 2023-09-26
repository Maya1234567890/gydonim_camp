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
import os

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

people_list = []

"""
Web Functions
"""


@app.route("/", methods=["POST", "GET"])
def main_page():
    return render_template('main_page.html', mador_list=mador_list)


@app.route("/madors", methods=['POST'])
def madors_page():
    return render_template('madors_page.html', mador_list=mador_list)


@app.route("/people", methods=['POST'])
def people_page():
    return render_template('people_page.html')


@app.route("/news", methods=['POST'])
def news_page():
    return render_template('news_page.html')


@app.route("/mador", methods=['POST'])
def mador_page():
    mador_name = request.form.get('mador_name')
    # take mador symbol from the mador list later!
    # everything has to be dynamic, but i dont know how to store stuff... so for now it's static
    return render_template('mador_page.html', mador_name=mador_name, mador_symbol="it_symbol",
                           commandar="אליאור", )


"""
regular functions
"""


def add_person(name, job, sayings, email, phone, main_page_display):
    """folder_path = "people/" + name
    try:
        os.mkdir(folder_path)
    except FileExistsError:
        # instead of print make an alert in html with a link to his page
        print(name + " כבר קיים במערכת")
        return
    open(folder_path + "/job", "w").write(job)
    open(folder_path + "/sayings", "w").write(sayings)"""

    # f = open("people/file.txt", "w")
    # f.close()


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
    # add_person("אליאור גז", "מפקד מדור תקשוב", "היי אני אליאור גז", "email", "055", True)
    try:
        app.secret_key = 'super secret key'
        app.config['SESSION_TYPE'] = 'filesystem'
        app.run(port=8000, debug=False, host="0.0.0.0",
                threaded=True)  # application will start listening for web request on port 5000

    except Exception as e:
        print(e)
        # client_sock.close()
