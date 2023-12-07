

#### How to copy a class.
##### What is shallow copy?

When we copying class type, the default behavior is to copy the data members. When the data members contain data object like pointer to a array, we only copy the value of pointer(which is the address of the array) instead of the array itself. This behavior is so called shallow copy.


##### copy constructor vs copy assignment

When write copy constructor we have to:
```
Array(Array const& other)
```
- make sure to pass the reference and add const to it.
- allocate a new memory for the new object we create.
- copy the value one by one.

When write copy assignment we have to deal with the extra things include:

- destory the previous resource inside the object.
- return the reference to the current assigned object.

best pratice for writing copy assginment is to reuse the *copy constructor* and *std::swap* as follow:

 ```
Array& operator=(Array const& other)
 {
 // reuse copy constructor
 Array copy { other };

 // swap the members
 std::swap(size, copy.size);
 std::swap(data, copy.data);

 // copy is destroyed which releases the previous data
return *this;
}
 ```

##### Move statement and where to use it

```
1 Array modify(Array array)
2 {
3 ++array[0];
4 return array;
5 }
6
7 int main()
8 {
9 Array a { create(1, 2, 3) };
10 Array b { modify(a) };
11 }
```

The 10th line of the code above call the copy constructor(which needs to allocate the dynamic memmory) a lot:

- When calling modify: 
- 1. we have to _copy_ a into parameter *array*
- When function modify return:
- 2. the local variable array will be destroyed so we have to _copy_ array into a temporary object in main 
- 3. To construct b we use the _copy_ constructor again

We can modify the second steps here. Instead of _copy_, we can use _move_ here where we pass rvalue reference as function parameter. _Move_ will occur aotomatically whenever we are trying to copy an rvalue.







####relative material
- slide in tddd38:Fundamentals III 