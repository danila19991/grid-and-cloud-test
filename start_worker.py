import subprocess

if __name__ == '__main__':
    res = subprocess.run(['celery', 'worker',
                          '-A', 'remoteexperements',
                          '--loglevel=info', '--concurrency=4'],
                         stdout=subprocess.PIPE)
    print('rabbitmq docker:')
    print(res.stdout)
