# clamp
CLI Alias tool with variable substitution

This tool allows you to bind a string to a CLI command. It also allows for
variable that are passed as cli parameters. This is really handy for testing
an HTTP API by wrapping curl commands, for example:

```
$ clamp --set listusers -- 'curl http://localhost:$(-p=3000)/users'
```

This will create a new clamp command called "listusers" that can accept a
parameter "-p" for the port, although a default of 3000 is provided.

```
$ clamp listusers
[{"id":1,"created_at":"2015-05-28T16:39:52.178Z","updated_at":"2015-05-28T16:39:52.178Z","name":"Eric"}]
```

##Clamp options
```
$ clamp -h
usage: clamp [-h] [--set SET] [--list] [--delete DELETE] ...

CLAMP

positional arguments:
  command

optional arguments:
  -h, --help       show this help message and exit
  --set SET        Create a new command
  --list           List commands
  --delete DELETE  Delete command
```

Clamp will even show the usage for the commands you create, though it needs improvement:

```
$ clamp listusers --help
usage: clamp [-h] [-p P]

listusers

optional arguments:
  -h, --help  show this help message and exit
  -p P
```

##.clamp files
Clamp will create a file in the current directory called .clamp where it will
store the command alias. This allows you to create different clamp files for
different projects.
