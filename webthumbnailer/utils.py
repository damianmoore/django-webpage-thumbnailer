from hashlib import sha1
from subprocess import Popen, PIPE, STDOUT


def run_cmd(cmd):                                                               
    p = Popen(cmd.split(' '), stdout=PIPE, stdin=PIPE, stderr=PIPE)             
    return p.communicate()[0]

def make_hash(data):
    m = sha1()
    m.update(data)
    return m.hexdigest()
