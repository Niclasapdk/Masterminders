from tkinter import *
from PIL import ImageTk, Image


class mainmenu():
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        self.root.geometry("800x600")
        self.root.configure(bg="royalblue2")
        self.img = Image.open("mastermind.png")
        self.imageSizeWidth, self.imageSizeHeight = self.img.size
        self.n=0.25
        self.newImageSizeWidth = int(self.imageSizeWidth * self.n)
        self.newImageSizeHeight = int(self.imageSizeHeight * self.n)
        self.image = self.img.resize((self.newImageSizeWidth, self.newImageSizeHeight), Image.ANTIALIAS)

        self.test = ImageTk.PhotoImage(self.image)

        self.titleimg = Label(self.root, image=self.test).place(relx=0.5, rely=0.19, anchor=CENTER)
        #self.Title = Label(self.root, text="MASTERMIND",font=("Times", "50", "bold"), bg="royalblue2", fg ="red4").place(relx=0.5, rely=0.2, anchor=CENTER)

        self.StartButton = Button(self.root, text="Start Game", command=self.start,font=("Arial", "25"), bg="black", fg ="white").place(relx=0.5, rely=0.45, anchor=CENTER)
        self.RuleButton = Button(self.root, text="Rules", command=self.rules,font=("Arial", "25"), bg="black", fg ="white").place(relx=0.5, rely=0.6, anchor=CENTER)

    def start(self):
        print("start has been pressed")
        Game(Toplevel(self.root))

    def rules(self):
        print("rules have been pressed")
        Rules(Toplevel(self.root))


class Rules(mainmenu):
    def __init__(self, root):
        self.root = root
        self.root.title("Rules")
        self.root.geometry("400x370")

        self.configfile = Label(self.root, width=45, height=20)
        self.text = open("Rules.txt")
        self.t = self.text.readlines()
        self.configfile.insert(END, self.t)




class Game(mainmenu):
    def __init__(self, root):
        self.root = root
        self.root.title("Game")
        self.root.geometry("400x370")


def main():
    root = Tk()
    app = mainmenu(root)
    root.mainloop()


if __name__ == "__main__":
    main()










def Main():
    pass



