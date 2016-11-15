# SYS-ACTIVITIES SERVICE
Microservice for activity management in the BIBBOX framework. First an activity logbook is impelemented. 

## Docker Images Used
 * phyton server running flask
 * [redis](https://hub.docker.com/_/redis/), offical redis container
 * [busybox](https://hub.docker.com/_/busybox/), offical data container

## INSTALL
#### run install.sh 

## Mounted Volumes
* the phyton APP folder _/app/activities_  will be mounted to _/yourlocalpath/sys-activities/app/activities_
* the redis datafolder _/var/lib/redis/data_  will be mounted to _/yourlocalpath/sys-activities/redis/data_ 

## APIs

### POST /activities
`POST http://activities.development.bibbox.org/activities/api/v1.0/activities`

Generate an activity

```json
  {
    "name": "Name of the activity, specified by the owner of the task",
    "type": "INSTALLAPP | UPDATEAPP | DELETEAPP | BACKUPAPP",
    "user_id": 8776,
    "user_name": "Name of the user issued the task / job", 
    "start_time" : "start time in javascript format",  
    "finished_time":  "finished time in javascript format, empty string when still running",
    "state" : "RUNNING | FINISHED | PAUSED",
    "result" : "SUCCESS | ERROR | UNKNOWN"
  }
```


### GET /activities
`GET http://activities.development.bibbox.org/activities/api/v1.0/activities`

URL Parameter | Default | Description
--------- | ------- | -----------
finished | false    | If set to true, the result will also include finished activities
limit    |          | return a maximum of _limit_ entries
offset   |          | skip the first _offset_ entries


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

### GET /activities/[id]
`GET http://activities.development.bibbox.org/activities/api/v1.0/activities/[id]`

Get a specific activity. 

### PUT /activities/[id]
`PUT http://activities.development.bibbox.org/activities/api/v1.0/activities/[id]`

Update some fields in an activity. 

####  Body payload in JSON FORMAT
```json
  {
    "finished_time":  "2016-04-22T18:29:43.511Z",
    "state" : "FINISHED",
    "result" : "ERROR"
  }
```
### DELETE /activities/[id]
`DELETE hhttp://activities.development.bibbox.org/activities/api/v1.0/activities/[id]`

Delete a specific activity, only used in development and debugging. 


### POST /activities/[id]/logs
`POST http://activities.development.bibbox.org/activities/api/v1.0/activities/[id]/logs`

Generate a log entry for the activiy

```json
  {
    "log-message": "Log Meassage, usaly a multiline string",
    "type" : "INFO | WARNING | ERROR "
  }
```

## GET /activities/[id]/logs
`GET http://activities.development.bibbox.org/activities/api/v1.0/activities/[id]/logs`

```json
[
  {
    "log-message": "Start Installation",
    "type" : "INFO"
  },
  {
    "log-message": "Unknown Critical Problem",
    "type" : "ERROR"
  }
]
```

URL Parameter | Default | Description
--------- | ------- | -----------
limit    |   | return a maximum of _limit_ entries
offset   |   | skip the first _offset_ entries
