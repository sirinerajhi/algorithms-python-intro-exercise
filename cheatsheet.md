# C# to Python cheat sheet

## Declaring a variable

C#:

    int numberOfStudents = 17;

Python:

    numberOfStudents = 17

## Output to terminal

C#:

    Console.WriteLine("text");

Python:

    print("text")

## Casting variables

C#:

    Convert.ToString(variable);

    Convert.ToInt32(variable);

    Convert.ToFloat(variable);

Python:

    int(variable)

    str(variable)

    float(variable)

## Operators

*C# == Python* for mathematical, compound, comparison and conditional operators:

    Math: '+' , '-' , '*' , '/' , '%' , '**' , '//'

    Compound: '+=' , '-=' , '*=' , '/=' , '%=' , '//=' , '**='

    Comparison: '==' , '!=' , '>' , '>=' , '<' , '<='

    Conditional: 'and' , 'or' , 'not'

'+' can also be used to concatenate strings

## Making decisions

### If-statement

C#:

    if(condition) {
        code to execute if true;
    }

    code after the if-statement;

Python:

    if condition:
        code to execute if true

    code after the if-statement

### If-else statement

C#:

    if(condition) {
        code to execute if true;
    } else {

    code to execute if false;
    }

    code after the if-statement;

Python:

    if condition:
        code to execute if true
    else:
        code to execute if not true

    code after the if-else statement

### If - elif - else statement

C#:

    if(condition) {
        code to execute if true;
    } else if (condition){
        code to execute if else condition is true;
    } else if (condition){
    code to execute if else condition is true;
    } 
    ... (add as many as needed)

    else {
        code to execute if all conditions return false;
    }

    code after the if-elif-else statement;

Python:

    if condition:
        code to execute if true
    elif condition:
        code to execute if elif condition is true
    elif condition:
        code to execute if elif condition is true

    ...(add as many as needed)

    else:
        code to execute if not true
    code after the if-statement

## Loops

### For loop

C#:

    for(initialization ; condition ; increment) {
        body of the for loop;
    }

Python:

    for varName in range(start,end,step-size):
        body of the for loop

### While loop

C#:

    while(condition){
        body of the while loop;
    }

Python:

    while <'condition'>:
        body of the while loop

## Lists

### Creating a list

C#:

    int[] numbers = {1,2,3,4,5};
    string[] names = {'Mark', 'Donna', 'Ella'};

Python:

    numbers = [1, 2, 3, 4, 5]
    names = ['Mark', 'Donna', 'Ella']

### Iterating over a list

C#:

    foreach (var name in names) {
        code to be executed;
    }

Python:

    for i in range(0,len(names)):
        code to be executed (e.g. print all elements)

### Adding items

C#:

    list[i] = newValue;

Python:

    list.append("value"[i])

## Classes

### Creating a class

C#

Done via a VS pre-made application

Python:

    class 'ClassName':

### Methods

C#:

    access_modifier static/not return_data_type NameOfTheMethod(arguments){
        body of the method;
        return data if necessary;
    }

Python:

    def name_of_method(self, 'arguments')

### Constructors

C#: (overloading is possible)

    public ClassName(arguments/or empty brackets){
        body of the constructor;
    }

Python: (overloading is not possible)

    def __init__(self, 'arguments'):
        initialization of the instance

### Creating objects

C#:

    ClassName objectName = new ClassName(arguments if needed);

Python:

    obj = ClassName()

### Assign or access variables

C#:

    access_modifier data_type attributeName = initial_value;

Python:

    self.__attributeName = 'value'

### Returning values from methods

C#:

(in body of the method)

    return 'returnValue';

Python:

(in body of the method)

    return 'returnValue'
