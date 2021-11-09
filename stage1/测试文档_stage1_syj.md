1.若在使用yum安装常用的软件时出现如下信息：
Loaded plugins: fastestmirror, refresh-packagekit, security

Loading mirror speeds from cached hostfile

Could not retrieve mirrorlist http://mirrorlist.centos.org/?release=6&arch=i386&repo=os error was

14: PYCURL ERROR 6 - "Couldn't resolve host 'mirrorlist.centos.org'"

Error: Cannot find a valid baseurl for repo: base

问题原因：
出现如下错误信息，是因为DNS配置错误。

解决方法： 
    在命令提示符中输入: vi  /etc/sysconfig/network-scripts/ifcfg-eth0
ONBOOT=yes
NM_CONTROLLED=no


设置好后，重新进行启动。 




2.安装完成后无法连接网络，使用yum无法正常安装软件报错could not resolve host: mirrorlist.centos.org等。
问题原因：centos系统的网络不通
解决方法：
1.进入网卡配置文件所在目录：# cd /etc/sysconfig/network-scripts/
2.编辑网卡配置文件（下图红框中的文件）：# vi ifcfg-ens33 (不用系统可能文件名不一样)



3.将文件中的最后一行的ONBOOT=no 改为ONBOOT=yes.
4.保存文件并退出vi，重启network：# service network restart



3.问题：error: command 'gcc' failed with exit status 1 on CentOS……

解决方法：https://stackoverflow.com/questions/19955775/error-command-gcc-failed-with-exit-status-1-on-centos



4.未解决的问题：执行./configure时出现,error,Missing libraries；unable to ptoceed.

安装了相关的所有库，而且换了文件夹进行编译还是不能成功。