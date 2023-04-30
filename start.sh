uvicorn main:app --reload > vault_test.out 2>&1 & echo $! > python.pid
echo "[FAST VAULT] Service started"
