# Hello TF-IDF

[![Build Status][badge-travis]][link-travis]
[![MIT License][badge-license]](LICENSE)

A simple toy implementation of TF-IDF


## Prerequests

+ [python3](https://www.python.org/download/releases/3.0/) - required
+ [virtualenv](https://virtualenv.pypa.io/en/stable/) - required
+ [fabric](http://www.fabfile.org/) - required
+ [gmake](https://www.gnu.org/software/make/) - optional


## Execute Code

### Installing Dependencies

```bash
fab setup
```

### Run Demo Code

```bash
fab index
```

If you have already installed gmake, you can simply type

```bash
make
```

## Example Output

```bash
$ make
fab index
[localhost] local: which python3
/path/to/project/env/bin/python3
[localhost] local: python3 index.py
Building Index ..
653  records indexed ..
Your Query (e.g. Data Mining): Data Mining
Results by Sum of TF-IDFs
[ 287 ] ( 0.6107932232871334 ) Data Mining
[ 413 ] ( 0.40719548219142226 ) Mining Data Streams
[ 554 ] ( 0.40719548219142226 ) Mining multimedia data
[ 578 ] ( 0.40719548219142226 ) Data Mining Techniques
[ 188 ] ( 0.3053966116435667 ) Mining Concept-Drifting Data Streams
[ 548 ] ( 0.3053966116435667 ) Constraint-Based Multidimensional Data Mining
[ 288 ] ( 0.25694160318259573 ) Stream Mining
[ 499 ] ( 0.24431728931485341 ) Data Mining for Web Intelligence
[ 536 ] ( 0.24431728931485341 ) Data Mining: Concepts and Techniques
[ 572 ] ( 0.24431728931485341 ) Attribute-Oriented Induction in data Mining
[ 567 ] ( 0.21693370661743228 ) OLAP Mining: Integration of OLAP with Data Mining
Results by BM25
[ 287 ] ( 1.581421045562941 ) Data Mining
[ 413 ] ( 1.1688764249813042 ) Mining Data Streams
[ 554 ] ( 1.1688764249813042 ) Mining multimedia data
[ 578 ] ( 1.1688764249813042 ) Data Mining Techniques
[ 188 ] ( 0.9270399232610343 ) Mining Concept-Drifting Data Streams
[ 548 ] ( 0.9270399232610343 ) Constraint-Based Multidimensional Data Mining
[ 499 ] ( 0.7681187935591427 ) Data Mining for Web Intelligence
[ 536 ] ( 0.7681187935591427 ) Data Mining: Concepts and Techniques
[ 572 ] ( 0.7681187935591427 ) Attribute-Oriented Induction in data Mining
[ 288 ] ( 0.746688259276887 ) Stream Mining
[ 567 ] ( 0.7054582857823681 ) OLAP Mining: Integration of OLAP with Data Mining

Done.
```


[badge-travis]:    https://travis-ci.org/yuikns/hello-tfidf.svg?branch=master
[link-travis]:     https://travis-ci.org/yuikns/hello-tfidf
[badge-license]:   https://img.shields.io/badge/license-MIT-007EC7.svg
