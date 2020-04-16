# 5.NetDevOps

## Date
2020-04-16

## Agenda
* DevOps and NetDevOps
* Ansible Introduction

## Attendees
* Angus Ba
* Frank Tan
* Yixin Xing
* Yali Kai
* Yongli Chen
* Leo Cui
* Wenlong Zhao
* Haifeng Li
* House Liang

## Notes
* Hands-on:
    * Use ios_config module to add an ACL to target device. The ACL should be named as “{{device_hostname}}_acl”
    * Make sure there’s no ACL using the same ACL name
    * The ACL should allow traffic from network 10.1.1.0/24, 10.1.2.0/24 to any destination
    * Create role and playbook to finish this task
* Ansible Doc: https://docs.ansible.com/

![alt text](https://github.com/tqs0117/devnet_forum/blob/1st_forum/5.netdevops/devops_infinity.png "devops_infinity")


## References
* 


