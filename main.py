def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    print(f"There is {count} words in this document.")
    text_l = text.lower()
    text_l=text_l.strip()
    d1={}
    d2={}
    
    

    d1 , d2 = count_letters(text_l)
    print (f"{d1}"+f"\n \n{d2}")
    



def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(txt):
    count = txt.split()
    return (len(count))

def count_letters (txt) :
    letter_count = {}
    for i in txt : 
        if i.isalpha() == False:
            continue
        if i in letter_count:
            letter_count[i] += 1 
        else :
            letter_count[i] = 1 
    
    letter_count_sorted_alpha = {k: v for k, v in sorted(letter_count.items())}
    letter_count_sorted_num = {k: v for k, v in sorted(letter_count.items(), key=lambda item: item[1] , reverse= True)}
    return letter_count_sorted_alpha , letter_count_sorted_num
    



main()