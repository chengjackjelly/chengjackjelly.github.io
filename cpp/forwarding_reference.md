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
