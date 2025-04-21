python manage.py clean
python manage.py syncdb
python manage.py migrate
python manage.py import_admin
python manage.py collectstatic --noinput --clear

exec "$@"