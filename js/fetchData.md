The goal of this md is to learn how to fetch model data using the built-in object in js. I have trouble in understanding the relative concept which makes this md relatively long.


**What is asynchronous in js?**

Asynchronous programming is a technique that enables your program to start a potentially long-running task and still be able to be responsive to other events while that task runs, rather than having to wait until that task has finished. Once that task has finished, your program is presented with the result.

通过异步式编程，程序可以在执行一个长时间运行的任务的同时仍然相应其他事件。

The program below uses a very inefficient algorithm to generate multiple large prime numbers when a user clicks the "Generate primes" button. The higher the number of primes a user specifies, the longer the operation will take.

_html:_
```html
<label for="quota">Number of primes:</label>
<input type="text" id="quota" name="quota" value="1000000" />

<button id="generate">Generate primes</button>
<button id="reload">Reload</button>

<div id="output"></div>
```
_javascript:_
```
const MAX_PRIME = 1000000;

function isPrime(n) {
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return n > 1;
}

const random = (max) => Math.floor(Math.random() * max);

function generatePrimes(quota) {
  const primes = [];
  while (primes.length < quota) {
    const candidate = random(MAX_PRIME);
    if (isPrime(candidate)) {
      primes.push(candidate);
    }
  }
  return primes;
}

const quota = document.querySelector("#quota");
const output = document.querySelector("#output");

document.querySelector("#generate").addEventListener("click", () => {
  const primes = generatePrimes(quota.value);
  output.textContent = `Finished generating ${quota.value} primes!`;
});

document.querySelector("#reload").addEventListener("click", () => {
  document.location.reload();
});
```

The code above is a synchronous program that generate(possibly large amount of) prime number specified by the user input.
It takes a few secounds before the result shows up.
The problem to synchronous programming is that our program stay completely unresponsive before all the prime number being generated.

And a asynchronous program should be able to:

- Start a long-running operation by calling a function. （通过调用函数执行一个长时间运行的任务）
- Have that function start the operation and return immediately, so that our program can still be responsive to other events. （让函数开始运算的同时立即返回，我们的程序因此可以相应其他事件）
- Notify us with the result of the operation when it eventually completes.（当长时间运行的任务结束后提醒我们）

**What is Event handlers in js?**

```
const xhr = new XMLHttpRequest();

xhr.addEventListener("loadend", () => {
log.textContent = `${log.textContent}Finished with status: ${xhr.status}`;
});

xhr.open(
"GET",
"https://raw.githubusercontent.com/mdn/content/main/files/en-us/_wikihistory.json",
);
xhr.send();
log.textContent = `${log.textContent}Started XHR request\n`;

```
Here, the function provided to addEventListener is not executed immediately. It will be executed when the "loadend" event occurs, which happens after the xhr.status is available. 

An event handler is a particular type of callback. A callback is just a function that's passed into another function, with the expectation that the callback will be called at the appropriate time. 


**What is Promise in js?**

The Promise is a [standard built-in object](#standard-built-in-objects) which category belong to [control abstraction objects](#control-abstraction-objects).

The asynchronous method returns a promise to supply the value at some point in the future.


A Promise is in one of these states:

pending: initial state, neither fulfilled nor rejected.
fulfilled: meaning that the operation was completed successfully.
rejected: meaning that the operation failed.

The eventual state of a pending promise can either be fulfilled with a value or rejected with a reason (error). When either of these options occur, the associated handlers queued up by a promise's *then* method are called. If the promise has already been fulfilled or rejected when a corresponding handler is attached, the handler will be called, so there is no race condition between an asynchronous operation completing and its handlers being attached.



**What is XMLHttpRequest (XHR) in js?**
XMLHttpRequest (XHR) objects are used to interact with servers. You can retrieve data from a URL without having to do a full page refresh. This enables a Web page to update just part of a page without disrupting what the user is doing.




**Addition Note**

<a id="standard-built-in-objects">1.What is standard built-in objects</a>

Including methods/properties/objects

Standard built-in objects + global objects created by user script + provided by the host application(?) == global objects


<a id="control-abstraction-objects">2.What is control abstraction objects</a>

Control abstractions can help to structure code, especially async code (without using deeply nested callbacks, for example).


