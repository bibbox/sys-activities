git clone https://github.com/bibbox/sys-activities.git 

git pull

git add .
git commit -m "update from development server"
git push -u origin master

git remote add origin https://github.com/bibbox/sys-activities.git 

http://127.0.0.1:8050/activities/api/v1.0/activities
http://127.0.0.1:5000/activities/api/v1.0/activities
