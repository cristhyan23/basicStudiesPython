import curses
from curses import wrapper
import queue
import time



maze = [["#","#","#","#","#","#","O","#","#"],
        ["#"," "," "," "," "," "," "," ","#"],
        ["#"," ","#","#"," ","#","#"," ","#"],
        ["#"," ","#"," "," "," ","#"," ","#"],
        ["#"," ","#"," ","#"," ","#"," ","#"],
        ["#"," ","#"," ","#"," ","#"," ","#"],
        ["#"," ","#"," ","#"," ","#"," ","#"],
        ["#"," "," "," "," "," "," "," ","#"],
        ["#","#","#","#","#","#","#","X","#"]
]


def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0,0,"hello world!")
    stdscr.refresh()
    stdscr.getch()

wrapper(main)