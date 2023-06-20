import string
from collections import Counter 

# nltk libraries
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer



def analysis(text): 
  lower_case = text.lower()

  # Cleaning text
  # print(string.punctuation) #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

  clean_text = lower_case.translate(str.maketrans('','',string.punctuation))
  # print(clean_text)

  # Tokenization (changing a string into a list)
  tokenized_words = word_tokenize(clean_text, "english")
  # print(tokenized_words)


  # Stop Words (don't add any meaning to the sentence)
  # filtered words
  filtered_words = []
  for word in tokenized_words:
    if word not in stopwords.words('english'):
      filtered_words.append(word)
  # print(filtered_words)

  # creating list of emotions 
  emotions_list = []
  word_list = []
  with open('files/emotions.txt', 'r') as files:

    for line in files:
      clear_line = line.replace('\n', '').replace(',','').replace("'","").strip()
      word, emotion = clear_line.split(':')

      if word in filtered_words:
        emotions_list.append(emotion)
        word_list.append(word)

  # print(emotions_list)

  # count the number of occurrence 
  c = Counter(emotions_list)
  # print(c)
  return c,word_list


# Sentiment Analysis (Positve or Negative)
def sentiment_analyse(text):
  score = SentimentIntensityAnalyzer().polarity_scores(text)
  neg = score['neg']
  pos = score['pos']

  return neg,pos


