Computer Science Rankings
=========================

Doctored version to see what could happen with Purdue ECE + Purdue CS under "Purdue Computes".

Instructions:
- Go get the dblp database. See the instructions from the original csrankings README.
- Add ECE faculty to the appropriate csrankings-X.csv. The second field should be "Purdue University". The third field should be "ECE" if they are ECE faculty. You need to use the correct name as listed on dblp. I also filled in the Google Scholar link -- not sure if that's necessary (I don't think so). I did 27 of our faculty and then had to do something else.
- There is a program called `make-ece-version.py` which reads in a csrankings-X.csv file and spits out a csrankings-ece-X.csv file. Run it like this: 

```
for f in `ls csrankings-*csv`; python3 make-ece-version.py $f
```

    - Now you have two sets of files, one called "csranking-X.csv" and the other called "csranking-ece-X.csv".

- To build the database that *merges* ECE and CS, just run `make` now. This is the full union of CS+ECE faculty, as opposed to the current scattershot union of faculty who at some point sought a joint/courtesy appointment. 
- To build a separate "Purdue CS" and "Purdue ECE" for comparison, run `export PURDUE_ECE_ALONE=1; make`
- Once done, run `python3 -m http.server` and visit http://localhost:8000
