# Vim

## History

Vim was created by **Bram Moolenar**. The history of Vim is tied to tht of 
classic Unix editors, such as *vi* and *ed*. These predate mouses and 
point-and-click interfaces, thus in Vim, everything can be done with the 
keyboard only (touch typing is important to use Vim to its full potential).

## Philosophy

### Repetition

Editing text invovles many repetitive tasks (making a same change in several
places, moving around between similar regions of a document, etc.), and Vim
thus provides tool to help repeat tasks. It can do that efficiently because it
tracks our most recent actions.

In Vim, you can repeat the last **change** with a single keystorke (with the dot
command). To use this efficiently, you must understand what is a change in Vim 
and thus how to structure your actions so repeating the last change will do
something useful.

A **change** in Vim is anything command that changes the buffer. It could apply
to one character (e.g pressing x), several (e.g pressing x with a counter), an
entire line (e.g gUgU is a single change), or several, potentially the entire
file (e.g. using >G at the start of the file). Using an operation-motion, a 
text object operation (caw, yap, etc.), or dipping into Insert Mode,
typing text and reverting it to Normal Mode are all examples of actions that 
count as a single change. Any command that changes the buffer (x, dd, etc.)
is also a single change.

This broad possible definition of a change means that it can be very powerful
to simply "repeat" a change.

The dot command can be considered to be a **micro macro**: like a macro, it 
plays back a series of keystrokes, we use it in order to avoid having to 
retyping them (difference being that with actual macros you can decide when to
start and stop recording them, while the dot command always simply contains the
last change, you have to develop an intuition for what a change is to use it
well).

Repetition is not limited to replaying changes: you can also replay the last
search pattern (be it filewise with n/N or linewise with ;/,), the last
Ex-command with @: (the :substitute command is repeated often enough than it has
its own repetition shortcut: &), etc.

If you are too hasty in repeating something, you can always cancel it with
**undo** (u) command. Likewise, when you use search motions, you can either
go forwards or backwards.

The book *Practical Vim* suggests to keep to the **Dot Formula**, using one
keystroke to move (motion) and one keystroke to execute a change (repeating the
last change with .). As you can, moving around a document using a motion is 
not a change.

## Plugins

### Packages

**Packages** were introduced with Vim8 (plugins were notoriously hard to install
before that which is why plugin managers exist).

A **package** is simply a directory that contains one or more plugins, which
are directories with one or more scripts, which are standalone files written
with Vimscript.



```aln
# Commands
  # Modal
    Command to enter insert mode at cursor : i
    Command to enter insert mode after cursor : a
    Command to delete character under cursor and enter insert mode at the same location : s
    Command to enter insert mode after creating a new line below current line : o
    Command to enter insert mode after creating a new line above current line : O
    Command to enter insert mode at end of current line : A
    Command to enter insert mode to replace the content of current line : C
    Command to enter insert mode at the start of current line (non-whitespace start) : I
    Command to delete current line and enter insert mode to replace its content (same as cc) : S
  Command to repeat last change : .
  Command to undo the last change : u
  Command to delete character under cursor : x
  Command to delete the current line : dd 
  Command to repeat the last ex command : @:
  Command to repeat the last substitution : &
  Command to execute the macro in register {x} : @x
  Command to start recording a macro in register {x} : qx
  Command to stop recording a macro : q

# Ex-Commands
  Ex-command to open documentation, with an optional {topic} : :h topic
  Ex-command to substitute a {pattern} with a replacement : :s/pattern/replacement
  
# Operators
  Operator to increase line indentation : >
  Operator to decrease line indentation : <
  Operator to replace text (delete text in the motion and enter insert mode to replace it) : c
  Operator to delete text : d
  Operator to yank (copy to unnamed register) text : y
  Operator to switch to upper case : gU
  Operator to switch to loewr case : gu
  Operator to encode text with ROT13 Caesar : g?

# Motions
  Motion leftwards : h
  Motion rightwards : l
  Motion topwards : k
  Motion downwards : j
  Motion towards next (small) word : w
  Motion towards next (big) word : W
  Motion to start of line, including whitespace : 0
  Motion to start of line, excluding whitespace : ^
  Motion to end of line : $
  Motion to end of file (end of last line) : G
  Motion to start of next line, excluding whitespace : +
  # Search Motions
    Filewise motion towars next occurence of pattern : /pattern
    Filewise motion towars previous occurence of pattern : ?pattern
    Filewise motion to next occurence of word under cursor (to first character) : *
    Filewise motion to previous occurence of word under cursor (to first character) : #
    Linewise motion towards next occurence of {c}haracter : fc
    Linewise motion towards previous occurence of {c}haracter : Fc
    Linewise motion towards before next occurence of {c}haracter : tc
    Linewise motion towards after previous occurence of {c}haracter : Tc
    Repeat the last linewise search forwards : ;
    Repeat the last linewise search backwards: ,
    Repeat the last filewise search forwards : n
    Repeat the last filewise search backwards : N

# Vimscript
  Syntax to declare a {FunctionName} in Vimscript (...) : function! FunctionName() ... endfunction
  Instruction to output {data} in Vimscript : echo data
  Instruction to define a new Vim ex-command with an {Identifier} and an associated {Function} : command! Identifier call Function()
```

```aln-temp
- custom text object, Kana Natsuno
- *rails.vim* plugin, Tim Pope
- *:gn*
- *:cfdo*
- *:vimgrep*
- *:make*
- *vimrc*
- *:substitute*, :g (flags)
- *Q*
- *|*
- *q:*
- *q/*, *q?*
- %, . , etc. (ranges in Ex command)
- nnoremap (an associate normal mode keys to ex command btw)
- :source (loading vimscript)
sand + sand + sand + sand + sand + sand
```

