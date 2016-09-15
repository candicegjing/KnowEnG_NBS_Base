** Launch a chronos job:
```
curl -L -H 'Content-Type: application/json' -X POST -d '{"async": true,"command": "python3 /mnt/knowstorage/jingge/distributed_computing/simplified.py","epsilon": "PT30M","errorCount": 0,"lastError": "","schedule": "R/2016-09-12T21:05:00.000Z/PT24H","name": "jingge_testing","owner": "jingge2@illinois.edu","retries": 2,"successCount": 10}' knowcluster01.dyndns.org:4400/scheduler/iso8601
```

** Example result:
```
Received SUBSCRIBED event
Subscribed executor on knowcluster06.dyndns.org
Received LAUNCH event
Starting task ct:1473868380675:1:jingge_testing:
/usr/libexec/mesos/mesos-containerizer launch --command="{"environment":{"variables":[{"name":"mesos_task_id","value":"ct:1473868380675:1:jingge_testing:"},{"name":"CHRONOS_JOB_OWNER","value":"jingge2@illinois.edu"},{"name":"CHRONOS_JOB_NAME","value":"jingge_testing"},{"name":"HOST","value":"knowcluster06.dyndns.org"},{"name":"CHRONOS_RESOURCE_MEM","value":"128.0"},{"name":"CHRONOS_RESOURCE_CPU","value":"0.1"},{"name":"CHRONOS_RESOURCE_DISK","value":"256.0"}]},"shell":true,"user":"root","value":"python3 \/mnt\/knowstorage\/jingge\/distributed_computing\/simplified.py"}" --help="false" --unshare_namespace_mnt="false"
Forked command at 28163
2016-09-14 15:52:37 asyncoro - version 4.2.2 with epoll I/O notifier
2016-09-14 15:52:37 dispy - Storing fault recovery information in "_dispy_20160914155237"
knowcluster04.dyndns.org executed job 0 at 1473868442.1397698 with 7
knowcluster04.dyndns.org executed job 1 at 1473868442.1417158 with 20
knowcluster04.dyndns.org executed job 2 at 1473868442.144034 with 13

                           Node |  CPUs |    Jobs |    Sec/Job | Node Time Sec
------------------------------------------------------------------------------
 192.17.176.157 (knowcluster04. |    16 |       3 |      0.004 |         0.013

Total job time: 0.013 sec, wall time: 0.040 sec, speedup: 0.328

Command exited with status 0 (pid: 28163)
```