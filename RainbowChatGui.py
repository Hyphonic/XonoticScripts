import colour, pyperclip
from tkinter import ttk
import tkinter as Tk

# Config
DarkMode = True # Recommended.
RemoveWindowBorder = False # Not recommended :>

def Convert(Message, Color1, Color2):
    Red = colour.Color(Color1) # The first color in the range.
    Green = colour.Color(Color2) # The last color in the range.
    Ranges = list(Red.range_to(Green, len(Message)))
    RangeList = []
    for Letter in Message:
        Range = Ranges.pop(0)
        Range = list(Range.hex_l)[1:]
        Range = Range[0:1], Range[2:3], Range[4:5]
        Range = ''.join((''.join(Range[0]), ''.join(Range[1]), ''.join(Range[2])))
        Range = '^x'+Range+Letter
        RangeList.append(Range)
    pyperclip.copy('Say '+''.join(RangeList))

Root = Tk.Tk()
Root.title('Xonotic Rainbow Chat')
Root.geometry('250x300')
Root.wm_attributes('-topmost', 1)
Root.resizable(False, False)
Root.iconphoto(False, Tk.PhotoImage(file='Theme/Icon.png')) # Credits to Octicons for the icon.
Root.overrideredirect(RemoveWindowBorder)
Root.tk.call('source', 'Azure.tcl')
Root.tk.call('set_theme', 'dark' if DarkMode == True else 'light')
Frame = ttk.Frame(Root, relief='flat', borderwidth=0)
Frame.pack(fill='both', expand=True)
MessageBox = ttk.Entry(Frame)
ComboBox1 = ttk.Combobox(Frame, values=open('Colors.txt', 'r').read().splitlines())
ComboBox2 = ttk.Combobox(Frame, values=open('Colors.txt', 'r').read().splitlines())
ConvertButton = ttk.Button(Frame, text='Convert', command=lambda: Convert(Message=MessageBox.get(), Color1=ComboBox1.get(), Color2=ComboBox2.get()))
ComboBox1.current(0)
ComboBox2.current(0)
MessageBox.grid(sticky='n', row=0, column=0)
ConvertButton.grid(sticky='n', row=0, column=1)
ComboBox1.grid(sticky='n', row=1, column=0)
ComboBox2.grid(sticky='n', row=2, column=0)
Root.mainloop()