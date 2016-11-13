#!/bin/bash
PROGNAME=$(basename $0)
echo 'Install BIBBOX SYS-ACTIVITIES Microservice'
echo '-  Create data folder for redis and orientDB'

mkdir -p data/redis/data
mkdir -p data/orientdb/config
mkdir -p data/orientdb/databases
mkdir -p data/orientdb/backup

if  [[ ! -f data/orientdb/config ]]; then
        echo '-- Copy orientDB config file'
        cp config/orientdb-server-config.xml  data/orientdb/config
        cp config/security.json  data/orientdb/config
        echo '-- Copy orientDB default DB'
        cp -R config/orientdbdatabases/*  data/orientdb/databases/
fi
echo '-- orientDB db     = activities-v1'
echo '-- orientDB rootpw = bibbox4ever'
echo '-- orientDB user   = bibboxadmin / bibbox4ever'
echo '-- redis    db0pw  = bibbox4ever'
echo '-  Finished'
echo 'run docker-compose up -d'