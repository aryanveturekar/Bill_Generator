# code written in python 2.7
import os
import datetime
import ctypes
itemname=[]
amount=[]
qty=[]
rate=[]
ch='y'

os.system("title Bill Generator by Sandeep")

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t  Bill Generator\t\t\t\t\t  %I:%M:%S %p")
print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
print reg_format_date
print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'

def show():
	print '\nItemname\t\t\t\t'+'\tRate\t'+'Qty\t'+'Amount'
	for i in range(0,len(itemname)):
		print '{0}\t\t\t\t\t{1}\t{2}\t{3}'.format(itemname[i],rate[i],qty[i],amount[i])
	print '\nTotal amount:\t\t\t\t\t\t\t{0}'.format(sum(amount))

def errorhand(tempvalue):
	try:
		ctypes.windll.user32.MessageBoxA(0,"Please insert number","Oops",0)
		tempvalue=float(input('Input again: '))
	except:
		errorhand(tempvalue)
	return tempvalue


while ch=='y' or ch=='Y':
	tempitemname=raw_input('\nEnter item name (max 15 character): ')
	tempitemname=tempitemname[0:15]
	if len(tempitemname)<8:
		tempitemname=tempitemname+'        '
	itemname.append(tempitemname)
	tempamount=0
	tempqty=0
	tempa=0
	tempq=0

	try:
		tempamount=float(input('Enter rate: '))
		tempa=tempamount
	except:
		tempa=errorhand(tempamount)

	try:
		tempqty=input('Enter quantity: ')
		tempq=tempqty
	except:
		tempq=int(errorhand(tempqty))

	amount.append(tempq*tempa)
	qty.append(tempq)
	rate.append(tempa)
	show()
	ch=raw_input('\nDo you want to add more(y for yes and n for no): ')


print '\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n'
filename=raw_input('Enter filename to save: ')
fob=open(filename+'.txt','w+')
fob.write('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
filedatetime=d_date.strftime("  %d-%m-%Y\t\t\t\t\t  Bill Generator\t\t\t\t\t  %I:%M:%S %p")
fob.write(filedatetime)
fob.write('\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n')
fob.write('\t\t\tItemname\t\t\t\t'+'Rate\t'+'Qty\t'+'Amount\n')
for i in range(0,len(itemname)):
	fob.write('\n\t\t\t{0}\t\t\t\t{1}\t{2}\t{3}'.format(itemname[i],rate[i],qty[i],amount[i]))
fob.write('\n-----------------------------------------------------------------------------------------------------------------------')
fob.write('\n\t\t\tTotal amount:\t\t\t\t\t\t{0} Rs'.format(sum(amount)))
fob.write('\n-----------------------------------------------------------------------------------------------------------------------')
ctypes.windll.user32.MessageBoxA(0,"Bill Create successfully in a text file "+filename+".txt","Message",0)
