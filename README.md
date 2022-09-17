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

pragma
  * -main.py -- a main script which have routes to run product at [**/products**] path
  * -model.py -- a script containing models and database initialization
  * -order.py -- a script to do CRUD operations for order
  * -product.py -- a script to create product

Open **model.py** file and **Run** it- This will create databases and required tables in it.

Ro run the app
`uvicorn main:app --reload`


