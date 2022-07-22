# Project Alpha

## 💻  Technologies
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)

## 🔨 Project setup

```bash
# Clone repository
git clone https://github.com/thomasnakamura/projectalpha.git
```

```bash
cd projectalpha
pip install -r requirements.txt
python manage.py migrate

python manage.py loaddata fixture.json

#create a superuser
python manage.py createsuperuser
```

## ▶️ Running locally

```bash
python manage.py runserver
```
