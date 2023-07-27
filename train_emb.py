import time
import multiprocessing
from datetime import timedelta

from gensim.models import word2vec


if __name__ == '__main__':


    start_time = time.time()
    print('Creating Word2Vec Model...')
    sentences = word2vec.LineSentence('wiki_id.txt')
    id_w2v = word2vec.Word2Vec(sentences, vector_size=300, workers=multiprocessing.cpu_count()-1)
    id_w2v.wv.save_word2vec_format('idwiki_word2vec_300_new.txt', binary=False)
    finish_time = time.time()

    print('Finished. Elapsed time: {}'.format(timedelta(seconds=finish_time-start_time)))