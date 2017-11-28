
default: html

html:
	pelican -s pelicanconf.py -o ../tylerbevan-bsu.github.io-master content
