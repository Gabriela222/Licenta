################################################################################
#
# Mihai I. - 2019
# Description : Retrieve the ceilometer information regarding the VNF's
#
################################################################################

import ceilometerclient.client                                                  #pip install ceilometerclient

cclient = ceilometerclient.client.get_client(VERSION, os_username=USERNAME,
        os_password=PASSWORD, os_tenant_name=PROJECT_NAME, os_auth_url=AUTH_URL)
                                                                                #VERSION = 2
                                                                                #OS_USERNAME = admin
                                                                                #OS_PASSWORD = ADMIN_PASSWORD this is set during the OpenStack Installation
                                                                                #OS_TENANT_NAME = PROJECT_NAME this is the name of the project
                                                                                #OS_AUTH_URL = http://controller:35357/v3

cclient.meters.list()                                                           #it retreive all the meters from the OpenStack CeilometerDB using the ceilometerclient-API
ccl ient.new_samples.list()
