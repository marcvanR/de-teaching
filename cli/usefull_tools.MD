# CLI TOOLS

in our work we often work on the terminal, and to be honest, the more time you spend in a situation where a lot of what
you see is text based, the more you start to appreciate it. Most commands here are either very old and highly optimized
or new implementation of the same but "rewritten in Rust". However the optimizations that lead to the programs being so
good are implemented as well ofcourse. This is by no means an exhaustive list, just a bunch of commands that I tend to
use sometimes to very often in my day to day work. There is also an example in our Lingua Franca python how to create
your very own cli setup. 

## The Golden oldies

- `man` -> access documentation on all the following commands 
  ```shell
  man grep
  ```
- `cd` -> change your directory
- `ls` -> show what is in the current folder, notable flags are: -a show all files, including hidden ones; -l show 
information about the files including size, ownership and modes like being executable. 
- `pwd` -> which folder am I in right now starting from `/`
- `rm` remove file or folder
- `cp` copy file or folder 
- `rsync` file transfer, either on your local system but also to remote locations, very fast and reliable
- `open .` -> open a file explorer at the given position (this is for GUI losers ofcourse)
- `vi` / `nano` -> availble on many systems to manipulate text in within your terminal. 
- `vim` / `emacs` for some actual text editing, I prefer vim, and if you prefer emacs you're dumb. 
- `>` operator to pipe the data into a file which gets (re)-created. Be carefull, this deletes everything thats in the file in the first place
- `>>` operator to pipe the data into a file. This however is an append type, so this can add stuff to an existing file
- `ssh` or Secure SHell, this allows you to navigate to other servers in a secure manner and perform actions there. 
- `cat <filename>` this extracts all the contents of a file and pipes it to STDIN 
- `|` The pipe, this is especially usefull, this allows you to chain your commands into a fully fledged analysis/transformation pipeline
- `grep` look for lines with some filter, super useful to look for stuff in logs or a filename within a large folder
- `sed` replace text in a file or in the piped text
- `xargs` take in the list of values and redistribute them to the next command as separate args, handy if you need to call some azure command 20000 times for every entry in a list for example. 
- `awk` transform lines in A LOT of different ways 
- `jq` JSON JSON JSON, this allows you to work with json files in all kinds of ways, to start simply makes it better readable, but allows you to access json data in very convenient ways
- `less` open a file which you can scroll through without needing to open the entire file. For "Big data" stuff very convenient
- `head` show first 10 lines (Dont let 20 Gb file destroy your terminal)
- `tail` show last 10 lines 
- `htop` show the running processes on your computer, a bit like task manager on windows
- `clear` clear your screen to start fresh (but with all of your context in place)
- `chmod` change file modes or Access Control Lists 
- `chown` change owner of the file (if you currently have rights to change that 😉;


## Networking

- `nslookup`
- `dig`
- `nmap`
- `traceroute`

### Files

- `/etc/resolv.conf` your traditional nameserver IP adresses are stored here. 
- `/etc/hosts` you can define your own host to IP adress mappings here


## Working with text

- `fzf`
    A lot of the commands that are described here work nicely with fzf, an example could be to see which files are
available in your folder structure and open them in `vim`
- vim, any system that has it installed comes with `vimtutor` which you can run from your terminal. Go through the entire thing to get you started, this will land you in a position where you can move around a bit more easily and you can continue from there on. 
<img src="./resources/vim_fzf.gif" width="800" alt="vim with fzf"/>

## Working with kubernetes

- `kubectl`
  - `show`
  - `get`
  - `describe`
  - `edit`
  - `cp`
- `kubens`
- `kubectx`
- `kdash`


## Making this file better with screencaptured terminal as GIFs

- `asciinema`
- `agg` 

![Example](resources/show_terminal.gif)


## Data exploration

- `duckdb`
- 


## Some other useful stuff, which are not tools per se

- `cntrl-r` (the one shown here is actually combined with `fzf`)

<img src="./resources/control_r.gif" alt="control r usage"/>

- `TAB` -> Autocomplete really is your best friend here, don't type out everything, let the system show you what's possible


