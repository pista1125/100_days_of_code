#1. TK inter begining
# import tkinter
#
# window = tkinter.Tk()
# window.title("My first GUI program")
# window.minsize(width=500, height=300)
#
#
# my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
#
#
#
# window.mainloop()

#2. default values

# def my_function(a=1, b=2):
#     print(a,b)
#
# my_function()

#3. unlimited argument

# def my_funciton(*args):
#     #print(args[1])
#     add = 0
#     for n in args:
#         add += n
#     print(add)
# my_funciton(1,2,3,4)

#4. keyword arguments

# def calculate(n, **kwargs):
#     print(n)
#     # for key, argue in kwargs.items():
#     #     print(key)
#     #     print(argue)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
# calculate(5, add=3, multiply=5)

#5. keyworg with class

# class Car:
#     def __init__(self, **kw):
#         #self.make = kw["makes"]
#         #self.model = kw["models"]
#
#         #You will not give an error
#         self.make = kw.get("makes")
#         self.model = kw.get("models")
#
# my_car = Car(models="G Astra")
#
# print(my_car.model)