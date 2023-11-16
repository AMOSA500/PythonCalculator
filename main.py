from art import logo

print(logo)

def addition(n1,n2):
  return n1 + n2

def subtraction(n1,n2):
  return n1 - n2

def multiplication(n1,n2):
  return n1 * n2

def division(n1,n2):
  return round(n1 / n2, 2)
  

# Create a dictionary
operations = {
  "+": addition,
  "-":subtraction,
  "*":multiplication,
  "/":division
}

while True:
  try:
    num1 = int(input("What is your first number: "))
    num2 = int(input("What is your second number: "))
    s_no = 0
    for symbols in operations:
      s_no += 1
      print(f"{s_no}. {symbols}")
    operation_symbol = input("Enter your operation symbol: ")
    if operation_symbol in operations:
      calculator_function = operations[operation_symbol]
      answer = calculator_function(num1, num2)
  
      print(f"The {operations[operation_symbol].__name__} of {num1} and {num2} = {answer}")
      print("------RESTART-------")
      restart = int(input("1. Restart\n2. Quit\n"))
      if restart == 2:
        print("Thank you and GoodBye")
        break    
    else:
      print("Operator cannot be found")
  except ValueError as e:
    print(f"Integers only - {e}")