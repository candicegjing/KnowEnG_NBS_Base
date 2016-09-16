import socket
import os


# simple program that distributes 'compute' function' to each node running 'dispynode'
def main():
    host = socket.gethostname()
    print("In compute function on host {}\n".format(host))
    #dir_to_write = "/mnt/backup/users/jingge/distributed_computing/tmp/"
    dir_to_write = "/workspace/backup/distributed_computing/tmp/"
    if not os.path.exists(dir_to_write):
        os.makedirs(dir_to_write, mode=0o755, exist_ok=True)
    f = open(dir_to_write+"test", 'w')
    f.write("Knoweng testing on {}..... \n".format(host))
    f.close()

if __name__ == '__main__':
    main()