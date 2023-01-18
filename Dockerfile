From python:3.7
COPY . /app   ## copying all files in this operating system (pyhton 3.7) in an app folder.
WORKDIR /app  ## setting working dir for the folder 
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app  
####  module:Flask_object (app:app)

