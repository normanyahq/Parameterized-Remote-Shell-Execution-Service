from flask import Flask, request
from subprocess import Popen, PIPE
import json

app = Flask(__name__)

HelpMessage = """
Usage:
    POST command to this URL with following payload:
        {"file": "...", args:[...]}
    We are using this format to keep it the same with NodeJs spawnSync
Example:
    {"file": "ls", args: ["-l", "-a"]}
Test with curl:
    curl -X POST -H "Content-type: application/json" --data '{"file": "ls", "args":["-a", "-l"]}' localhost:41414
"""

@app.route("/", methods=["POST", "GET"])
def commandExecutor():
    if request.method == "GET":
        return HelpMessage
    elif request.method == "POST":
        commandObject = request.get_json()
        print ('Command Object: {}'.format(commandObject))
        process = Popen([commandObject["file"]] + commandObject["args"],
                        stdin=PIPE,
                        stdout=PIPE,
                        stderr=PIPE)
        (stdout, stderr) = process.communicate(input=commandObject.get("input", ""))
        result = json.dumps({ "stdout": stdout,
                            "stderr": stderr,
                            "exit_code": process.returncode,
                            "error": process.returncode!=0})
        print (stdout)
        if stderr:
            print (stderr)
        return result
