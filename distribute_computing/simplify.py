import dispy, random
import socket
import os


# simple program that distributes 'compute' function' to each node running 'dispynode'
def compute(n):
    host = socket.gethostname()
    print("In compute function with number = {}, on host {}\n".format(str(n), host))
    dir_to_write = "/mnt/backup/users/jingge/distributed_computing/tmp/"
    if not os.path.exists(dir_to_write):
        os.makedirs(dir_to_write, mode=0o755, exist_ok=True)
    f = open(dir_to_write+"test", 'w')
    f.write("Knoweng testing..... \n")
    f.close()
    return (host, n)

if __name__ == '__main__':
    nodelist = ['192.17.176.151','192.17.176.158','192.17.176.156','192.17.176.161','192.17.176.152']
#    nodelist = ['192.17.176.*']
    cluster = dispy.JobCluster(compute, nodes=nodelist)
    jobs = []
    for i in range(5):
        # schedule execution of 'compute' on a node (running 'dispynode')
        # with a parameter (random number in this case)
        job = cluster.submit(random.randint(5,20))
        job.id = i # optionally associate an ID to job (if needed later)
        jobs.append(job)
    # cluster.wait() # wait for all scheduled jobs to finish
    for job in jobs:
        host, n = job() # waits for job to finish and returns results
        print('%s executed job %s at %s with %s' % (host, job.id, job.start_time, n))
        # other fields of 'job' that may be useful:
        print(job.stdout, job.stderr, job.exception, job.ip_addr, job.start_time, job.end_time)
    cluster.print_status()