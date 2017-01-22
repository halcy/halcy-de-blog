from fabric.api import *
import fabric.contrib.project as project
import os
import shutil
import sys
import SocketServer
from subprocess import call

from pelican.server import ComplexHTTPRequestHandler

# "production" path
dest_path = '/home/halcyon/www/blog'

# Local path configuration
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Port for `serve`
PORT = 8000

def clean():
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
        os.makedirs(DEPLOY_PATH)

def build():
    """Build local version of site"""
    local('pelican -s pelicanconf.py')

def rebuild():
    """`build` with the delete switch"""
    local('pelican -d -s pelicanconf.py')

def regenerate():
    """Automatically regenerate site upon file modification"""
    local('pelican -r -s pelicanconf.py')

def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(env.deploy_path)

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    """`build`, then `serve`"""
    build()
    serve()

def preview():
    """Build production version of site"""
    local('pelican -s publishconf.py')

def publish():
    """Publish to production via cp"""
    local('pelican -s publishconf.py')
    call([
		"rsync",
		"-r",
		"--delete",
		DEPLOY_PATH + '/',
		dest_path
	])
