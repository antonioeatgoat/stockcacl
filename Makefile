init:
	pip install -r requirements.txt

test:
	pytest test_percentile.py

run:
	python3 -m percentile
