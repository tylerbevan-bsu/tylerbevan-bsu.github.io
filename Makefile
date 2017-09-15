
default: html

html:
	pelican -s pelicanconf.py -o public content
