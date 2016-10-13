# SCHELLING SEGREGATE

Before starting, numpy must be installed first. Install it using `pip install numpy`. 

To use, import everything from exam.py by typing:
`from exam import *`

## Problem 1
```
loadgrid(<filename>) 
```

## Problem 2
```
g = loadgrid(<filename>) 
dissimilarity(g, 0,0, 2,2)
```

## Problem 3
```
g = loadgrid(<filename>) 
schelling(g, 0.3)
```

## BONUS 
```
g = loadgrid(<filename>) 
schelling_segregate(g, 0.3)
```

### To use schelling or schelling_segregate:
```
schelling(grid, threshold)
schelling_segregate(grid, threshold)
```
`schelling()` and `schelling_segregate()` can have additional parameters:
1. log - enable/disable logs
  * True
  * False
2. limit - maximum number of rounds. Any positive integer can be a limit.
