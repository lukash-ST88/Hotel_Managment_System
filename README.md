
<h1> Hotel_Management_System </h1>

<h4> Application description</h4>
This project is a hotel management system, 
that allows authorized users to book, cancel and change rooms of three categories(cheep, standard, luxury). 
When a user defines data for checking in and checking out, system verifying if chosen room is free for this 
data by scanning all occupied data for this room.

<ui><h4>The functionality of the project includes:</h4></ui>
<li>allauth authentication system;</li>
<li>Possibility to choose a room's category</li>
<li>Possibility to choose suitable data for checking in and out</li>
<li>Possibility to cancel booked rooms </li>
<li>Possibility to view all booked rooms </li>

<ui><h4>Basic frameworks and libraries:</h4></ui>
<li>Django</li>
<li>allauth</li>
<li>psycopg2</li>
<li>pytest</li>
<li>redis-server

<h4>Screen of application</h4>


<h4>Steps to activate the project on linux machine:</h4>

<p>1. Clone git repository to your machine:</p>

```
git clone git@github.com:lukash-ST88/Hotel_Managment_System.git
```
<p>2. Create and activate virtual environment:</p>

```
python -m venv [name]
source [name]/bin/activate
```

<p>3. Install all requirements:</p>

```
pip install -r requirements.txt 
```

<p>4. Create .env file and fill it with your database and backend data:</p>

```
SECRET_KEY=some-secret-key

ALLOWED_HOSTS=127.0.0.1 localhost

POSTGRES_ENGINE=django-backend
POSTGRES_USER=user
POSTGRES_PASSWORD=pass
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_NAME=name
```


<p>5. Install [redis-server]](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-20-04) on linux machine and start it then:</p>

```
sudo service redis-server start
```

<p> 6. Migrate data to database:</p>

```
cd noncountries
python3 manage.py migrate
```
<p>7. Run the application:</p>

```
python3 manage.py runserver
```