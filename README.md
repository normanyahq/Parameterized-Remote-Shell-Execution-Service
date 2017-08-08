# Parameterized-Remote-Shell-Execution-Service 
Execute File on Remote Machine with Parameterized Arguments through REST API

To avoid shell injection, we may need to run some executables with parameter list. It can be easily done on local machine with APIs provided by compilers, interpreters, etc. However, I haven't found any utilities that can run executable on remote machine that is parameterized, so I decided to write this one.

Note that this tool should only be used for debugging purpose, because it doesn't have any authentication, which means anyone can run command through this service. If you do need authentication, feel free to modify the code. One simple way is to use HTTP Basic Auth provided by Flask: http://flask.pocoo.org/snippets/8/


## Install
make install

## Run in Debug Mode
make debug

## Run in Multithreaded Mode
make run

## Usage

### Payload

- file: The file or command to execute 
- args: the arg list for the executable
- input: the input for standard input stream

Following payload is equivalent to `echo "/var/tmp\n/tmp" | xargs ls`
```
{
  "file": "xargs",
  "args": [
    "ls"
  ],
  "input": "/var/tmp\n/tmp"
}
```
### Example

POST
```
curl -X POST -H "Content-type: application/json" --data '{"file": "xargs", "args":["ls"], "input":"/var/tmp\n/tmp"}' localhost:41414
```

Response
```
{
  "error": false,
  "exit_code": 0,
  "stderr": "",
  "stdout": "/tmp:\nOSL_PIPE_503_SingleOfficeIPC_5a6dc4eb4f69bf723c573d1689ce47\ncom.adobe.reader.rna.0.1f7\ncom.adobe.reader.rna.9635.1f7\ncom.adobe.reader.rna.9641.1f7\ncom.apple.launchd.3p4NpYziwC\ncom.apple.launchd.I7npyPRGFr\ncom.apple.launchd.XQI79eZ57B\ncom.apple.launchd.cStuiclSpB\ncom.apple.launchd.duNRp9uzhM\ncom.apple.launchd.rUIihXbdjO\nelectron-api-demos\nmeraki_wifi_loc.log\ntmux-503\n\n/var/tmp:\ncom.cleverfiles.cfbackd.chief\ncom.cleverfiles.cfbackd.pid\ndataFolder\nfilesystemui.socket\ngraphStudioSystemData\niTerm2.socket.586\nkernel_panics\nloadingData\n"
}
```
