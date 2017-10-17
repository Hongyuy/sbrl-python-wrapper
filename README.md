# sbrl-python-wrapper
A python wrapper for R package sbrl, following sklearn main object API. 

Dependencies: ``numpy, pandas, rpy2`` 

Installation:  
```
pip install -e .
```

Usage:
```
from sbrl import SBRL
sbrl_model = SBRL()
sbrl_model.fit(X,y)
sbrl_model.predict(X)
sbrl_model.print_model()
```
