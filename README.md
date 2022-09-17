# beprgama
A challenge of bepragma(formerly Logisy)

# Prequisities
1. Make sure [python 3.6+](https://www.python.org/downloads/) is installed on your system
2. Have installed [DB Browser for SQLite](https://sqlitebrowser.org/)
3. Any text editor like VSCode

## Getting Started

`pip install fastapi`

if you have both python 2 and 3 installed on your device

`pip3 install fastapi`

The file structure is like
```
 pragma
   * -main.py -- a main script which have routes to run product at [**/products**] path
   * -model.py -- a script containing models and database initialization
   * -order.py -- a script to do CRUD operations for order
   * -product.py -- a script to create product
  ```

Open **model.py** file and **Run** it- This will create databases and required tables in it.

Now, to see the app running, let's install **uvicorn** which is an ASGI server.

`pip install uvicorn`

or

`pip3 install uvicorn`


Run the app:

`uvicorn main:app --reload`

The server gets started and can be accessed at:
`http://127.0.0.1:8000/`

The uvicorn is ASGI server to run the python scripts


You can very easily test the APIs running with **Swagger UI** that comes up with fast api and can be accessed at
`http://127.0.0.1:8000/docs#`

# Start creating products

```
In swagger UI Createproducts
pass below request body, no need to pass id as it's auto generated at backend

{
  "name": "Ball",
  "price": 20
}

```

After products are created you can test crud on **Order** at **/orders**

alternatively it can be accessed from swagger UI itself.

**Happy Coding**

Please write to me at **dipakshah401@gmail.com** for any queries 😊.





