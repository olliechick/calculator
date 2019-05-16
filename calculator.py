# This was a GUI calculator I created using Python 3 and tkinter as part of an NCEA Level 3 assessment in 2015.
# Author: Ollie Chick - github.com/olliechick and olliechick.co.nz

from tkinter import *#imports everything from tkinter
from tkinter import ttk#imports the ttk skin, so it conforms with the design standards of the operating system it is running on

root = Tk()#sets up the main window
root.title("Calculator")#gives the window a title so the user knows instantly what the program is

class GUI:
    def __init__(self):
        #Declaring variables
        self.math=Math()#starts an instance of Math (named math) in this class (GUI)
        self.whereUserEditing="first operand"#tells the program that the user is entering the first operand
        self.intodecimal=False#tells the program that the user has not yet clicked the decimal point while entering the current operand
        self.equationarray=[]#creates an empty array, this is used to store what is displayed in the IO box (after being coverted to a string)
        self.firstOperandHasDecimal=False#tells program that the user has not put a decimal point in the first operand

        #Sets up mainframe
        mainframe = ttk.Frame(root, padding="5")#creates frame (named mainframe) in root, with a padding of 5 pixels inside the frame on each side (left, top, right and bottom)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        #IO box
        self.outputLabel = ttk.Label(mainframe, text = "0")#creates the label (named outputLabel), puts it in mainframe and displays a preliminary string of 0
        self.outputLabel.grid(column =1, columnspan = 4, row=1, sticky = 'E')#puts outputLabel at the top-right, stretches it across the entire row, and aligns it to the right

        #BUTTONS
        #backspace
        backspacebutton = ttk.Button(mainframe, text="<-", width=5, command=self.pushbackspace)#creates a button (named backspacebutton), puts it in mainframe, displays <- on it, restricts it to 5 units wide, and when pushed it will run the function pushbackspace
        backspacebutton.grid(column=1, row=2)#puts the button in the left column on the second row down
        #clear
        clearbutton = ttk.Button(mainframe, text="CE", width=5, command=self.pushclear)
        clearbutton.grid(column=2, row=2)
        #equals
        equalsbutton = ttk.Button(mainframe, text="=", width=10, command=self.pushequals)
        equalsbutton.grid(column=3, row=2, columnspan=2, sticky = 'WE')
        #divide
        self.dividebutton = ttk.Button(mainframe, text="/", width=5, command=self.pushdivide)
        self.dividebutton.grid(column=4, row=3)
        #multiply
        self.multiplybutton = ttk.Button(mainframe, text="*", width=5, command=self.pushmultiply)
        self.multiplybutton.grid(column=4, row=4)
        #minus
        self.minusbutton = ttk.Button(mainframe, text="-", width=5, command=self.pushminus)
        self.minusbutton.grid(column=4, row=5)
        #plus
        self.plusbutton = ttk.Button(mainframe, text="+", width=5, command=self.pushplus)
        self.plusbutton.grid(column=4, row=6)
        #decimal point
        decimalbutton = ttk.Button(mainframe, text=".", width=5, command=self.pushdecimal)
        decimalbutton.grid(column=3, row=6)
        #0
        zerobutton = ttk.Button(mainframe, text="0", width=10, command=self.pushzero)
        zerobutton.grid(column=1, row=6, columnspan=2, sticky = 'WE')
        #1
        onebutton = ttk.Button(mainframe, text="1", width=5, command=self.pushone)
        onebutton.grid(column=1, row=5)
        #2
        twobutton = ttk.Button(mainframe, text="2", width=5, command=self.pushtwo)
        twobutton.grid(column=2, row=5)
        #3
        threebutton = ttk.Button(mainframe, text="3", width=5, command=self.pushthree)
        threebutton.grid(column=3, row=5)
        #4
        fourbutton = ttk.Button(mainframe, text="4", width=5, command=self.pushfour)
        fourbutton.grid(column=1, row=4)
        #5
        fivebutton = ttk.Button(mainframe, text="5", width=5, command=self.pushfive)
        fivebutton.grid(column=2, row=4)
        #6
        sixbutton = ttk.Button(mainframe, text="6", width=5, command=self.pushsix)
        sixbutton.grid(column=3, row=4)
        #7
        sevenbutton = ttk.Button(mainframe, text="7", width=5, command=self.pushseven)
        sevenbutton.grid(column=1, row=3)
        #8
        eightbutton = ttk.Button(mainframe, text="8", width=5, command=self.pusheight)
        eightbutton.grid(column=2, row=3)
        #9
        ninebutton = ttk.Button(mainframe, text="9", width=5, command=self.pushnine)
        ninebutton.grid(column=3, row=3)

        #STYLES
        style = ttk.Style() #Calls a style theme from tkinter in the variable style so I can modify it
        style.configure("selected.TButton", background="blue", foreground="blue") #creates a style called "Blue.TButton" which has a blue background and foreground so I can apply this style to the selected operator button when it is clicked

    #Functions
    def pushclear(self):
        self.whereUserEditing="first operand"#tells the program that the user is entering the first operand
        self.intodecimal=False#tells the program that the user has not yet clicked the decimal point while entering the current operand
        self.firstOperandHasDecimal=False#tells program that the user has not put a decimal point in the first operand
        self.equationarray=[]#clears out the equationarray
        self.updateIO("0")#puts a zero in the equationarray
        self.math.pushclear()#runs logic
    def pushbackspace(self):
        self.updateIO('backspace')
        self.math.pushbackspace()#runs logic
    def pushzero(self):
        self.updateIO("0")#appends a zero to the equationarray
        self.math.numberclick(0)#runs logic
    def pushone(self):
        self.updateIO("1")
        self.math.numberclick(1)
    def pushtwo(self):
        self.updateIO("2")
        self.math.numberclick(2)
    def pushthree(self):
        self.updateIO("3")
        self.math.numberclick(3)
    def pushfour(self):
        self.updateIO("4")
        self.math.numberclick(4)
    def pushfive(self):
        self.updateIO("5")
        self.math.numberclick(5)
    def pushsix(self):
        self.updateIO("6")
        self.math.numberclick(6)
    def pushseven(self):
        self.updateIO("7")
        self.math.numberclick(7)
    def pusheight(self):
        self.updateIO("8")
        self.math.numberclick(8)
    def pushnine(self):
        self.updateIO("9")
        self.math.numberclick(9)
    def pushdecimal(self):
        if self.intodecimal==False:#if the user has not yet clicked . whilst entering the current operand
            self.updateIO(".")#appends . to the equationarray
            self.math.pushdecimal()#runs logic
        else:#if the user has already clicked . whilst entering the current operand
            print ('Sorry, you cannot click the decimal point more than once per operand.')#sends this error message to the console
        self.intodecimal=True#tells the program that the user has entered a decimal point, so they won't be able to enter another until intodecimal has been made False again
    def pushplus(self):
        if self.whereUserEditing=="first operand":
            self.plusbutton.configure(style="selected.TButton")
            self.minusbutton.configure(style="TButton")
            self.multiplybutton.configure(style="TButton")
            self.dividebutton.configure(style="TButton")
        self.pushoperator("plus", "+")
    def pushminus(self):
        if self.whereUserEditing=="first operand":
            self.plusbutton.configure(style="TButton")
            self.minusbutton.configure(style="selected.TButton")
            self.multiplybutton.configure(style="TButton")
            self.dividebutton.configure(style="TButton")
        self.pushoperator("minus", "-")
    def pushmultiply(self):
        if self.whereUserEditing=="first operand":
            self.plusbutton.configure(style="TButton")
            self.minusbutton.configure(style="TButton")
            self.multiplybutton.configure(style="selected.TButton")
            self.dividebutton.configure(style="TButton")
        self.pushoperator("multiply", "*")
    def pushdivide(self):
        if self.whereUserEditing=="first operand":
            self.plusbutton.configure(style="TButton")
            self.minusbutton.configure(style="TButton")
            self.multiplybutton.configure(style="TButton")
            self.dividebutton.configure(style="selected.TButton")
        self.pushoperator("divide", "/")
    def pushoperator(self, operatorName, operatorSymbol):
        if self.intodecimal==True:#if the user has entered a decimal
            self.firstOperandHasDecimal=True#tells program that the user not put a decimal point in the first operand
        self.intodecimal=False#tells the program that the user can enter a decimal point
        if self.whereUserEditing=="first operand":
            self.updateIO(operatorSymbol)
            self.math.operatorclicked(operatorName)
            self.whereUserEditing="second operand"
        elif self.whereUserEditing=="operator" or self.whereUserEditing=="second operand" or self.whereUserEditing=="solution":
            print ("you can't have more than one operator.")
        else:
            print ('Not quite sure how you managed this (having self.whereUserEditing!="first operand", "second operand", "operator", or "solution").')

    def pushequals(self):
        self.math.pushequals()#runs logic
        self.solution=(self.math.returnsolution())#gets the solution from the math instance of the Math class and stores it in self.solution
        if self.solution=="error":
            pass
        else:
            self.updateIO("="+str(self.solution))#appends = then the solution (in string form) to the IO box (eg an entry could be '=42')
            self.whereUserEditing="solution"#tells the program not to let the user input anything more
    def updateIO(self,buttonclicked):
        stringToOutput=""#declards the variable and sets it to an empty string, this is so it can be added to and displayed in the IO box
        if self.whereUserEditing=="first operand" or self.whereUserEditing=="operator" or self.whereUserEditing=="second operand" or buttonclicked=='backspace':#if equals hasn't been pressed yet or backspace was clicked
            if buttonclicked=='backspace' and self.equationarray!=[]:#if backspace was clicked and equationarray isn't empty
                if self.whereUserEditing=='solution':#if the equation had been solved
                    self.whereUserEditing="second operand"#tell the program that the equation has not been solved anymore
                if self.equationarray[-1] == "+" or self.equationarray[-1] == "-" or self.equationarray[-1] == "*" or self.equationarray[-1] == "/":#if the last item in the equationarray is (was) an operator
                    self.whereUserEditing='operator'#tells the program that the user can enter an operator
                    if self.firstOperandHasDecimal==True:#if the first operand has a decimal
                        self.intodecimal=True#the user can't enter a decimal point
                    else:#if the first operand doesn't have a decimal
                        self.intodecimal=False#the user can enter a decimal point
                if self.equationarray[-1]==".":#if the last item in the equation array is (was) .
                    self.intodecimal=False#the user can enter a decimal point
                    if self.whereUserEditing=="first operand":#if the user is creating the first operand
                        self.firstOperandHasDecimal=False#tell the program that the user no longer has a decimal point in the first operand
                if self.whereUserEditing=="operator":#if the user had just deleted the operator
                    self.whereUserEditing="first operand"#tells the program that the user
                del self.equationarray[-1]#delete the last item in equationarray
            elif buttonclicked=='backspace' and self.equationarray==[]:#if backspace was clicked but equationarray is empty
                pass#do nothing
            else:#if something other than backspace was clicked
                if self.equationarray == ['0']:#if there is just a 0 in the IO box:
                    self.equationarray = []#deletes that 0 from the equationarray, so the equation will be displayed as e.g. 1+1=2 instead of 01+1=2
                self.equationarray.append(buttonclicked)#add the button clicked to the equationarray
            for n in range(len(self.equationarray)):#loop once for every item in equationarray
                stringToOutput = stringToOutput + self.equationarray[n] #puts all the items in self.equationarray sequentially into the string stringToOutput
            self.outputLabel.config(text=stringToOutput)#displays stringToOutput in the IO box
        elif self.whereUserEditing=="solution" and buttonclicked!='backspace':#if the user is trying to input after solving the equation
            print ('Sorry, you cannot enter values once you have clicked equals. Please click CE to start a new equation or <- to delete the result and continue editing.')

