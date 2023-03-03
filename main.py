import pkg_resources
import subprocess

from sys import executable

if __name__ == '__main__':
    # Make sure pygame installed
    required = {'pygame'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        python = executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

    import solver
