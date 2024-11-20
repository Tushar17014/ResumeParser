import pickle
import re

classifier_categorization = pickle.load(open('models/categorization.pkl', 'rb'))
vectorizer_categorization = pickle.load(open('models/vectorizer_categorization.pkl', 'rb'))

def cleanResume(txt):
    cleanText = re.sub('http\S+\s', ' ', txt)
    cleanText = re.sub('RT|cc', ' ', cleanText)
    cleanText = re.sub('#\S+\s', ' ', cleanText)
    cleanText = re.sub('@\S+', '  ', cleanText)
    cleanText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText)
    cleanText = re.sub('\s+', ' ', cleanText)
    return cleanText

def predict_category(resume_text):
    resume_text = cleanResume(resume_text)
    resume_tfidf = vectorizer_categorization.transform([resume_text])
    predicted_category = classifier_categorization.predict(resume_tfidf)[0]
    return predicted_category
