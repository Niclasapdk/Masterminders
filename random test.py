import Logik
import webbrowser
from tkinter import *

from PIL import ImageTk, Image

# Variables used for game

turncount = 0
width = 4
height = 10
def Board(width, height):
    board = [[None] * width for _ in range(height)]
    return board
labels1 = []
labelswhite = []
labelsred = []
logik = Logik.MastermindLogik()
code = logik.randomkode(4)


class SampleApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        # container.grid(sticky="N",ipadx = "200", ipady="200")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        if page_name == "StartPage":
            self.title("Main Menu")
            self.geometry("800x600")
        else:
            self.title("Game")
            self.geometry("455x900")
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()


def Rules():
    # Opens a notepad with the rules
    print("rules have been pressed")
    webbrowser.open("Rules.txt")


def on_click(i, j, event):
    global turncount
    colors = ["grey", "red", "purple", "blue", "yellow", "green", "orange", "white", "pink"]
    # finder værdierne til det label man trykkede på
    lblcolor = event.widget.cget("bg")
    lblnumber = event.widget.cget("text")
    tilex = event.widget.grid_info()["column"]
    tiley = event.widget.grid_info()["row"]
    config = event.widget.config
    print("Color:", lblcolor, ", Tile column:", tilex, ", Tile row:", tiley)

    if 5 > tilex > 0 and tiley == turncount:
        print("Valid pick")
        if lblnumber == 8:
            lblnumber = 1
        else:
            lblnumber = int(lblnumber) + 1
        config(text=lblnumber)
        config(bg=colors[int(lblnumber)])


def check():
    global turncount, labels1, labelswhite, labelsred, logik, code
    # print(labels1)
    print("check")
    checklblnum = []
    checklblcol = []
    if turncount < 10:
        for i in range(4):
            num = i + ((1 + turncount) * 4) - 4
            # print(num)
            checklblcol.append(labels1[num].cget("bg"))
            checklblnum.append(labels1[num].cget("text"))
        # print(checklblnum, checklblcol)
        guess = checklblnum
        print("Guess:", guess)
        print("Code:", code)
        result = logik.match(code, guess)
        print("How close:", result)

        check = result.count("check")

        labelsred[turncount].config(text=result.count("check"))
        labelswhite[turncount].config(text=result.count("half"))
        if check == 4:
            Winner = Tk()
            lbl = Label(Winner, text="You won!")
            lbl.grid(row=1, column=1)
            done = Button(Winner, text="Quit", command=winner)
            done.grid(row=2, column=1)
        turncount += 1


def winner():
    # SampleApp.show_frame("StartPage")
    SampleApp.destroy()
    SampleApp.__init__()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="royalblue2")
        self.img = Image.open("mastermind.png")
        self.imageSizeWidth, self.imageSizeHeight = self.img.size
        self.n = 0.25
        self.newImageSizeWidth = int(self.imageSizeWidth * self.n)
        self.newImageSizeHeight = int(self.imageSizeHeight * self.n)
        self.image = self.img.resize((self.newImageSizeWidth, self.newImageSizeHeight), Image.ANTIALIAS)

        self.test = ImageTk.PhotoImage(self.image)

        self.titleimg = Label(self, image=self.test).place(relx=0.5, rely=0.19, anchor=CENTER)
        # self.Title = Label(self.root, text="MASTERMIND",font=("Times", "50", "bold"), bg="royalblue2", fg ="red4").place(relx=0.5, rely=0.2, anchor=CENTER)

        self.StartButton = Button(self, text="Start Game", command=lambda: controller.show_frame("PageOne"),
                                  font=("Arial", "25"), bg="black",
                                  fg="white").place(relx=0.5, rely=0.45, anchor=CENTER)
        self.CustumButton = Button(self, text="Custom Game", command=self.custom, font=("Arial", "25"), bg="black",
                                   fg="white").place(relx=0.5, rely=0.575, anchor=CENTER)
        self.RuleButton = Button(self, text="Rules", command=Rules, font=("Arial", "25"), bg="black",
                                 fg="white").place(relx=0.5, rely=0.7, anchor=CENTER)

        # button1 = Button(self, text="Go to Page One",
        # command=lambda: controller.show_frame("PageOne"))
        # button1.pack()

    def custom(self):
        self.customize = Tk()
        Label(self.customize, text="Code Length").grid(row=0, column=1)
        self.codelength = Entry(self.customize)
        self.codelength.grid(row=1, column=1)
        Label(self.customize, text="Attempts").grid(row=2, column=1)
        self.attempts = Entry(self.customize)
        self.attempts.grid(row=3, column=1)
        done = Button(self.customize, text="Done", command=self.done).grid(row=4, column=1)

    def done(self):
        self.width2 = int(self.codelength.get())
        self.height2 = int(self.attempts.get())

        self.update_idletasks()
        self.controller.show_frame("PageTwo")
        PageTwo.build()
        self.customize.destroy()



class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="royalblue2")
        board = Board(width,height)
        label = Label(self, text="This is page 1")
        label.place(x=10, y=860)
        button = Button(self, text="Go to the start page",
                        command=lambda: controller.show_frame("StartPage"))
        button.place(x=10, y=830)

        for i, row in enumerate(board):
            for j, column in enumerate(row):
                lbl = Label(self, text="0", bg='grey', relief="groove")
                labels1.append(lbl)
                k = len(labels1) - 1
                labels1[k].bind('<Button-1>', lambda e, i=i, j=j: on_click(i, j, e))
                labels1[k].grid(row=i, column=1 + j)
                labels1[k].config(width=10, height=5)

        for i, row in enumerate(board):
            lbl2 = Label(self, text="hvid", bg='white', relief="groove")
            labelswhite.append(lbl2)
            k = len(labelswhite) - 1
            labelswhite[k].grid(row=i, column=0)
            labelswhite[k].config(width=10, height=5)

        for i, row in enumerate(board):
            lbl3 = Label(self, text="rød", bg='red', relief="groove")
            labelsred.append(lbl3)
            k = len(labelsred) - 1
            labelsred[k].grid(row=i, column=5)
            labelsred[k].config(width=10, height=5)

        button = Button(self, text="Check", command=check)
        button.place(x=400, y=830)

class PageTwo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="royalblue2")
        label = Label(self, text="This is page 2")
        label.place(x=10, y=860)
        button = Button(self, text="Go to the start page",
                        command=lambda: controller.show_frame("StartPage"))
        button.place(x=10, y=830)

    def build(self):
        board2 = Board(self.controller.width2, self.controller.height2)
        for i, row in enumerate(board2):
            for j, column in enumerate(row):
                lbl = Label(self, text="0", bg='grey', relief="groove")
                labels1.append(lbl)
                k = len(labels1) - 1
                labels1[k].bind('<Button-1>', lambda e, i=i, j=j: on_click(i, j, e))
                labels1[k].grid(row=i, column=1 + j)
                labels1[k].config(width=10, height=5)

        for i, row in enumerate(board2):
            lbl2 = Label(self, text="hvid", bg='white', relief="groove")
            labelswhite.append(lbl2)
            k = len(labelswhite) - 1
            labelswhite[k].grid(row=i, column=0)
            labelswhite[k].config(width=10, height=5)

        for i, row in enumerate(board2):
            lbl3 = Label(self, text="rød", bg='red', relief="groove")
            labelsred.append(lbl3)
            k = len(labelsred) - 1
            labelsred[k].grid(row=i, column=5)
            labelsred[k].config(width=10, height=5)

        button = Button(self, text="Check", command=check)
        button.place(x=400, y=830)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
