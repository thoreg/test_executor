#!/bin/bash
#
easy_install readline
pip install -r requirements
#
pyenv activate profitbricks

#
# Start the Redis service on your host
$ sudo service redis-server start
#
# Check if Redis is up and accepting connections
$ redis-cli ping
PONG


cd /home/thoreg/projects/profitbricks/pb
celery -A pb worker -l info
