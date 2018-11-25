#Уважаемый преподаватель!
#Прощу не обращать внимание на комменты, они мне помогут в будущем,
#когда, я все забуду, а мне нужно будет решать задачу с xml файлом.

import xml.etree.ElementTree as ET

def find__top_word():
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse("files/newsafr.xml", parser=parser)

    # titles = []
    # что такое корневой элемент xml

    root = tree.getroot()

    # теги и атрибуты
    # поиск в XML
    # xml_title = root.find("channel/title")
    # print(type(xml_title))
    # print(xml_title.text)
    
    words_dict = {}
    xml_items = root.findall("channel/item")
    for xmli in xml_items:
      # print(xmli.attrib["id"])
      # print(xmli.find("description").text)
      news_word = xmli.find("description").text.split()
      for word in news_word:
          if len(word) > 6:
              if word in words_dict.keys():
                  words_dict[word] += 1
              else:
                  words_dict[word] = 1
    words_len_list = []
    for key, value in words_dict.items():
        word_tuple = (value, key)
        words_len_list.append(word_tuple)

    words_len_list_sorted = sorted(words_len_list)

    print('Топ 10 встречаюшихся слов: ')
    n = 10
    for key, value in words_len_list_sorted[-10:]:
        print('{} место. Слово "{}" встречается {} раз'.format(n, value, key))
        n -= 1

find__top_word()

