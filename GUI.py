import Logik
import webbrowser
from tkinter import *

from PIL import ImageTk, Image

# Variables used for game
turncount = 0
width = 4
height = 10
labels1 = []
labelswhite = []
labelsred = []
labels2 = []
labelswhite2 = []
labelsred2 = []
logik = Logik.MastermindLogik()
code = logik.randomkode(width)


def boardcreate(width, height):
    board = [[None] * width for _ in range(height)]
    return board


def Rules():
    # Opens a notepad with the rules
    print("rules have been pressed")
    webbrowser.open("Rules.txt")


# Function that runs when clicking on a label
def on_click(i, j, event, width):
    global turncount
    colors = ["grey", "red", "purple", "blue", "yellow", "green", "orange", "white", "pink"]
    # Finds the values of the label
    lblcolor = event.widget.cget("bg")
    lblnumber = event.widget.cget("text")
    tilex = event.widget.grid_info()["column"]
    tiley = event.widget.grid_info()["row"]
    config = event.widget.config
    # print("Color:", lblcolor, ", Tile column:", tilex, ", Tile row:", tiley)

    if width >= tilex > 0 and tiley == turncount:
        print("Valid pick")
        if lblnumber == 8:
            lblnumber = 1
        else:
            lblnumber = int(lblnumber) + 1
        config(text=lblnumber)
        config(bg=colors[int(lblnumber)])


def check(labels1, labelswhite, labelsred, logik, code, width, height):
    global turncount
    # print(labels1)
    print("check")
    checklblnum = []
    checklblcol = []
    if turncount < height:
        for i in range(width):
            num = i + ((1 + turncount) * width) - width
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
        turncount += 1
        if check == width:
            Winner = Tk()
            lbl = Label(Winner, text="You won!")
            lbl.grid(row=1, column=1)
            done = Button(Winner, text="Quit", command=winner)
            done.grid(row=2, column=1)
        elif turncount == height:
            Loser = Tk()
            lbl = Label(Loser, text="You lost!")
            lbl.grid(row=1, column=1)
            done = Button(Loser, text="Quit", command=winner)
            done.grid(row=2, column=1)


def winner():
    exit()


class SampleApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # the container is where we'll stack a bunch of frames on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location the one on the top of the stacking order will be the one that
            # is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        if page_name == "StartPage":
            self.title("Main Menu")
            self.geometry("800x600")
        elif page_name =="PageTwo":
            self.title("Custom")
            self.geometry("250x900")
        else:
            self.title("Game")
            self.geometry("456x900")
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()

    def custom(self, width):
        width = (2 + width) * 76
        self.geometry("{}x900".format(width))


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

        self.StartButton = Button(self, text="Start Game", command=lambda: controller.show_frame("PageOne"),
                                  font=("Arial", "25"), bg="black",
                                  fg="white").place(relx=0.5, rely=0.45, anchor=CENTER)
        self.CustomButton = Button(self, text="Custom Game", command=lambda: controller.show_frame("PageTwo"),
                                   font=("Arial", "25"), bg="black",
                                   fg="white").place(relx=0.5, rely=0.575, anchor=CENTER)
        self.RuleButton = Button(self, text="Rules", command=Rules, font=("Arial", "25"), bg="black",
                                 fg="white").place(relx=0.5, rely=0.7, anchor=CENTER)
        self.QuitButton = Button(self, text="Exit", command=winner, font=("Arial", "25"), bg="black",
                                 fg="white").place(relx=0.5, rely=0.825, anchor=CENTER)


class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="royalblue2")
        board = boardcreate(width, height)
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
                labels1[k].bind('<Button-1>', lambda e, i=i, j=j: on_click(i, j, e, width))
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

        button = Button(self, text="Check",
                        command=lambda: check(labels1, labelswhite, labelsred, logik, code, width, height))
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
        self.codelengthtxt = Label(self, text="Code Length")
        self.codelengthtxt.grid(row=0, column=1)
        self.codelength = Entry(self)
        self.codelength.grid(row=1, column=1)
        self.attemptstxt = Label(self, text="Attempts")
        self.attemptstxt.grid(row=2, column=1)
        self.attempts = Entry(self)
        self.attempts.grid(row=3, column=1)

        self.done = Button(self, text="Done", command=self.test)
        self.done.grid(row=4, column=1)

    def test(self):
        if 0 < int(self.codelength.get()) < 8 and int(self.attempts.get()) > 0:
            self.width2 = int(self.codelength.get())
            self.height2 = int(self.attempts.get())
            self.build()
        else:
            error = Tk()
            Label(error, text="Code lenght must be between 1 and 8, and height greater than 0").grid(row=1, column=1)

    def build(self):
        width2 = self.width2
        height2 = self.height2
        self.attempts.destroy()
        self.codelength.destroy()
        self.attemptstxt.destroy()
        self.codelengthtxt.destroy()
        self.controller.custom(width2)
        self.done.destroy()
        code2 = logik.randomkode(width2)
        board2 = boardcreate(width2, height2)
        for i, row in enumerate(board2):
            for j, column in enumerate(row):
                lbl = Label(self, text="0", bg='grey', relief="groove")
                labels2.append(lbl)
                k = len(labels2) - 1
                labels2[k].bind('<Button-1>', lambda e, i=i, j=j: on_click(i, j, e, width2))
                labels2[k].grid(row=i, column=1 + j)
                labels2[k].config(width=10, height=5)

        for i, row in enumerate(board2):
            lbl2 = Label(self, text="hvid", bg='white', relief="groove")
            labelswhite2.append(lbl2)
            k = len(labelswhite2) - 1
            labelswhite2[k].grid(row=i, column=0)
            labelswhite2[k].config(width=10, height=5)

        for i, row in enumerate(board2):
            lbl3 = Label(self, text="rød", bg='red', relief="groove")
            labelsred2.append(lbl3)
            k = len(labelsred2) - 1
            labelsred2[k].grid(row=i, column=width2 + 1)
            labelsred2[k].config(width=10, height=5)

        button = Button(self, text="Check",
                        command=lambda: check(labels2, labelswhite2, labelsred2, logik, code2, width2, height2))
        button.grid(row=(height2 + 2), column=width2)


app = SampleApp()
app.mainloop()
