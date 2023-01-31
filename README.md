# Y2_Project
## Money management project
This is a project where we had to use PyQT5 library to build an application. The project consists of 
3 different difficulty levels. I did the hardest one.

**EASY**
- Reading the transactions from a file
- Grouping stores based on users grouping
- Visualisation of the spending (not graphically)  

**MEDIUM**
- Easy requirements
- Interface and spending implemented graphically
- Unittests for at least part of the program

**HARD**
Medium requirements
- Ability to add new transaction records to the existing data (no need to be able to delete it afterwards)
- Saving A.I that takes the given data and user given amount that needs to be saved and modifies the data (deletes from set places) and adds savings into the graphs
 
  - The A.I needs to understand not to cut from mandatory spendings like rent
  - The program can be based on user given importance factors, but it needs to evaluate them itself too. It can generate importance from e.g amount of trips in records.  

##Libraries  

- CVS
- SYS
- Unittest
- PyQT5

##To Run the code  
 As the code is in Finnish here is a way to run the code.
- Run the Kuvaaja.py file
- It asks which file do you want to open
  - Input any of the following or a combination 
  - 1 is working
  - 2 is a test
  - 3 is a broken file
- Then input 0 to continue  

A graphical interface will open up which shows how much you've spent money
and how much you made. It showcases the 10 biggest expences you've had and the rest
can be found if you press MUUT button. If you want to add an expence press Meno and input 
the name of the company and the amount. If you want to add income press Tulo and input the amount
You can group multiple expences into one from lisää ryhmittely button. Select the expences and add a name for them
(i.e Alepa, Lidl, K-market => Groceries). The  code also has the A.I and you can change every
expences importance from Muuta tärkeyttä button. If you want to save money press Haluan säästää button 
and imput the amount. It cuts out the least important expences untill it has saved as much you want.
