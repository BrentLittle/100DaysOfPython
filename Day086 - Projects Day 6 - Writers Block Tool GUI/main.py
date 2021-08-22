from tkinter import *

class Root:
    def __init__(self, second):
        self.second = second
        self.timer = None

        # Root
        self.root = Tk()
        self.root.title('Disappearing Text Writing App')
        self.root.config(padx=10, pady=10)
        
        # Frame
        self.frame = Frame(width=40, height=40, pady=5)
        self.frame.pack(fill='both', expand=True)
        
        # Scroll Bar
        self.scroll_bar = Scrollbar(self.frame)
        self.scroll_bar.pack(side='right', fill='y')
        
        # Text Box
        self.text_box = Text(self.frame, width=40, height=40, yscrollcommand=self.scroll_bar.set)
        self.text_box.pack(side='left', fill='both', expand=True)
        
        # Scroll to see text content
        self.scroll_bar.config(command=self.text_box.yview)
        
        # Focus cursor
        self.text_box.focus()
        
        # Autoscroll of text and scrollbar in text box
        self.text_box.see('end')
        
        # Make text box non-editable before start
        self.text_box.config(state='disabled')
        self.start_button = Button(text='Start', command=lambda: [self.start(), self.countdown()])
        self.start_button.pack(side='bottom')
        
        # Word label will initial after start
        self.label = None
        self.word_count = IntVar()
        
        self.root.mainloop()

    # Hide start button
    def start(self):
        self.text_box.config(state='normal')
        
        # Detect input in text box
        self.text_box.bind('<Key>', self.refresh)
        self.start_button.pack_forget()
        self.label = Label(textvariable=self.word_count)
        self.label.pack(side='bottom')
        self.word_count.set(f"{len(self.text_box.get('1.0', 'end').split())} words")

    # Count down <second> to erase content in text box
    def countdown(self):
        self.timer = self.root.after(self.second * 1000, func=self.erase)

    # Re countdown
    def refresh(self, event):
        self.root.after_cancel(self.timer)
        self.word_count.set(f"{len(self.text_box.get('1.0', 'end').split())} words")
        self.countdown()

    # Erase content in text box
    def erase(self):
        self.text_box.delete('1.0', 'end')
        self.word_count.set('No word ?')

app = Root(5)