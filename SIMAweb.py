#change the keys and values in this section to whatever you are searching for, you can add more as needed
a_dict = {
    'Key1': ('value1','value2'),
    'Key2': ('value3','value4'),
    'Key3': ('value5','value6'),
}
def percentage(part, whole):
  return 100 * float(part)/float(whole)

#list all the tuples into a list for key:value iteration
one_big_list = list(item for items in a_dict.values() for item in items)

#scrape website and create passable output of text
import nltk 
from nltk import word_tokenize
import requests
url = 'https://theUrlGoesHere'
r = requests.get(url)
type(r)
html = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(html)
type(soup)
text = soup.get_text()
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer('\w+')
tokens = tokenizer.tokenize(text)
tokens[:8]
tokens = nltk.wordpunct_tokenize(text)
import string
table = str.maketrans ('', '', string.punctuation)
words = [w.translate(table) for w in tokens]
words = [word for word in tokens if word.isalpha()]

#dictionary iteration party
word_count_dict = {}
for line in words:
        for item in one_big_list:
            line_split = list(line.strip('\n').split(' ')) 
            if item in line_split:
                #print(f"found {item} in {line}")  #uncomment to see line context
                if item not in word_count_dict.keys():
                    word_count_dict[item] = line_split.count(item) 
                else:
                    word_count_dict[item] = word_count_dict[item] + line_split.count(item) 
#print(word_count_dict) #uncomment to see all tagged words and their counts
ideal_output = {}
for count in word_count_dict:
    for key, value in a_dict.items():
        if count in value:
            if key not in ideal_output:
                ideal_output[key] = word_count_dict.get(count) 
            else:
                ideal_output[key] = ideal_output[key] + word_count_dict.get(count)             
for item in ideal_output:
   string_list = [] 
   tuple_of_words = a_dict[item]
   for entry in tuple_of_words:
       get_times_said = word_count_dict.get(entry)
       if get_times_said:
           string_list.append(f"'{entry}': {get_times_said}")
   print(f"{item}: {ideal_output.get(item)} found, {round(percentage(ideal_output.get(item), len(words)), 2)}% of total words in document: {', '.join(string_list)}.")
