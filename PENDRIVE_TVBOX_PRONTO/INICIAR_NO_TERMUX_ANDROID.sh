#!/bin/sh
echo "======================================================================"
echo "  INICIANDO EDGE AI FRIGORIFICO SIF NA TV BOX ANDROID (OFFLINE)"
echo "======================================================================"
cd "$(dirname "$0")"
if command -v python3 >/dev/null 2>&1; then
    am start -a android.intent.action.VIEW -d "http://localhost:8080/ABRIR_NA_TVBOX.html" >/dev/null 2>&1 &
    python3 servidor_local_tvbox.py
else
    am start -a android.intent.action.VIEW -d "file://$(pwd)/ABRIR_NA_TVBOX.html"
fi
