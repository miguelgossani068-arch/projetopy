@echo off
title Vyreon - Django

echo ===============================
echo Iniciando o projeto Vyreon
echo ===============================
echo.

if not exist ".venv" (
    echo Criando ambiente virtual...
    python -m venv .venv
)

echo Ativando ambiente virtual...
call .venv\Scripts\activate

echo Instalando dependencias...
pip install -r requirements.txt

echo.
echo Servidor iniciado.
echo Acesse no navegador: http://localhost:8000
echo.

python manage.py runserver

pause
