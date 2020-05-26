# WebScrapingForAll
A simple set of tools to make web scarping easy. 
This tool is perfect for collecting information in websites where data is presented upfront without the need of clicking or entering passwords.
### Disclaimer 
Every website is different, therefore not every toll can be used on every website This toolbox is especially good for scraping websites in html.

## Installation
Download the complete file to your computer and use the command prompt to run from the setup folder
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
Use FindKey to find unique strings related to the data (keys)
Example: let’s say we want all the sates in http://www.sale-tax.com/. To find the key we have to provide a few keywords used as training (i.e. Ohio, NorthDakota) 
```python
keys=FindKey(address='http://www.sale-tax.com/',training=['Ohio','NorthDakota')
```
### ManyInOne
Use the Key to find all the needed elements
```python
States=ManyInOne(address=adrs,keyst=keys[0],keynd=keys[1])
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
 
