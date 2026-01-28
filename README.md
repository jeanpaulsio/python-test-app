# Python Test App

Basic Flask web server for Heroku deployment.

## Local Setup

```bash
pip install -r requirements.txt
python app.py
```

Visit http://localhost:5000/ping

## Deploy to Heroku

```bash
heroku create
git init
git add .
git commit -m "Initial commit"
git push heroku main
```
