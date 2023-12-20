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

- By all means, we can only get the *copy* of the iterator from the container. However, method likes `filter` in `range` require us to modify the `range`. This means `iterator begin(){
        return data.begin();
    }` which we expose to the user, can not change the current `range` we are woring on.
- But if we use the latter way, which we only store the *copy* of iterator at the very beginning. And return the reference to our iterator inside the range, we are allowed to change the begin and end for the `range`.
- Noted that the iterator of both range and original container point to the same place (the container). However, the *address* of iterator is difference( they are different object in memory).