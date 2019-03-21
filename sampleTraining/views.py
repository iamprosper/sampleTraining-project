from django.shortcuts import render
import string

def home(request):
	return render(request,'home.html')

def count(request):
	#request the text
	text = request.GET['text']

	#Setting the dictionnary
	textDic = {}

	#Splitting the text
	itemsList = text.split()

	# list of new words in a comma-separated word
	other = []

	# # traversing all the items
	index = 0
	redo = False
	print("Before.... : ",end='')
	print(itemsList)

	while index < len(itemsList):
		item = itemsList[index]
		for char in item:
			print(char)
			if char in string.punctuation:
				item = item.replace(char,' ')
				other=item.split()
				redo = True
				break
		if not redo:
			index+=1
		else:
			redo = False
			for i in range(len(other)-1,-1,-1):
				itemsList.insert(index+1,other[i])
			itemsList.pop(index)
		print("\n***************************************\n")
		print("\nWorking on Other.... : ",end='')
		print(other)
		print("\n***************************************\n")
		print("\nWorking on ItemList.... : ",end='')
		print(itemsList)
		print("\n***************************************\n")
		# punc = item[len(item)-1]
		# if item[len(item)-1] in string.punctuation:
		# 	punc = item[len(item)-1]
		# 	itemsList[itemsList.index(item)] = item.strip(punc)
	#filling the dictionnary
	size = 0
	times = 0
	for item in itemsList:
		if len(item)>1:
			if item in textDic:
				textDic[item] += 1
			else:
				textDic[item] = 1
				size+=1
			times+=1

	return render(request,'count.html',{
		'textDic':textDic,
		'text':text,
		'size':size,
		'times':times,
		})

def splitItems(items):
	for item in string.punctuation:
		if item in items:
			items = items.split(item)
	return items

def about(request):
	return render(request,'about.html')