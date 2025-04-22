from sympy import *
from IPython.display import Markdown, display
init_printing(use_latex="mathjax")
mdisplay = lambda x: display(Markdown(str(x)))

class print_delayer:
    def __init__(self):
        self.delayed_print = ""

    def add(self, input):
        self.extend("\n")
        self.extend(input)

    def extend(self, input):
        if isinstance(input, Markdown):
            input = input.data
        if isinstance(input, str):
            input = input.replace("\n", "\n\n")
        self.delayed_print += input

    def adisplay(self, input):
        self.add(input)
        mdisplay(self)
    
    def edisplay(self, input):
        self.extend(input)
        mdisplay(self)


    def __str__(self):
        temp = self.delayed_print
        self.delayed_print = ""
        return temp
    
# p = print_delayer()

# p1 = symbols("p_1")
# p.add("Hej\nmed")
# p.add(f"$\\sum {p1}$")
# p.add(Markdown("$\\int5$"))
# p.add("test")
# p.adisplay("test")
# p.add("$\\sum$")
# p.edisplay(" $\\sin(\\pi)$")



