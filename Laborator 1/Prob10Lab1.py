def count_words(text):
    words_list = text.split()
    print("Sunt "+str(len(words_list))+" cuvinte in textul dat.")


if __name__ == '__main__':
    count_words("I have Python exam")
