#### implement range and my discovery

##### situation&task:
we are asked to implement a prototype of range in cpp20.

##### action:
Besides the method that need to be exposed to the user, there are several things we need to consider.

How can we initialize the range?
We can either

- save the whole container as the private data member.
- or we should only save the *copy* of begin and end iterator.

It turns out very obviously that the latter is correct. But I still go for the first one at the beginning and encounter many problems.

And the reason the first one is a big mistake is due to:

- By all means, we can only get the *copy* of the iterator from the container.(*Update 12/21: We can not get the non const reference of the iterator from container which means we can still get the const reference of the iterator from container*) However, method likes `filter` in `range` require us to modify the `range` by modifying the iterator of it. This can not be achieved since `iterator begin(){
        return data.begin();
    }` which we expose to the user, can not change the current `range` we are working on.
- But if we use the latter way, which we only store the *copy* of iterator at the very beginning. And return the reference to our iterator inside the range, we are allowed to change the begin and end for the `range`.
- Noted that the iterator of both range and original container point to the same place (the container). However, the *address* of iterator is difference( they are different object in memory).

##### other detail:
###### std::distance
Noted that some containers like list, forwarding_list, do not have the size() method. The reason can be found [here](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2008/n2543.htm). But we can use std::distance(start,end) to solve this problem.(Noted that it causes O(N) for list and forwarding_list).

###### std::advance
Some iterator are not allowed to perform `++` operator. This is a method return void and perform the operation to the iterator inplace.
```
//example std::advance
auto l=data.begin();
std::advance(l,n);
```