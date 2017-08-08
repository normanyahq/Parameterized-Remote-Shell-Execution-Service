PORT := 41414
HOST := 0.0.0.0
WORKER := 4

.PHONY: install run debug

install:
	pip install -r requirements.txt

run:
	gunicorn -w $(WORKER) server:app -b $(HOST):$(PORT)

debug:
	export FLASK_APP=server.py && flask run -p $(PORT) --host $(HOST)
