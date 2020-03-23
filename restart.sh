. venv/bin/activate
kill `ps aux | grep "python jokerdyndns.py" | grep -v grep | awk '{print $2}'`
nohup python jokerdyndns.py > /dev/null 2>&1 &
