# Parameterized-Remote-Shell-Execution-Service 
Execute File on Remote Machine with Parameterized Arguments through REST API Edit


## Install
make install

## Run in Debug Mode
make debug

## Run in Multithreaded Mode
make run

## Example

Command
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
}```
