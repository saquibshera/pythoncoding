numbers={
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine',
    '0':'zero'
}
output=''
getnumber=input("enter the number")
for number in getnumber:
    output+=numbers.get(number,number)+" "
print(output)

