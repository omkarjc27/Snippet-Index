# API

```
snip-index.herokuapp.com / <mode> / <language-code> / <parameters>
```


#### Language-Codes
- **py** : Python 
- **go** : GoLang 
- **js** : JavaScript 

## Modes
### Search
```
All Parameters Seperated By Spaces
Parameters: <number of results wanted> <keyword1> <keyword2> <keyword3> ......

eg: 20 bubble sort // Returns first 20 results for query bubble sort for required language  
```
**Returns** a JSON List of Results in following format
```
[
  [
    Similarity Between Query and this Snippet.
    Hash Value of this Snippet. (Used While Fetch)
    Snippet Name.
    Snippet Description.
  ]
  [
    Similarity Between Query and this Snippet.
    Hash Value of this Snippet. (Used While Fetch)
    .
    .
  ]
  .
  .
]
```

### Fetch

```
Parameter: <hash key of result>

eg: 69dcb9989cff99fcdba7e82651a6f3... // Returns Source Code corresponding to given Hash  

```
**Returns** a JSON list with single element i.e. Source Code 
```
[
  "def bubble_sort(collection):\n    \"\"\"Pure implementation of bubble sort ......
]
```
