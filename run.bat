@echo on
start msedge http://localhost:9011/
uvicorn be.main:app --reload --port 9011

REM gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
