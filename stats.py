

def get_book_text( filepath ):
    with open(filepath) as fd:
        text = fd.read()
    return text

def word_count( text ):
    word_list = text.split()
    return len(word_list)

def token_count( mydict, words ):
    for i in words:
        ii = i.lower()
        if ii not in mydict:
            mydict[ii] = 1
        else:
            mydict[ii] += 1
    return mydict

def convert2list( mydict):
    mylist = []
    for i in mydict.keys():
        if not( i.isalpha() ):
            pass
        else: 
            mylist.append( { "character" : i, "count" : mydict[i] })
    mylist.sort( key=lambda mylist: mylist["count"], reverse=True)
    return mylist

#def print_report( mylist ):

