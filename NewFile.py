
sentence = input("Enter a sentence with some string :")
def calculate_count(sentence):

    sentence_length = len(sentence)
    word_count = 1
    space_count = 0
    char_count = 0
    vowel_count = 0
    vowel_list = ['a','A','e','E','i','I','o','O','u','U']
    for index in range(0,sentence_length):
        index_char = sentence[index]
        if index_char != ' ':
            char_count += 1
            if index_char in vowel_list:
                vowel_count += 1
            else:
                space_count += 1
                if index < sentence_length:
                    word_count += 1

        return (word_count,space_count,char_count,vowel_count)

    word_count,space_count,char_count,vowel_count = calculate_count(sentence)

    print("\nOutput:-\n",sentence)
    print("word count :",word_count,"\nspace count :",space_count,"\ncharacter count :",char_count,"\nvowel count :",vowel_count)
