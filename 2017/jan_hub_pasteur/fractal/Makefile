

dag:
	snakemake -s fractal.rules --configfile fractal.yaml --dag > dag.dot
	dot -Tpng dag.dot -o dag.png

snakemake:
	snakemake -s fractal.rules --configfile fractal.yaml

clean:
	rm -f julia_*.png
	rm -f dag.dot
	rm -f index.html
	rm -rf analysis

run:
	mkdir -p analysis
	cp fractal.py analysis
	sequanix -w analysis -s fractal.rules -c fractal.yaml
