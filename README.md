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

### most frequent word
| Word   |   Frequency |
|:-------|------------:|
| في     |     5312695 |
| من     |     3181089 |
| على    |     1332843 |
| إلى    |     1003987 |
| هو     |      670619 |
| أن     |      653989 |
| عام    |      582445 |
| التي   |      536241 |
| مع     |      508169 |
| و      |      506597 |
| عن     |      486752 |
| أو     |      451778 |
| ،      |      419063 |
| هي     |      412564 |
| كان    |      380104 |
| .      |      342948 |
| بين    |      326676 |
| ما     |      310063 |
| هذه    |      305964 |
| بعد    |      289098 |
| الذي   |      287346 |
| كانت   |      280527 |
| حيث    |      273788 |
| هذا    |      271383 |
| عدد    |      263233 |
| بن     |      239084 |
| وقد    |      216643 |
| ولد    |      216060 |
| -      |      215931 |
| سنة    |      215680 |

### hapax words
| Word                    |   Frequency |
|:------------------------|------------:|
| لبوتشيني.               |           1 |
| OT11                    |           1 |
| وسفيزف،                 |           1 |
| التَّمايُز                 |           1 |
| اراتوشين                |           1 |
| رومبوني.                |           1 |
| بأليكساندريا،           |           1 |
| فولِد                    |           1 |
| "كمستعمرة               |           1 |
| يردد:"فلنغير            |           1 |
| (camila)                |           1 |
| التصرية،                |           1 |
| H.AMDT.974              |           1 |
| الاصرة                  |           1 |
| "تووت                   |           1 |
| (بالإنجليزية:Shielfield |           1 |
| العبايات.               |           1 |
| (خُرَّمشهر)،               |           1 |
| "غوبلز                  |           1 |
| الصحيحة-                |           1 |
| أذكرني                  |           1 |
| نالاعضاء                |           1 |
| طتبت                    |           1 |
| ريدجاني،                |           1 |
| Bolnisi)                |           1 |
| دلامه.                  |           1 |
| يَتخد                    |           1 |
| الغوا"                  |           1 |
| السيكلوثيميا،           |           1 |
| تبرزين]]                |           1 |


## corpus extracts from 20-10-2018 

## corpus extracts from 20-01-2017 
  
### Corpus Information

| documents | words | vocabulary |
| --- | --- | --- |
| 459,208 | 83.5M | 4.7M |

## To cite this resource:

Motaz Saad and Basem Alijla (2017). _WikiDocsAligner: an off-the-shelf Wikipedia Documents Alignment Tool_. in The Second Palestinian International Conference on Information and Communication Technology (PICICT 2017). 
