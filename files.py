with open('referat.txt', 'r', encoding='utf-8') as referat_read:
    content = referat_read.read()
    string_length = len(content)
    words_content = content.split(' ')
    words_count = len(words_content)
    content_replace = content.replace('.', '!')
    print ('Длина строки в файле: {}'.format(string_length))
    print ('Количество слов в тексте: {}'.format(words_count))
    with open ('referat2.txt', 'w', encoding='utf-8') as referat_write:
        referat_write.write(content_replace)
