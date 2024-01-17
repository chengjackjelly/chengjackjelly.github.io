##### set_intersection/set_union
##### cppref:
Constructs a _sorted_ range beginning at result consisting of elements that are found in _both sorted_ input ranges [first1, last1) and [first2, last2). If some element is found m times in [first1, last1) and n times in [first2, last2), the first min(m, n) elements will be copied from the first range to result. The order of equivalent elements is preserved.
##### reproduce the bug i met:
```
std::vector<std::string> a{"c","a"};
std::vector<std::string> b{"a","c"};
std::vector<std::string> v_intersection;
std::ranges::set_intersection(b,a,
                std::back_inserter(v_intersection));
for(auto & x:v_intersection){
    std::cout<<x<<std::endl;
}
```

since vector is not sorted, the result is not meet what we desire. So it is better to use set instead of vector when we need to use this set operation.