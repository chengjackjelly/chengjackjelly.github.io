#### Template template parameter

##### situation:
we try to create a template function which takes an arbitary container as parameter.

##### task:
but how to manage the template when the template itself need another template.

##### action:
```
template<typename T,typename Container<T> >
void prepend(Container<T> c, T value){

}
```
##### result
gives a error:
```
error: expected nested-name-specifier before 'Container'
   10 | template<typename T,typename Container<T> >
```

##### explanation

besides `type template parameters` and `non-type template parameters`
we still have `template template parameter`(yes we only have these three, no more!)

```
template<template<typename> typename Container,typename T>
void prepend(Container<T> c, T value){

}

```

