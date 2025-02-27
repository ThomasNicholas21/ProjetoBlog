#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar
set -e

# Ficará executando até que o postgres seja iniciado, verificando o HOST e a PORTA
# configurando nas variáveis de ambiente
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST $POSTGRES_PORT) ..." &
  sleep 0.1
done

echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"

python manage.py collectstatic
python manage.py migrate
python manage.py runserver
