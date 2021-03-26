from translate import Translator

translator = Translator(to_lang="fr")

try: 
    with open('./Translation/test.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print (translation)
    f = open('./Translation/myfile.txt', 'w')
    f.write(translation)
except FileNotFoundError as e:
    print('check your file path silly!')