class Math:
    def __init__(self):
        #Declaring variables
        self.numberUserEditing="first operand"#tells the program that the user is entering the first operand
        self.firstOperand="0"#these two lines set...
        self.secondOperand="0"#...both operands to 0
        self.firstOperandFloat=0
        self.secondOperandFloat=0
        self.solution=0
        self.operator="nothing"

        #Functions
    def numberclick(self, pushed):
        if self.numberUserEditing=="first operand":#if the user is editing the first operand
            if self.firstOperand=="0":#if the first operand is 0
                self.firstOperand=str(pushed)#set the first operand to a string of the number pushed, so you end up with 16 not 016
            else:
                self.firstOperand=self.firstOperand+str(pushed)#appends the number pushed to the existing number in string form
        elif self.numberUserEditing=='operator' or self.numberUserEditing=="second operand":#if the user is editing the second operand
            if self.secondOperand=="0":#if the second operand is 0
                self.secondOperand=str(pushed)#set the second operand to a string of the number pushed, so you end up with 16 not 016
            else:
                self.secondOperand=self.secondOperand+str(pushed)#appends the number pushed to the existing number in string form
        elif self.numberUserEditing=="solution":#if the user has clicked =
            print ('Sorry, you cannot enter values once you have clicked equals. Please click CE to start a new equation or <- to delete the result and continue editing.')
        else:
            print ('Not quite sure how you managed this (having self.numberUserEditing!="first operand", "second operand", "operator", or "solution").')
    def operatorclicked(self, operator):
        self.numberUserEditing="second operand"#doesn't let the user enter another operand
        self.operator=operator#sets the classwide variable operator to the operator clicked, so when equals is clicked the program knows what to do with the two operands
    def pushbackspace(self):
        if self.numberUserEditing=="solution":#if the user has clicked =
            self.numberUserEditing='second operand'#the user is now editing the second operand
        elif self.numberUserEditing=="second operand":#if the user was editing the second operand
            self.secondOperand = (self.secondOperand)[:-1]#take the last character off the second operand
            if self.secondOperand=="":#if the second operand is empty
                self.numberUserEditing='operator'#the user is now editing the operator, so the program won't need
                self.secondOperand="0"#sets the second operator to 0 to avoid errors if the program tries to float it
        elif self.numberUserEditing=="operator":#if the user is deleting the operator
            self.numberUserEditing='first operand'#the user is now editing the first operand
            self.operator="nothing"#the user hasnt selected an operator
        elif self.numberUserEditing=="first operand":
            self.firstOperand = (self.firstOperand)[:-1]
    def pushclear(self):
        self.numberUserEditing="first operand"#tells the program that the user is going to enter the first operand
        self.firstOperand="0"
        self.secondOperand="0"
        self.operator="nothing"
    def pushequals(self):
        try:
            self.firstOperandFloat=float(self.firstOperand)
        except:
            self.firstOperandFloat=0
        try:
            self.secondOperandFloat=float(self.secondOperand)
        except:
            pass
        if self.operator=="plus":
            try:
                self.solution=self.firstOperandFloat+self.secondOperandFloat#adds the two operands to get the result
            except:
                print("Math error")
                self.solution="error"
        elif self.operator=="minus":
            try:
                self.solution=self.firstOperandFloat-self.secondOperandFloat#takes the second operand away from the first to get the result
            except:
                print("Math error")
                self.solution="error"
        elif self.operator=="multiply":
            try:
                self.solution=self.firstOperandFloat*self.secondOperandFloat#multiplies the two operands to get the result
            except:
                print("Math error")
                self.solution="error"
        elif self.operator=="divide":
            try:
                self.solution=self.firstOperandFloat/self.secondOperandFloat#divides the first operand by the second to get the result
            except ZeroDivisionError:
                self.solution="\u221e"
            except:
                print("Math error")
        else:
            try:
                self.solution=self.firstOperandFloat
            except:
                print ('Please enter something before clicking =')
        self.numberUserEditing='solution'
    def returnsolution(self):
        return str(self.solution)
    def pushdecimal(self):
        self.numberclick('.')

GUI()
root.mainloop()#starts the program going
