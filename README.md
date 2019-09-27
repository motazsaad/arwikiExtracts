# Arabic Wikipedia Extracts
Documents extracts from [Arabic Wikipedia](ar.wikipedia.org) downloaded from [Arabic Wikipedia dumps](https://dumps.wikimedia.org/arwiki/)
## instructions 
1. get the corpus dump 
```
wget https://dumps.wikimedia.org/arwiki/latest/arwiki-latest-pages-articles.xml.bz2 
```
2. get the tool
```
git clone https://github.com/attardi/wikiextractor.git
```

OR 

```
wget https://github.com/attardi/wikiextractor/raw/master/WikiExtractor.py
```



3. extract: 
```
python arwikiExtracts/WikiExtractor.py arwiki-latest-pages-articles.xml.bz2 -o 20190920 --json 
```

4. Compile and compress (optional):
```
python json2text.py
7za -v50m a arwiki_20190920.txt.zip arwiki_20190920.txt
```

to unzip 
```
7za x arwiki_20190920.txt.zip.001

```


## License
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-sa/4.0/)
 
This corpus is extracted by [wikiextractor](https://github.com/attardi/wikiextractor)

## corpus extracts from 20-09-2019 
| documents | words | vocabulary |
| --- | --- | --- |
| 953,507 | 123,079,742 | 4,437,963 |


[Most frequent words and Hepax words](arwiki_20190920_info.md)


## corpus extracts from 20-10-2018 

## corpus extracts from 20-01-2017 
  
### Corpus Information

| documents | words | vocabulary |
| --- | --- | --- |
| 459,208 | 83.5M | 4.7M |

## To cite this resource:

Motaz Saad and Basem Alijla (2017). _WikiDocsAligner: an off-the-shelf Wikipedia Documents Alignment Tool_. in The Second Palestinian International Conference on Information and Communication Technology (PICICT 2017). 
