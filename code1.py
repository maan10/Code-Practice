def tutter(word):
	return (2*(word[:2]+'... '))+word+'?'
    # return  word[0:2] +str(...)+word[0:2]+str(...)+word+'?'
print(tutter("incredible"))