delete:
delete from cursor to the next word: dw
delete from cursor the end of the line: d$
delete whole line: dd
operator [number] motion
undo:
undo previous actions: u
undo all the changes on a line: U
undo the undo: Ctrl-R

paste:
put back the text just been deleted/copied: p
replace the character under the cursor: r
change from cursor to the end of the line: c$ (delete and replace)

move:
Ctrl-G show the location in the file
G moves to the end of the file
number G move to that line
gg moves to the first line

search:
:/xx search xx forward
:?xx search xx backward
n/N to find the next

subtitute:
:s/old/new (substitute the first)
:s/old/new/g (substitute all on a line)
:#,#s/ole/new (from line to line)
:%s/olg/new/g subtitue all on a file
:%s/old/new/gc subtitue all on a file and ask confirmation each time


match:
type % while the cursor is on ([{}]) to go to its match

insert:
o: open a line BELOW the cursor and start to insert
O: open a line ABOVE the cursor.
a: insert text AFTER the cursor.
A: insert text after end of the line.
e: move to the end of a word.
y: copy text
set (no)ic(ignorecase) is(incsearch) hls(hlsearch)

0     Go to the first character in the current line
^     Go to the first nonblank char in the current line
g_    Go to the last non-blank char in the current line
$     Go to the last char in the current line
n|    Go the column n in the current line

f    Search forward for a match in the same line
F    Search backward for a match in the same line
t    Search forward for a match in the same line, stopping before match
T    Search backward for a match in the same line, stopping before match
;    Repeat the last search in the same line using the same direction
,    Repeat the last search in the same line using the opposite direction

H     Go to top of screen
M     Go to medium screen
L     Go to bottom of screen
nH    Go n line from top
nL    Go n line from bottom

zt    Bring the current line near the top of your screen
zz    Bring the current line to the middle of your screen
zb    Bring the current line near the bottom of your screen