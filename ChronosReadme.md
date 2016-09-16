## Chronos link (http://knowcluster01.dyndns.org:4400/#)
## Mesos link (http://knowcluster01.dyndns.org:5050/#/)

## Launch a chronos job:
```
curl -L -H 'Content-Type: application/json' -X POST -d '{"async": true,"command": "python3 /mnt/knowstorage/jingge/distributed_computing/simplified.py","epsilon": "PT30M","errorCount": 0,"lastError": "","schedule": "R/2016-09-12T21:05:00.000Z/PT24H","name": "jingge_testing","owner": "jingge2@illinois.edu","retries": 2,"successCount": 10}' knowcluster01.dyndns.org:4400/scheduler/iso8601
```

## Example result:
 * Run on Cloud9
```
Received SUBSCRIBED event
Subscribed executor on knowcluster03.dyndns.org
Received LAUNCH event
Starting task ct:1473968940000:0:jingge_testing:
/usr/libexec/mesos/mesos-containerizer launch --command="{"environment":{"variables":[{"name":"mesos_task_id","value":"ct:1473968940000:0:jingge_testing:"},{"name":"CHRONOS_JOB_OWNER","value":"jingge2@illinois.edu"},{"name":"CHRONOS_JOB_NAME","value":"jingge_testing"},{"name":"HOST","value":"knowcluster03.dyndns.org"},{"name":"CHRONOS_RESOURCE_MEM","value":"128.0"},{"name":"CHRONOS_RESOURCE_CPU","value":"0.1"},{"name":"CHRONOS_RESOURCE_DISK","value":"256.0"}]},"shell":true,"user":"root","value":"python3 \/mnt\/backup\/users\/jingge\/distributed_computing\/simplified.py"}" --help="false" --unshare_namespace_mnt="false"
Forked command at 29215
2016-09-15 19:50:54 asyncoro - version 4.2.2 with epoll I/O notifier
2016-09-15 19:50:54 dispy - Storing fault recovery information in "_dispy_20160915195054"
knowcluster04.dyndns.org executed job 0 at 1473969002.9278748 with 7
In compute function with number = 7, on host knowcluster04.dyndns.org
  None 192.17.176.157 1473969002.9278748 1473969002.9349637
knowcluster04.dyndns.org executed job 1 at 1473969002.9374275 with 12
In compute function with number = 12, on host knowcluster04.dyndns.org
  None 192.17.176.157 1473969002.9374275 1473969002.9410896
knowcluster04.dyndns.org executed job 2 at 1473969002.9278278 with 16
In compute function with number = 16, on host knowcluster04.dyndns.org
  None 192.17.176.157 1473969002.9278278 1473969002.9324195
knowcluster04.dyndns.org executed job 3 at 1473969002.9314284 with 9
In compute function with number = 9, on host knowcluster04.dyndns.org
  None 192.17.176.157 1473969002.9314284 1473969002.9370959
knowcluster04.dyndns.org executed job 4 at 1473969002.9315076 with 13
In compute function with number = 13, on host knowcluster04.dyndns.org
  None 192.17.176.157 1473969002.9315076 1473969002.935683

                           Node |  CPUs |    Jobs |    Sec/Job | Node Time Sec
------------------------------------------------------------------------------
 192.17.176.157 (knowcluster04. |    16 |       5 |      0.005 |         0.025

Total job time: 0.025 sec, wall time: 0.037 sec, speedup: 0.684

Command exited with status 0 (pid: 29215)
```

 * Multiple nodes assigned to the job
