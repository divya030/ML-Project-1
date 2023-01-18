##  machine_learning_project

### Software and Account Requiremnets 

1. [Github Account](https://github.com/login)
2. [Heroku Account](https://www.heroku.com)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/git)

To create conda env 

conda create -p venv python==3.7 -y

To activate conda

conda activate venv/
`````
conda init cmd.exe
``````
To add files in github directly

git add <file_name>
git add.
`````
To see the status 

git status
``````
To ignore file or folder from git 

.gitignore <file>
`````
To check all versions maintained by git

git log
``````
To create version/commit all changes by git

git commit -m "message"
`````
To send versions/changes to git

git push origin main 

main -- branch name

In origin --- the complete github url is stored 
"https://github.com/divya030/machine_learning_project.git"
`````
To check the url in origin

git remote -v
`````
To check the branch name 

git branch
````
To undo changes 

git rollback
````
To check the status of any file 

git diff

+ -- if any lines are added
- -- if any lines are deleted
`````


To Setup CI/CD pipeline in heroku

1. Heroku Email_id 
2. Heroku API key 
3. Heroku APP name 

BUILD DOCKER IMAGE
````
docker build -t <image_name>:<tagname> .

> Note: Image name for docker must be lowercase 
````
To list docker images 

docker images
````
Run docker image 

docker run -p 5000:5000 -e PORT=5000 <image id>
````
To check running container in docker 

docker ps 
````
To stop docker container 

docker stop <container id>
````



````
python setup.py install 
````