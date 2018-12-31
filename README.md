# Boiler Plate Python
Boiler Plate for Simple Python Application

## Setup python virtual environment

### 1. Create an environment:
```bash
cd boilerplate-python
python3 -m venv venv
```

### 2. Activate environment:
```bash
. venv/bin/activate
```

## Install dependancies:
```bash
pip3 install -r requirements.txt
```

## Run application
### 1. Install pip3 if not already install in your system
```bash
python3 main.py
```

## Install Alembic
```bash
sudo apt-get install alembic
```

## Db Migration
```bash
# Create a Migration Script
alembic revision -m "migration name"

# Running Migration
alembic upgrade head
alembic upgrade +2

# Downgrade Migration
alembic downgrade [revision]
alembic downgrade -2
```
