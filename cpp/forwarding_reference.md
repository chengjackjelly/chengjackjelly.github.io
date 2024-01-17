##### Forwarding References for function template
```
template <typename T>
void foo(T&&);
```
This will deduce the function based on what type of parameter passing in.

##### Why we have std::forward\<T>()

Consider

```
template <typename T>
void fun1(T&& t)
{
fun2(t);
}
template <typename T>
void fun2(T&& t)
{
// value category?
}
```
Then we call:
```
fun1(7);
```

When we pass 7(an rvalue) into fun1 which be deduced as a rvalue reference. t in fun1 becomes a xvalue. This means t is regarded as lvalue in the context of fun1. Then in fun2, it still be deduced as lvalue(which is not the case).

we can use std::move to solve this problem.
```
template <typename T>
void fun1(T&& t)
{
fun2(std::move(t));
}
```

However, std::move fail to provide the same value type in both function when we pass in a lvalue into fun1.

In this way, the std::forward can be used to solve this problem.

when we pass in a rvalue(included xvalue/prvalue) to std::forward, it's going to return it as an rvalue. 

##### Dealing with variadic

```
#include <utility> // std::forward
template <typename T, typename... Ts>
vector<T> store(Ts&&... list)
{
vector<T> vec {std::forward<Ts>(list)...};
return vec;
}

```

##### reproduce a bug
```
template<typename Container>
auto count_bytes_helper(Container c){
    std::begin(c);
}

int main(){
int array[] = { 1, 2, 3, 4 };
    count_bytes_helper(array);
}
```
error: error: no matching function for call to 'begin(int*&)' c++
adding the reference

The error solved by adding a reference to the parameter c.
The reason of this error is : std::begin(take the reference to the input variable), but if we pass the container as rvalue, the std::begin() will fail.