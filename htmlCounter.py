import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup 

#read the html file 
u = input("Enter a url: ") 
h = urllib.request.urlopen(u).read()
s = BeautifulSoup(h, "html.parser")

#find the numbers and append them in a list 
g = s('span') 
l = []

for i in g: 
    for v in i.contents: 
        l.append(int(v))

#count the total and how many numbers in a file 
t = 0 
c = 0 

for n in l: 
    c += 1 
    t += n 

#print the result 
print("The sum of numbers in this HTML file: ", t) 
print("There is", c, "Number in this HTML file.")