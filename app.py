from flask import Flask
import os
import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system information
    username = os.getenv("USER") or os.getenv("varunchopra-08") or "codespace-user"


    full_name = "Varun Chopra"  # Replace with your full name
    ist_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S %Z')

    # Get the output of the 'top' command
    top_output = os.popen("top -b -n 1").read()

    # Return the result as HTML
    return f"""
    <h1>Name: {full_name}</h1>
    <h2>Username: {username}</h2>
    <h3>Server Time (IST): {ist_time}</h3>
    <h4>TOP Output:</h4>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
