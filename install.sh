#!/bin/bash

echo "Create Data Folder and copy phyton source"
echo ""

folder="/yourpath/without/slash/at/the/end"


PROGNAME=$(basename $0)

usage()
{
    echo "Usage:    ./install.sh [OPTIONS]"
    echo "          ./install.sh [ --help | -v | --version ]"
    echo ""
    echo "OPTIONS:"
    echo "      -f, --folder                  Base Data Folder"
    echo ""
    echo "Example:"
    echo "      ./install.sh -f /yourpath/without/slash/at/the/end  -p 10080"
    echo ""
}

version()
{
  echo "Version: 1.0"
  echo "Build: 2016-10-24"
}

clean_up() {	
	exit $1
}

error_exit()
{
	echo "ERROR in ${PROGNAME}: ${1:-"Unknown Error"}" 1>&2
	clean_up 1
}

createFolders()
{
    mkdir -p "$folder/sys/sys-activities/app/activities"
    mkdir -p "$folder/sys/sys-activities/redis/data"
    mkdir -p "$folder/sys/sys-activities/orientdb"
    mkdir -p "$folder/sys/sys-activities/orientdb/config"
    

}

copyInitFiles()
{
    if [[ ! -d  $folder/sys/sys-activities/app/activities/app ]]; then
        cp src/app   $folder/sys/sys-activities/app/activities
    fi
    
    COPY orientDB confif "$folder/sys/sys-activities/orientdb/config"
    
}

checkParameters() 
{
    echo "Setup parameters:"
    
    if [[ "$folder" = "/yourpath/without/slash/at/the/end" ]]; then
        usage
        error_exit "No Data Folder set, use the -f option"
    else
        echo "Data Folder: $folder" 
    fi
    
    if [[ -z "$port" ]]; then
        usage
        error_exit "The port is not set."
    else
        echo "Port: $port"
    fi       
}


while [ "$1" != "" ]; do
    case $1 in
        -f | --folder )         shift
                                folder=$1
                                ;;
        -h | --help )           usage
                                clean_up
                                ;;
        -v | --version | version )  version
                                clean_up
                                ;;
        * )                     usage
                                error_exit "Parameters not matching"
    esac
    shift
done

echo "Patch Docker Compose File and Create Data Folder for MySQL and Webtrees"
echo ""

checkParameters
createFolders
copyInitFiles

echo ''
echo 'run docker-compose up -d'
echo ""
