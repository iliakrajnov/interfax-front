import gensim
import json
from utils import preprocess
from simpletransformers.seq2seq import Seq2SeqModel, Seq2SeqArgs
import pickle



def get_tags(path):
  article = json.load(open(path))
  docs = [preprocess(doc) for doc in article['news']]
  #построение LDA
  dictionary = gensim.corpora.Dictionary(docs)
  bow_corpus = [dictionary.doc2bow(doc) for doc in docs]
  lda_model = gensim.models.ldamodel.LdaModel(bow_corpus, 
                                    num_topics = 1, 
                                    id2word = dictionary,                                    
                                    passes = 10,
                                    )
  return ' '.join(lda_model.print_topics(-1)[0][1].split('"')[1::2])

def get_title(line):
  #инициализация модели
  model = Seq2SeqModel(
      encoder_decoder_type="mbart",
      encoder_decoder_name="IlyaGusev/mbart_ru_sum_gazeta",
      use_cuda=False
  )
  model = pickle.load(open('article_model.pkl', 'rb'))
  pred = model.predict([line])
  return pred[0][0]


tags = get_tags('test_article.json')
print(tags)
print(get_title(tags))
