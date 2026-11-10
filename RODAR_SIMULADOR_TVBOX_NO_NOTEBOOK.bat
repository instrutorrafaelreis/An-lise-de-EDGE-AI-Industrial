@echo off
title Emulador de Hardware TV Box Smart Pro 4K (1 Nucleo ARM / 2GB RAM) - Edge AI
cd /d "%~dp0"
echo ============================================================================
echo   INICIANDO SIMULADOR DE AMBIENTE TV BOX SMART PRO 4K NO SEU NOTEBOOK
echo   (Trava o processo em 1 Nucleo Fisico da CPU + Monitora Limite de 2GB RAM)
echo ============================================================================
python simular_ambiente_tvbox.py
pause
