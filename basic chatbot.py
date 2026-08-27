#basic chatbot generation 
#first make the function
def chatbot(user):
    if user==('hello'):
        return ' Bot=Hi!'
    elif user==('how are you'):
        return ' Bot=I am fine,thanks!'
    elif user==('bye'):
        return ' Bot=Goodbye!'
#use while loop after defining function and at the end brek it.
print("Welcome to bot!:")
while True:
    user=input('You=')
    response=chatbot(user)
    print(response)
    if user==('bye'):
        break