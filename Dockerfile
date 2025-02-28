FROM python:3.11-alpine3.20
LABEL mantainer="thomasnicholaas@gmail.com"

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copia a pasta "djangoapp" e "scripts" para dentro do container.
COPY app /app
COPY scripts /scripts

# Verifica se o arquivo commands.sh foi copiado
RUN ls -l /scripts

# Entra na pasta app no container
WORKDIR /app

# Expõe a porta 8000
EXPOSE 8000

# Instala dependências e configura o ambiente
RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /app/requirements.txt && \
  adduser --disabled-password --no-create-home duser && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chown -R duser:duser /venv && \
  chown -R duser:duser /data/web/static && \
  chown -R duser:duser /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R +x /scripts

# Adiciona a pasta scripts e venv/bin no $PATH do container.
ENV PATH="/scripts:/venv/bin:$PATH"

# Muda o usuário para duser
USER duser

# Executa o script commands.sh
CMD ["commands.sh"]