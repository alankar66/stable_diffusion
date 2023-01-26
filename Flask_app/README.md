<b> Finding face embedding from dlib 128 dim vector, saving the embedding in database and finding similarity between images using from database using euclidean distance</b><br><br>

<b> 1. Clone the repository<br>
  git clone https://github.com/alankar66/Face_embeddings_postgresql.git</b><br>

<b> 2. Install the requirement file</b><br>
     pip install -r requirements.txt<br>

<b> 3. Create a table in Postgresql database:-</b><br>

create table image_embedding(<br>
id serial,<br>
img_name varchar(150),<br>
img_ref varchar(150),	<br>
embd1 cube,<br>
embd2 cube<br>	
);
<br><br>

<b> 4. Install any one server redis (sudo apt-get install redis) or rabbitmq (sudo apt-get install rabbitmq-server)</b>
<br><br>
<b> 5. Run the server by executing (redis-server) if reddis OR (sudo rabbitmq-server) if rabbitmq
<br><br>
<b> 5. Run the app.py file </b> (First change your postgresql configuration in app.py & files.py in 'Database()' function)
<br><br>
<b> 6. Run-->  celery -A app.celery worker --loglevel=info
<br> to see the background task performance</b>    

<b>Image add api-->  {request-POST,  URL : http://127.0.0.1:5000/add_img_api}
<br>                 Body - {content_type - multipart/form-data, field_name: file, url of image}
