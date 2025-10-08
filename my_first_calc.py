input_1 = float(input('Enter the first number:')) #here is the input 1 line(first number)
input_2 = float(input('Enter the second number:')) #here is the input 2 line(second number)


print('Good choice, but whats operation you need? Please, choise:') #choice, it`s all
print('1 Plus')
print('2 Minus')
print('3 Multiplication')
print('4 Division')


choice = input('Enter the number of operation:') #line for enter choice, nothing more


if choice == '1':              #plus var. condition for work
   result = input_1 + input_2
   print(f'Result: {input_1} + {input_2} = {result}')

elif choice == '2':            #minus var. condition for work
   result = input_1 - input_2
   print(f'Result: {input_1} - {input_2} = {result}')

elif choice == '3':            # multiplication var. condition for work
   result = input_1 * input_2
   print(f'Result: {input_1} * {input_2} = {result}')

elif choice == '4':             # division var. condition for work
   if input_2 != 0:
    result = input_1 / input_2
    print(f'Result: {input_1} / {input_2} = {result}')
   else:
      print('You cant division on zero! wth bro')

else:
   print('Uncorrect choise! Please try again.')
