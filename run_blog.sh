#!/bin/bash
python manage.py migrate --settings=config.settings.production 
python manage.py collectstatic --settings=config.settings.production 
echo "from django.contrib.auth.models import User; User.objects.create_superuser('MiladAdmin', 'milad_khaleghi@live.com', '*m09126979915R#')" | python manage.py shell
python manage.py runserver 0.0.0.0:8000  --settings=config.settings.production 