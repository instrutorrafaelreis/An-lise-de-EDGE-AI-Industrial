@echo off
title Edge AI Frigorifico SIF - Modo Pendrive TV Box / Notebook
cd /d "%~dp0"
echo ======================================================================
echo   INICIANDO SISTEMA EDGE AI FRIGORIFICO SIF (11,9 KB INT8 - OFFLINE)
echo ======================================================================
where python >nul 2>nul
if %errorlevel%==0 (
    python servidor_local_tvbox.py
) else (
    start "" "ABRIR_NA_TVBOX.html"
)
