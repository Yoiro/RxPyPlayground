What works:
-----------
* source_of = Observable.of(...) OK with 1 Object, OK with 3 functions  
* source_of.map(fn)  
* source_of.filter(fn)  
* .of, .map and .filter can be chained together with expected behaviours.  
* source_int = Observable.int(...)  
* .int cannot be chained  
* Subscribe function is ok for both of those methods  
