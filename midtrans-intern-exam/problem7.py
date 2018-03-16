num_of_input = input('Number of Inputs\t: ')
num_of_input = int(num_of_input)
usr_input1 = input()
name = []
if usr_input1 == 'add':
    for i in range(num_of_input):
        name.append(input('Name\t\t\t: '))
    usr_input2 = input()
    if usr_input2 == 'find':
        search2 = input('Find\t\t\t: ')
        count2 = 0
        output2 = 0
        for count2 in range(len(name)):
            if name[count2].startswith(search2):
                output2 = output2 + 1
            else:
                output2 = output2
        print('Number of name(s) starting with', search2, 'is', output2)
    else:
        print('Wrong input')
elif usr_input1 == 'find':
    search = input('Find\t\t\t: ')
    count = 0
    output = 0
    for count in range(len(name)):
        if name[count].startswith(search):
            output = output + 1
        else:
            output = output
    print('Number of name(s) starting with', search, 'is', output)
else:
    print('Wrong input')

