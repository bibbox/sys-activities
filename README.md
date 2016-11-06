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
### Activity JSON data structure

```json
  {
    "id": 1,
    "name": "Name of the activity, specified by the owner of the task",
    "type": "INSTALLAPP | UPDATEAPP | DELETEAPP | BACKUPAPP",
    "user_id": 8776,
    "user_name": "Name of the user issued the task / job", 
    "start_time" : "start time in javascript format",  
    "finished_time":  "finisched time in javascript format, empty string when still running",
    "state" : "RUNNING | FINISHED | PAUSED",
    "result" : "SUCCESS | ERROR | UNKNOWN"
  }
```


### GET /activities
`GET http://sys-activities.demo.bibbox.com/activities/api/v1.0/activities`

URL Parameter | Default | Description
--------- | ------- | -----------
include_finished | false | If set to true, the result will also include finished activities
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
### POST /activities
`POST http://sys-activities.demo.bibbox.com/activities/api/v1.0/activities`

### GET /activities/[id]
`GET http://sys-activities.demo.bibbox.com/activities/api/v1.0/activities/[id]`

### PUT /activities/[id]
`PUT http://sys-activities.demo.bibbox.com/activities/api/v1.0/activities/[id]`

### DELETE /activities/[id]
`DELETE http://sys-activities.demo.bibbox.com/activities/api/v1.0/activities/[id]`
