if __name__ == '__main__':

    #Getting the user input as a set, to stop redundancy
    word = set(input())
    #Getting the text word to the Diction
    Dictionary = open("words.txt", 'r').readlines()

    for item in Dictionary:
        wordChars = set(item)
        #Remove '\n' from the set
        wordChars.remove('\n')
        notInChar = 0

        for char in wordChars:
            #If the considered characteres are not in the item, break
            if not char in word:
                notInChar = 1
                break
        if notInChar == 0:
            print(item, end='')