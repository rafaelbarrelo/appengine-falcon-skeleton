#!/bin/bash
set -e  # If occur any error, exit

function to_console {
    echo -e "\n*** $1 ***\n"
}

cd $(dirname $0)

to_console "Activating virtualenv"
source backend/venv/bin/activate

to_console "Deploying on AppEngine Local Server"
appcfg.py update backend/appengine --oauth2