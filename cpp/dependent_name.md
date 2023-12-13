#### Dependent names in cpp

##### situation:
We want to create a variadic template class. Inside the variadic template, we want to create a static template member function which takes the new class(type) as template and calculate the index of this class(type) in the original variadic template. it should return -1 if the class(type) does not exist in the variadic template.

##### task:
We have to pass a template into the member function of a variadic template class. In order to do so, we have to solve the dependent name's problem in cpp. But what is the dependent names in cpp?

##### action:
Here is our variadict template class:
```
//base class
template<typename... Types> 
struct Variant_Helper{
};
//specialization
template<typename Type, typename... Types > 
struct Variant_Helper<Type,Types...>{
   
    template<typename Query>
    constexpr static int index_of(int index){
      if(std::is_same_v<Query,Type>){
        return index;
      }
      return Variant_Helper<Types...>::index_of<Query>(index+1);
    }
};
//specialization
template<> 
struct Variant_Helper<>{
    template<typename Query>
    constexpr static int index_of(int index){
      return -1;
    }
};

```
##### result:
When we try to complie the code  `Variant_Helper<Types...>::index_of<Query>(index+1);`, a error will be reported by complier:
```
 error: expected primary-expression before '>' token
   53 |       return Variant_Helper<Types...>::index_of<Query>(index+1);
      |                               
```


#### Why? and What is dependent names in cpp?
- If a name depends on a template (as was the case with `Variant_Helper<Types...>::index_of<Query>`) the compiler cannot assume that the dependent name(`index_of` in our case) is a template
- Therefore the only reasonable interpretation must be
that the second < is a comparison
- unless we specify it as a template by adding template
before the dependent name
- This is true for all operators which can access names `->`, `.` and `::`

#### fix the code


```
return Variant_Helper<Types...>::template index_of<Query>(index+1);
```