input validation:
validate every pointer:
so if the system call has to read n parameter from stack
we should validate each n of these parameter? or just check the parameter that is pointer(which will be dereferenced afterward)

for example the sys read has 3 parameter:
1: *(void**)(f->esp+4) (int : fd)
2: *(void**)(f->esp+8)  (char pointer: file name)
3: *(void**)(f->esp+12) (unsigned: length)
in this case we only have to check the validation of the second pointer ?

in order to check the validation:
the value of pointer has to be under PHYS_SPACE

for the char*, in order to validate the string is null terminated, we should iterate the string until the null terminater and throw the error if the the address in middle is reach to PHYS_BASE

computing the page boundaries?
write(1, malloc(1), 1000);
write(1, pointer, size);
valide the pointer and pointer+size

cstring:
create
open
remove

buffer:
read
write



check the return value of pagedir_get_page()