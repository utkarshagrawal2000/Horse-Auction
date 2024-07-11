# Horse-Auction
Horse Auction


## Features

- User Registration and Login
- User Authentication with JWT
- Horse Listing page
- Horse Detail and Bidding page 
- RESTful API for frontend interaction
- CSRF protection

### Rationale

I've used Django Rest Framework (DRF) to create APIs and AJAX to consume them within Django templates for demonstration purposes. However, for production, I plan to use React for the frontend. Alternatively, if I opt for a Django-based frontend, I'll directly pass data using Django's context instead of relying on APIs.


### How to run the application.

Step 1:

* Clone the application to your local machine
 ```
clone https://github.com/utkarshagrawal2000/Horse-Auction
```
* Go into Auction directory in Horseauction

Step 2:

* Create a virtual environment:

``` 
python -m venv venv
source venv/bin/activate   # On Windows use ./venv/Scripts/activate
```
<br>

Step 3:
* Install the dependencies from the requirements file

```
pip install -r requirements.txt
```
<br>

Step 4:

run the following commands:

```
python manage.py collectstatic
python manage.py runserver
```

*Access the application:
<br>
[http://127.0.0.1:8000](http://127.0.0.1:8000)

Importing Postman Collection

- Open Postman.
- Click on Import in the top left corner.
- Select the Auction.postman_collection.json file from your file system.
- The collection will be imported, and you can view and test the API endpoints.


*API details
To register the user with parameters(email,username,password) :
<br>
[http://127.0.0.1:8000/api/register/](http://127.0.0.1:8000/api/register/)

To login the user with parameters(username and password) :
<br>
[http://127.0.0.1:8000/api/token/](http://127.0.0.1:8000/api/token/)


To get the horses data use the api:
<br>
[http://127.0.0.1:8000/api/horses/](http://127.0.0.1:8000/api/horses/)
<br>
To get Particular horse detail data :
<br>
[http://127.0.0.1:8000/api/horse/1](http://127.0.0.1:8000/api/horse/1)

To retrieves particular horse bid history :
<br>
[http://127.0.0.1:8000/api/bids?horse_id=1](http://127.0.0.1:8000/api/bids?horse_id=1)

To retrieves other live bids excluding current horse bid:
<br>
[http://127.0.0.1:8000/api/live-auctions?horse_id=2](http://127.0.0.1:8000/api/live-auctions?horse_id=2)

To bid on a horse:
<br>
[http://127.0.0.1:8000/api/bids_create/](http://127.0.0.1:8000/api/bids_create/)

Bid detail of a horse:
<br>
[http://127.0.0.1:8000/api/bids_detail/1](http://127.0.0.1:8000/api/bids_detail/1)
<br>




