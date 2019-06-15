## Description
  The src/ directory contains exclusively the Python3.7 code for interaction with
 the ceilometer-API.

## High Level Architecture

Figure 1. High Level Design of the e2e solution
![Imgur](https://i.imgur.com/SFhbpyy.jpg)

## Target implementation
  Using the OpenStack-Ceilometer project [1] retrieve all the information on an deployed VNF into an
MYSQLdb and expose all the metrics to a web-interface.
  The interrogation of the metrics from the web-interface is performed each time the user is pressing a
specific "retrieve" button.


## Documentation

[1] https://docs.openstack.org/ceilometer/latest/
