def top_words(text):
    word_freq={}
    with open(text, 'r') as file:
        content=file.read()
        for word in content:
            word=word.lower().strip('.,!?";()')
            if word in word_freq:
                word_freq[word]+=1
            else:
                word_freq[word]=1
        sorted_freq=sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        print("Top 10 most frequent words: ")
        for word, freq in sorted_freq[:10]:
            print(word, ":", freq)
text_file=input("Enter the path of the text file: ")
top_words(text_file)