```
Received SUBSCRIBED event
Subscribed executor on knowcluster02.dyndns.org
Received LAUNCH event
Starting task ct:1473970320000:0:jingge_testing:
/usr/libexec/mesos/mesos-containerizer launch --command="{"environment":{"variables":[{"name":"mesos_task_id","value":"ct:1473970320000:0:jingge_testing:"},{"name":"CHRONOS_JOB_OWNER","value":"jingge2@illinois.edu"},{"name":"CHRONOS_JOB_NAME","value":"jingge_testing"},{"name":"HOST","value":"knowcluster02.dyndns.org"},{"name":"CHRONOS_RESOURCE_MEM","value":"128.0"},{"name":"CHRONOS_RESOURCE_CPU","value":"0.1"},{"name":"CHRONOS_RESOURCE_DISK","value":"256.0"}]},"shell":true,"user":"root","value":"python3 \/mnt\/backup\/users\/jingge\/distributed_computing\/simplified.py"}" --help="false" --unshare_namespace_mnt="false"
Forked command at 6585
2016-09-15 20:14:07 asyncoro - version 4.2.2 with epoll I/O notifier
2016-09-15 20:14:07 dispy - Storing fault recovery information in "_dispy_20160915201407"
knowcluster03.dyndns.org executed job 0 at 1473970558.208094 with 14
In compute function with number = 14, on host knowcluster03.dyndns.org

  None 192.17.176.158 1473970558.208094 1473970558.2130573
knowcluster03.dyndns.org executed job 1 at 1473970558.2108924 with 18
In compute function with number = 18, on host knowcluster03.dyndns.org

  None 192.17.176.158 1473970558.2108924 1473970558.21696
knowcluster03.dyndns.org executed job 2 at 1473970558.2108274 with 7
In compute function with number = 7, on host knowcluster03.dyndns.org

  None 192.17.176.158 1473970558.2108274 1473970558.2153037
knowcluster03.dyndns.org executed job 3 at 1473970558.2143285 with 20
In compute function with number = 20, on host knowcluster03.dyndns.org

  None 192.17.176.158 1473970558.2143285 1473970558.2241287
knowcluster03.dyndns.org executed job 4 at 1473970558.2157662 with 19
In compute function with number = 19, on host knowcluster03.dyndns.org

  None 192.17.176.158 1473970558.2157662 1473970558.222586

                           Node |  CPUs |    Jobs |    Sec/Job | Node Time Sec
------------------------------------------------------------------------------
 192.17.176.151 (knowcluster02. |    16 |       0 |      0.000 |         0.000
 192.17.176.152 (knowcluster06. |    24 |       0 |      0.000 |         0.000
 192.17.176.156 (knowcluster01. |    16 |       0 |      0.000 |         0.000
 192.17.176.158 (knowcluster03. |    16 |       5 |      0.006 |         0.032

Total job time: 0.032 sec, wall time: 0.217 sec, speedup: 0.148

Command exited with status 0 (pid: 6585)
```
 
 * Run on localhost
 ```
 

Received SUBSCRIBED event
Subscribed executor on knowcluster07.dyndns.org
Received LAUNCH event
Starting task ct:1474041420000:0:jingge_localhost:
/usr/libexec/mesos/mesos-containerizer launch --command="{"environment":{"variables":[{"name":"mesos_task_id","value":"ct:1474041420000:0:jingge_localhost:"},{"name":"CHRONOS_JOB_OWNER","value":"jingge2@illinois.edu"},{"name":"CHRONOS_JOB_NAME","value":"jingge_localhost"},{"name":"HOST","value":"knowcluster07.dyndns.org"},{"name":"CHRONOS_RESOURCE_MEM","value":"128.0"},{"name":"CHRONOS_RESOURCE_CPU","value":"0.1"},{"name":"CHRONOS_RESOURCE_DISK","value":"256.0"}]},"shell":true,"user":"root","value":"python3 \/mnt\/backup\/users\/jingge\/distributed_computing\/simplified.py"}" --help="false" --unshare_namespace_mnt="false"
Forked command at 14154
2016-09-16 15:56:48 asyncoro - version 4.2.2 with epoll I/O notifier
2016-09-16 15:56:48 dispy - Storing fault recovery information in "_dispy_20160916155648"
knowcluster05.dyndns.org executed job 0 at 1474041415.1529186 with 11
In compute function with number = 11, on host knowcluster05.dyndns.org

  None 192.17.176.161 1474041415.1529186 1474041415.1575608
knowcluster02.dyndns.org executed job 1 at 1474041429.986635 with 16
In compute function with number = 16, on host knowcluster02.dyndns.org

  None 192.17.176.151 1474041429.986635 1474041429.991863
knowcluster01.dyndns.org executed job 2 at 1474041427.0966625 with 6
In compute function with number = 6, on host knowcluster01.dyndns.org

  None 192.17.176.156 1474041427.0966625 1474041427.1016147
knowcluster05.dyndns.org executed job 3 at 1474041415.1547046 with 13
In compute function with number = 13, on host knowcluster05.dyndns.org

  None 192.17.176.161 1474041415.1547046 1474041415.1597545
knowcluster02.dyndns.org executed job 4 at 1474041429.9865818 with 5
In compute function with number = 5, on host knowcluster02.dyndns.org

  None 192.17.176.151 1474041429.9865818 1474041429.9909887

                           Node |  CPUs |    Jobs |    Sec/Job | Node Time Sec
------------------------------------------------------------------------------
 192.17.176.158 (knowcluster03. |    16 |       0 |      0.000 |         0.000
 192.17.176.152 (knowcluster06. |    24 |       0 |      0.000 |         0.000
 192.17.176.161 (knowcluster05. |    16 |       2 |      0.005 |         0.010
 192.17.176.151 (knowcluster02. |    16 |       2 |      0.005 |         0.010
 192.17.176.156 (knowcluster01. |    16 |       1 |      0.005 |         0.005

Total job time: 0.024 sec, wall time: 0.209 sec, speedup: 0.116

Command exited with status 0 (pid: 14154)


 ```
 
## Kill a job
```
curl -L -X DELETE knowcluster01.dyndns.org:4400/scheduler/job/jingge_testing
```


## Knowcluster information
 * Mapping 
 
| Cluster localhost | Container env |
| ------------- | ------------- |
| /mnt/backup/users/jingge | /workspace/backup |
| /mnt/knowstorage/jingge/ | Doesn't apply |
 
 

 * Cluster IP address
 
|  Cluster Name | Cluster IP    |
| ------------- | ------------- |
| knowcluster01 |192.17.176.156 |
| knowcluster02 |192.17.176.151 |
| knowcluster03 |192.17.176.158 |
| knowcluster04 |192.17.176.157 |
| knowcluster05 |192.17.176.161 |
| knowcluster06 |192.17.176.152 |
| knowcluster07 |192.17.176.150 |
| knowcluster08 |192.17.176.181 |
 
 
 * Example Charles https://github.com/KnowEnG/KnowledgeEngine/blob/master/ML/docs/pipelines.rst