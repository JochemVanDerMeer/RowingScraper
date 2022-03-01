# Rowing Scraper

This is a scraper that retrieves results from Student Rowing Association Phocas at the Dutch Championship Indoor Rowing (NKIR). The results are written to an .xls file, which can be used for further purposes by the association. Built with Python.

## Project description
The manual part of this scraper consists of adding URLS to scrape. The Time Team website (https://time-team.nl/nl/info) provides results sorted by association, making it easy to add the URLs of races in which Phocas competes. 

`scrape.py` finds the relevant times and writes them to `output.txt`. This file is then used by `createSheet.py` which processes the results and creates a table, which is then written to `nkir_times.xls`.

## Reflection

I am member of Student Rowing Association Phocas, which is based in Nijmegen. Within the association, I am member of the data committee. My responsibility in this committee was to create this scraper, such that the results could be used by other members of the association for analytical purposes. Having partipated in the Dutch Championship Indoor Rowing myself, it was a nice project to build, as I also came across my own name in the results.
