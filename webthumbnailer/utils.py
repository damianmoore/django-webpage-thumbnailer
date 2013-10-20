from hashlib import sha1
from subprocess import Popen, PIPE


def run_cmd(cmd):
    try:
        p = Popen(cmd.split(' '), stdout=PIPE, stdin=PIPE, stderr=PIPE)
    except OSError, e:
        if e[0] == 2:
            raise OSError('\'%s\' is not installed' % cmd.split(' ')[0])
        else:
            raise e
    return p.communicate()[0]


def make_hash(data):
    m = sha1()
    m.update(data)
    return m.hexdigest()
