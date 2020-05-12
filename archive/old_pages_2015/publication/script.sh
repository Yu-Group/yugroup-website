bibtex2html -nokeywords -noabstract -s alpha -d -r -t "" -nodoc -noheader -o biblio yugroup.bib
cat head_yugroup.html biblio_title.html biblio.html bottom_yugroup.html > index.html
