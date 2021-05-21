env :
	test -d venv || python3 -m venv venv

requirements: venv
	. venv/bin/activate; pip3 install -Ur requirements.txt;

clean:
	rm -rf venv
	rm -rf output.txt

test:
	. venv/bin/activate; python3 kMeans_shvnka005.py

run:
	make clean && make env && make requirements && make test