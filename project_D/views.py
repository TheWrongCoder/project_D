from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request, 'home.html')

def count(request):
	fulltext = request.GET['fulltext']

	length = fulltext.split()

	word_coll = {}

	for word in length:
		if word in word_coll:
			word_coll[word] += 1
		else:
			word_coll[word] = 1  
	sortedw = sorted(word_coll.items(),key = operator.itemgetter(1),reverse = True)

	return render(request, 'a_page.html',{'fulltext':fulltext,'length':len(length), 'word_coll':sortedw})

def about(request):
    return render(request, 'about.html')


