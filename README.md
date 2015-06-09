# clamp
CLI Alias tool with variable substitution

This tool allows you to bind a string to a CLI command. It also allows for
variable that are passed as cli parameters. This is really handy for testing
an HTTP API by wrapping curl commands, for example:

```
$ clamp --set listusers -- 'curl --silent -H "Content-type: application/json" http://localhost:$(-port=3000)/users | python -m json.tool'
```

This will create a new clamp command called "listusers" that can accept a
parameter "-port" for the port, although a default of 3000 is provided.

```
$ clamp listusers
[
    {
        "created_at": "2015-05-29T23:18:47.224Z",
        "email": "eric@example.com",
        "id": 8,
        "name": "Eric",
        "updated_at": "2015-05-29T23:18:47.224Z"
    },
    {
        "created_at": "2015-05-29T23:34:43.583Z",
        "email": "sdjf",
        "id": 9,
        "name": "akdfh",
        "updated_at": "2015-05-29T23:34:43.583Z"
    }
]
```

Slightly more complicated, be careful with your quotes...
```
$ clamp --set adduser -- 'curl -X POST -H "Content-type: application/json" -d '"'"'{"name":"$(-name)","email":"$(-email)"}'"'"' http://localhost:$(-port=3000)/users'
$ clamp adduser -name Eric -email eric@example.com
{"id":8,"name":"Eric","email":"eric@example.com","created_at":"2015-05-29T23:18:47.224Z","updated_at":"2015-05-29T23:18:47.224Z"}
```
If the quotes get tricky, use the -r option to read from stdin
```
$ clamp -r --set adduser
curl -X POST -H "Content-type: application/json" -d '{"name":"$(-name)","email":"$(-email)"}' http://localhost:$(-port=3000)/users
$ ./clamp --list
adduser:  'curl -X POST -H "Content-type: application/json" -d '"'"'{"name":"$(-name)","email":"$(-email)"}'"'"' http://localhost:$(-port=3000)/users'
$
```
##Clamp options
```
$ clamp -h
usage: clamp [-h] [--version] [--set SET] [-r] [--list] [-n] [--delete {}] ...

CLAMP

positional arguments:
  command      user defined command: {}

optional arguments:
  -h, --help   show this help message and exit
  --version    show program's version number and exit
  --set SET    Create a new command
  -r           Read command from stdin instead of command line, may be easier
               for quotes
  --list       List commands
  -n           Don't escape commands when listing
  --delete {}  Delete command

```

Clamp will even show the usage for the commands you create, though it needs improvement:

```
$ clamp listusers --help
usage: clamp [-h] [-port PORT]

listusers

optional arguments:
  -h, --help  show this help message and exit
  -port PORT
```

##.clamp files
Clamp will create a file in the current directory called .clamp where it will
store the command alias. This allows you to create different clamp files for
different projects.

##Install
```
$ sudo pip3 install git+https://github.com/seiferteric/clamp.git

# To enable command line completion

$ pip3 install argcomplete
$ activate-global-python-argcomplete3
```
Or build a Debian package (must have git-buildpackage installed)
```
$ ./clamp mk_deb
$ sudo dpkg -i ../clamp_<version>.deb
```

##TODO
 - Add input from STDIN for long text input
 - Fix tab completion for custom clamp commands.
 - Export command(s) as standalone scripts.
