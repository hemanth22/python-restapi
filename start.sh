uvicorn main:app --host 0.0.0.0 --port 8000 > vault_test.out 2>&1 & echo $! > python.pid
echo "[FAST API] Service started"
