ZooKeeper Browser - Lite
========================

Required Modules
----------------
* zkpython
* web.py

Installing
----------
    sudo easy_install web.py
    Install zkpython from contrib folder of zookeeper distribution.

or

    sudo aptitude install python-webpy
    sudo aptitude install python-zookeeper

Running
-------
Export environment variable ZOOKEEPER to the zookeeper client endpoint and run project. If you do not set ZOOKEEPER variable, a default Zookeeper address will be tried. For example:

    export ZOOKEEPER=192.168.1.1:2181
    python code.py

Now point your browser to http://localhost:8080.

Also, you can set the port ZooKeeper Browser will run by:

    python code.py [port]

Screenshot
----------
![Sample Output](http://i.imgur.com/GS827.jpg)
