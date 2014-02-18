#!/usr/bin/env python
#
# Copyright 2013 Rodrigo Ancavil del Pino
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# -*- coding: utf-8 -*-

import json
#import urllib2
import httplib

data = {"uid": "12312873612783618"}
#req = urllib2.Request('http://0.0.0.0:8080/servers')
#req.add_header('Content-Type', 'application/json')

#response = urllib2.urlopen(req, json.dumps(data))

#print response


#data = {"somekey": 12}
#headers = {"Content-type": "application/json", "Accept": "text/plain"}
headers = {"Content-type": "application/json", "Accept": "text/plain"}
conn = httplib.HTTPConnection('127.0.0.1', 8880)
conn.request("POST", "/v1/users", json.dumps(data), headers)
response = conn.getresponse()

print response.status, response.reason

data = response.read()
print data
