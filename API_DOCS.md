# API

#### General Format
```
snip-index.herokuapp.com / <mode> / <language-code> / <parameters>
```


- **Language-Codes**
  - **py** : Python
- **Modes**
  - **Search**
    - Parameters 
        1. No of Results
        2. Keywords for Search
  - **fetch** 
    - Parameters 
        1. Hash Key of Code to fetch


#### Examples

**1>** Returns first 20 results for query "bubble sort" for required language.
(Sorted according to their popularity and concordance)
```
> snip-index.herokuapp.com/search/py/20 bubble sort 

Result :

[
  [
    0:Similarity Score(Between 0 to 1) 
    1:No of times this algo is used by others
    2:Hash Value of this Snippet. (Used While Fetch,See the next example)
    3:Algo/Function/Class Name.
    4:Snippet Description.
  ]
  [
    0:Similarity Score(Between 0 to 1) 
    1:No of times this algo is used by others
    .
    .
  ]
  .
  .
]
```


**2>** Returns Source Code corresponding to given Hash  
```
> snip-index.herokuapp.com/fetch/py/69dcb9989cff99fcdba7e82651a6f3

Result :
[
  "def bubble_sort(collection):\n    \"\"\"Pure implementation of bubble sort ......
]

```
