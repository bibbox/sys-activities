# SYS-ACTIVITIES SERVICE

Microservie for activity management in the BIBBOX framework.  First an activity logbook is impelemented. 

## Docker Images Used
 * [phyton server running flask]
 * [redis]
 * [busybox](https://hub.docker.com/_/busybox/), offical data container

## INSTALL
#### run install.sh 

## Mounted Volumes

* the phyton APP folder _/app/activities_  will be mounted to _/yourlocalpath/sys-activities/app/activities_
* the redis datafolder _/var/lib/redis/data_  will be mounted to _/yourlocalpath/sys-activities/redis/data_ 


## APIs

### GET activities

`GET http://sys-activities.demo.bibbox.com/activities/api/v1.0/activities`


URL Parameter | Default | Description
--------- | ------- | -----------
include_finished | false | If set to true, the result will also include finised activities
user_id  |   | If user_id is set, only activities started by the user are shown


```json
[
  {
    "id": 1,
    "name": "Install app-openspecimen at sample-manegement.demo.bibbox.com",
    "type": "INSTALLAPP",
    "user_id": 8776,
    "user_name": "Robert", 
    "start_time" : "2016-04-23T18:25:43.511Z",  
    "finished_time": "",
    "state" : "RUNNING",
    "result" : ""
  },
  {
    "id": 2,
    "name": "Install app-phenotips at phenotips.demo.bibbox.com",
    "type": "INSTALLAPP",
    "user_id": 8772,
    "user_name": "Lukas", 
    "start_time" : "2016-04-22T18:25:43.511Z",  
    "finished_time": "2016-04-22T18:29:43.511Z",  
    "state" : "FINISHED",
    "result" : "SUCCESS"
  }
]
```


