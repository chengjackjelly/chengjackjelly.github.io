#### How to use STL algorithm and iterator to do the I/O in cpp

##### istream_iterator

###### example with std::cin
```
//read from command line to std::vector:

std::vector<int> v;
auto begin{std::istream_iterator<int>{std::cin}};
auto end{std::istream_iterator<int>{}};
std::copy(begin, end, std::back_inserter(v));
```

###### example with std::ifstream
```
//read from file to std::vector

std::ifstream ifs("test.txt");
if (!ifs)
{
	std::cerr << "Error: Unable to open file '" << argv[1] << "'\n";
	return 2;
}

std::vector<int> v;
auto begin{std::istream_iterator<int>{ifs}};
auto end{std::istream_iterator<int>{}};
std::copy(begin, end, std::back_inserter(v));
```

##### ostream_iterator

###### example with std::cout

```
std::vector<int> v{1, 2, 3};
std::copy(std::begin(v), std::end(v),
std::ostream_iterator<int>{cout, " "});
```
