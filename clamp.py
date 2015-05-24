#!/usr/bin/python


import json, argparse, os, sys
import re



parser = argparse.ArgumentParser(description='CLAMP')
parser.add_argument('--set', help="Create a new command")
parser.add_argument('--list', action="store_true", help="List commands")
parser.add_argument('command', nargs=argparse.REMAINDER)
args = parser.parse_args()


def get_vars(searchstr):
    sub = re.compile('\$\((\-\w+)=?(\w*)\)')
    subvars = sub.findall(searchstr)
    return subvars

def var_replace(subvars, args, searchstr):
    sub = re.compile('\$\(\-\w+=?\w*\)')
    
    for s in subvars:
        replstr = ""
        if s[1]:
            replstr = '$(%s=%s)'%s
        else:
            replstr = '$(%s)'%s[0]
        arg = None
        try:
            arg = args[s[0].split('-')[1]]
        except:
            pass
        searchstr = searchstr.replace(replstr, arg if arg else s[1])
    return searchstr




if args.set:
    commands = {}
    try:
        with open(".clamp") as f:
            commands = json.load(f)
    except:
        pass
    #Create a new command
    command = ' '.join(args.command[1:])
    commands[args.set] = command
    with open(".clamp", "w") as f:
        f.write(json.dumps(commands))
elif args.list:
    commands = {}
    try:
        with open(".clamp") as f:
            commands = json.load(f)
    except:
        pass
    for c in commands:
        print "%s : %s"%(c, commands[c])
elif args.command:
    #Look for an existing command to run

    commands = {}
    with open(".clamp") as f:
        commands = json.load(f)
    if args.command[0] in commands:
        command = commands[args.command[0]]
        parser = argparse.ArgumentParser(description=args.command[0])
        cmd_args = get_vars(command)
        for a in cmd_args:
            parser.add_argument(a[0], default=a[1], required=False if a[1] else True)
        sys.argv.pop(0)
        args = parser.parse_args()

        command = var_replace(cmd_args, vars(args), command)
        
        os.system(command)
