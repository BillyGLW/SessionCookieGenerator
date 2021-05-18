import os
import subprocess

import argparse


def parse():
    parser = argparse.ArgumentParser(description='docker cleanup')
    parser.add_argument('--kill_volumes', type=int,
                        default=1, help='prune volumes')
    parser.add_argument('--kill_containers', type=int,
                        default=1, help='remove all running containers')
    parser.add_argument('--mode', type=int, default=1,
                        help='from file or by automatic search')
    parser.add_argument('--unused', type=int, default=1,
                        help='unused system space')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse()

    if args.unused:
        if args.kill_containers:
            cc = 'docker container ls -q'
            proc = subprocess.Popen(cc, stdout=subprocess.PIPE, shell=True)
            cc_val = str(proc.stdout.read(), 'utf-8').split()
            for _ in cc_val:
                os.system('docker rm --force %s' % _)
        cmd = 'docker rm'
        if args.mode:
            nonfile = 'docker ps -a -q -f status=exited > toremove'
            os.system(nonfile)

        with open('toremove', 'r') as f:
            _ = f.read().split()
        for cc in _:
            os.system('{} {}'.format(cmd, cc))

        if args.kill_volumes:
            '''
            prune volume using docker volume prune
            needed to control stdin, because user agreement needed
            '''
            cc = 'docker volume prune'
            proc = subprocess.Popen(
                cc, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            stdout_data = proc.communicate(input=b'y')[0]
