### QuickStart
```bash
git clonne https://github.com/Vitalii-pr/task
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

## change db connection in .env

python3 manage.py migrate

python3 manage.py runserver
```


###Testing

```bash
pytest
