def longest_word(sentence):
    word_list = sentence.split()
    special_characters = (" !@#$%^&*(){}[]?/<>,._-\|~`:;=+'")
    onlywords = []
    
    for i in word_list:
        onlywords.append(i.strip(special_characters))
    
    only_characters = []
    for i in onlywords:
        only_characters.append(i.replace("'", ""))
    
    print(only_characters)
    
    
    
    longestword = ""
    longest_word_length = 0
    for i in only_characters:
        if len(i) > longest_word_length:
            longest_word_length = len(i)        
    for i in only_characters:
        if len(i) == longest_word_length:
            longestword = i
            return longestword