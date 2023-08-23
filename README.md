Flask Setup
=================================


### How To Run
```
# provide db, etc
docker-compose up -d --build

# run script
export FLASK_APP=main.py
pip install -r requirements.txt
cd src/project

# migrate
flask db upgrade
# run application
flask run --reload
```
