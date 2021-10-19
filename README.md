# Hashtag Machine Test
This is machine test of Hashtag systems. Used Django rest framework and JWT.

- Clone The project :- https://github.com/AthifSaheer/hashtag-machine-test

### Built With

* Backend - `Django Rest Framework`

<!-- GETTING STARTED -->
## Getting Started

If you would love to run this project on your local env I will walk you through:

### Installation

1. Create virutal environment
   ```sh
   virtualenv venv
   ```
   
2. Activate virtualenv
   ```sh
   source venv/bin/activate
   ```
   
3. Clone the repo
   ```sh
   https://github.com/AthifSaheer/hashtag-machine-test
   ```
   
4. Install requirements.txt
   ```sh
   pip install -r requirements.txt
   ```
   
5. Run Project: <br>
   go to the project folder where manage.py file is present
   ```sh
   python manage.py migrate
   python manage.py runserver
   ```

### Check apis

Go to lading page then you can see overview of all apis.

1. Create an account(format👇)
   ```sh
    {
        "username" : "username",
        "email" : "email@gmail.com",
        "password" : "12345678"
    }
   ```
2. Login (format👇)
   ```sh
    {
        "username" : "username",
        "password" : "12345678"
    }
   ```
3. Create an order with products. You can send multiple products ID (format👇)
    ```sh
    {
        "user" : "username",
        "products" : 1 or [1, 2, 3]
    }
   ```
4. Transact an amount(format👇)
    ```sh
    {
        "user" : "username",
        "order" : orderID,
        "amount": amount
    }
   ```
