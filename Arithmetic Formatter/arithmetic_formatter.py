#This is my solution to the Arithmetic Formatter Problem in FCC's Scientific Computing with Python.
#You can view the original question and my repl solution @ https://repl.it/@atelicious/FCC-Arithmetic-Formatter

def arithmetic_arranger(problems, show_ans=' '):
    # Initiates show answers to False
  show_answer_status = False

    # Checks if the user passed an argument for showing the answer
  if show_ans == ' ':
        show_answer_status = False
  elif show_ans == True:
        show_answer_status = True

    # Initiates lists where the numerator will go to first_num, operator to operation and denominator to second_num
  first_num = []
  operation = []
  second_num = []
  ans_list = []

    # Initiates the final string to be the return value
  numerator_string = ''
  slash = ''
  denominator_string = ''
  answer_string = ''

    # Checks whether the list is more than five problems
  if len(problems) > 5:
      return 'Error: Too many problems.'

  for values in problems:
      op_list = ['+', '-']
      x , y, z = values.split(' ')

        # Checks whether numbers are more than four digits
      if len(x) > 4 or len(z) > 4:
          return 'Error: Numbers cannot be more than four digits.'

        # Checks if operator is '+' or '-'
      if y not in op_list:
            return "Error: Operator must be '+' or '-'."

      if y == '+':
            # Checks whether the numbers can be casted to int or not
          try:
              ans = int(x) + int(z)
          except ValueError:
              return 'Error: Numbers must only contain digits.'
      elif y == '-':
            # Checks whether the numbers can be casted to int or not
          try:
              ans = int(x) - int(z)
          except ValueError:
            return 'Error: Numbers must only contain digits.'

      first_num.append(x)
      operation.append(y)
      second_num.append(z)
      ans_list.append(str(ans))


  for i in range(0, len(first_num)):
        # Creates the numerator , denominator, slash, and answer final string.
      if i in range(0, len(first_num)-1):
          numerator_string += first_num[i].rjust(2 + max(len(first_num[i]),len(second_num[i]))) + '    '
          denominator_string += operation[i] + second_num[i].rjust(1+ max(len(first_num[i]),len(second_num[i]))) + '    '
          slash += '--' +'-'*max(len(first_num[i]),len(second_num[i])) + '    '
          answer_string += ans_list[i].rjust(2 + max(len(first_num[i]),len(second_num[i]))) + '    '
      else:
          numerator_string += first_num[i].rjust(2 + max(len(first_num[i]),len(second_num[i])))
          denominator_string += operation[i] + second_num[i].rjust(1+ max(len(first_num[i]),len(second_num[i]))) 
          slash += '--' +'-'*max(len(first_num[i]),len(second_num[i]))
          answer_string += ans_list[i].rjust(2 + max(len(first_num[i]),len(second_num[i])))

  final_answer = numerator_string + '\n' + denominator_string + '\n' + slash 


  if show_answer_status == True:
      return final_answer +'\n' + answer_string
  else:
      return final_answer