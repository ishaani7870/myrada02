@echo on
start msedge http://localhost:9077/
uvicorn be.main:app --reload --port 9077

REM gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
