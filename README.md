Flask Rest Setup
=================================
[![Format Check](https://github.com/BetterToPractice/flask-rest-setup/actions/workflows/main.yml/badge.svg)](https://github.com/BetterToPractice/flask-rest-setup/actions/workflows/main.yml)


### How To Run
```
# Run db, etc
docker-compose up -d --build

# Go to Project location
cd src/project

# Copy env from example
cp .env.example .env

# Install requirements
pip install -r requirements.txt

# Run migrate
flask db upgrade

# Run application
export FLASK_APP=main.py
flask run --reload
```
