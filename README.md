# WebScrapingForAll
A simple set of tools to make web scarping easy. 
This tool is perfect for collecting information in websites where data is presented upfront without the need of clicking or entering passwords.
### Disclaimer 
Every website is different, therefore not every toll can be used on every website This toolbox is especially good for scraping websites in html.

## Installation
Use git (https://git-scm.com/downloads).
```python
pip install git+https://github.com/marangoisa/WebScrapingForAll
```
To update
```python
pip install --upgrade git+https://github.com/marangoisa/WebScrapingForAll
```
Or download the complete file to your computer and use the command prompt to run from the setup folder
```python
pip install C:/xxx/xxx/WebScrapingForAll
```

## Usage
Import all (*) functions or one by one
```python
import WebScrapingForAll.WS
from WebScrapingForAll.WS import *
```
### FindKey 
Use FindKey to find unique strings related to the data (keys).\
Example: let’s say we want all the sates in http://www.sale-tax.com/. To find the key we have to provide a few keywords used as training (i.e. Ohio, NorthDakota) 
```python
keys=FindKey(address='http://www.sale-tax.com/',training=['Ohio'])
```
 ### TestKey
 Test how many times the key appears.\
 Example: we need a key that appears 50 times (number of states)
 ```python
 TestKey(address='http://www.sale-tax.com/',key=keys[0])
 ```
 Using only the last part, one gets a key that appears 50 times
 ```python
 key0=keys[0][48:len(keys[0])]
 TestKey(address='http://www.sale-tax.com/',key=key0)
 key1=keys[1][0:len(keys[1])-5]
 TestKey(address='http://www.sale-tax.com/',key=key1)
 ```

### ManyInOne
Use the Key to find all the needed elements
```python
States=ManyInOne(address='http://www.sale-tax.com/',keyst=key0,keynd=key1)
```
### OneInMany
Use ManyInOne if you have more than one address

```python
cities=['http://www.sale-tax.com/AlabasterAL',
        'http://www.sale-tax.com/AnnistonAL',
        'http://www.sale-tax.com/AuburnAL']
Rates=[]
for i in cities:
    rt=OneInMany(address=i,keyst="'rate'>",keynd='<')
    Rates.append(rt)
```

