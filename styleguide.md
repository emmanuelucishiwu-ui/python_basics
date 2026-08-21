# Naming convention
## List out all the rule in each naming convention 
**Variables and function** 
***Rules for variable names***
1. Must start with a letter (A-Z or a-z)or an underscore(_).
*example: name = "Emmanuel" , _score = 90*
2. Cannot start with a nnumber
*example: 2name = "john"*
3. Can contain only:
- letters(a-z, A-Z)
- Numbers(0-9)
- underscore(_)
*example: student_age = 18*
4. Cannot contain spaces. 
* example: student age = 18 is wrong , student_age = 18 is correct*
5. cannot contains special characters like @,#,$,%,!,- etc
*example: student@age = 18*
6. Variables names are case-senssitive.
*example: age = 18, Age = 19, AGE = 25*`
7. Do not use python keywords as variable names 
*examples: if = 10 , class = "A"*
8. Use meaningful names. 
*example: student_name = "emmanuel" not x = "emmanuel"*

***Rules for function names***
1. follow the same naming rules as variables.
*def greet():*
    *print("Hello")*
2. Use lowercase letters.
*def calculate_total():*
    *pass*
3. Seperate multiple words with underscores(snake_case).
*def find_average():*
    *pass*
4. Choose descriptive names that explain what the function does.
*def print_receipt()*
    *pass*
5. Do not use Python keywords. 
*def for():*
    *pass*

***Rules for class names***
1. Must start with a letter (A–Z or a–z) or an underscore (_).
*class Student:*
    *pass*
2. Cannot start with a number.
*class 1Student:
    *pass   #wrong* 
3. Can contain only letters, numbers, and underscores (_).
*class Student1:*
    *pass*
4. Cannot contain spaces.
*class Student Record:*
    *pass   #wrong* 
5. Cannot contain special characters such as @, #, $, %, !, -, etc.
*class Student-Record:*
    *pass   #wrong* 
6. Class names are case-sensitive.
*class Student:*
    *pass*

*class student:*
    *pass*
These are two different class names.
7. Cannot use Python keywords as class names.
*class for:*
    pass   #wrong* 
8. Use meaningful and descriptive names.
*class BankAccount:*
    *pass*


***Ruels for constant names***
1. Must start with a letter (A–Z or a–z) or an underscore (_).
*PI = 3.14159      # correct* 
2. Cannot start with a number.
*2PI = 3.14159     # wrong*
3. Can contain only letters, numbers, and underscores (_).
*MAX_USERS = 100   #correct* 
4. Cannot contain spaces.
*MAX USERS = 100   # wrong* 
5. Cannot contain special characters like @, #, $, %, !, -, etc.
*MAX-USERS = 100   # wrong* 
6. Cannot use Python keywords.
*True = 1          # wrong* 
*class = "A"       # wrong*
7. Constant names are case-sensitive.
*PI = 3.14*
*Pi = 3.14*
*pi = 3.14*
These are three different names.
8. Use meaningful and descriptive names.
*MAX_SPEED = 120*
*DEFAULT_PORT = 8080*


***Rules For Package Names***
1. Use only lowercase letters. 
*mypackage*
2. Keep the name short and meaningful. 
*mathutils correct*
3. Avoid underscores if possible. 
*my package correct* 
*my_package wrong*
4. Must start with a letter or an underscore (_).
5. Cannot sdtart with a number.
*123 package wrong* 
6. Use only letters, numbers, and underscores(_)
7. Cannot contain spaces or special characters.
*my package wrong* 
*my_package wrong* 
8. Cannot use python keywords.
*import wrong *
*class  wrong*

Rules For Module Names
A module is simply a python file (.py).
1. Use only lowercase letters. 
*calculator.py correct* 
2. Seperate word with underscores if needed.
*student_record.py correct* 
3. Keep the name short and descriptive. 
4. Must start with a letter or an underscore(_)
5. Cannot start with a number. 
*1math.py wrong* 
6. Use only letters, numbers, and underscores(_)
7. Cannot contains spaces or special characters*. 
*my modulule.py wrong*
*my-module.py   wrong*
8. Cannot use Python keywords.
*for.py wrong*