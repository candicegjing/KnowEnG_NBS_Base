# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 14:47:45 2016

@author: The Gene Sets Characterization dev team

"""


import time

def nmf(run_parameters):
    '''nmf clustering'''
    from knpackage.toolbox import run_nmf
    run_nmf(run_parameters) 

def cc_nmf(run_parameters):
    '''kmeans consensus clustering of the nmf-based clusters'''
    from knpackage.toolbox import run_cc_nmf
    start_time = time.time()
    num_of_process = 3
    run_cc_nmf(run_parameters, num_of_process)
    end_time = time.time()
    run_time = end_time - start_time
    output_file = open('time_check','a')
    output_file.write("Running time on parallelism % : % seconds" %(num_of_process, run_time))
    output_file.close()

def net_nmf(run_parameters):
    '''net-nmf clustering "'''
    from knpackage.toolbox import run_net_nmf
    run_net_nmf(run_parameters)

def cc_net_nmf(run_parameters):
    '''kmeans consensus clustering of the net-nmf-based clusters'''
    from knpackage.toolbox import run_cc_net_nmf
    run_cc_net_nmf(run_parameters)

SELECT = {
    "cluster_nmf":nmf,
    "cc_cluster_nmf":cc_nmf,
    "net_cluster_nmf":net_nmf,
    "cc_net_cluster_nmf":cc_net_nmf}

def main():
    import sys
    from knpackage.toolbox import get_run_directory_and_file
    from knpackage.toolbox import get_run_parameters

    
    run_directory, run_file = get_run_directory_and_file(sys.argv)
    run_parameters = get_run_parameters(run_directory, run_file)
    SELECT[run_parameters["method"]](run_parameters)

if __name__ == "__main__":
    main()
