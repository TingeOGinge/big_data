from gensim.models import word2vec
#remember that you always need to refer to texty corpus for building your own space of words
sentences = word2vec.Text8Corpus('text8')
#text8 is a classic and popular text corpus
#there are different text corpus for different languages, please check the one for your second/first language
model = word2vec.Word2Vec(sentences,size=200)
#please do check the similarity between words in the embedded space
vDog = model.wv['dog']
#the vector of word in the embedding space
print(vDog.shape)
print(vDog)
print(model.most_similar('queen',topn=10))
print(model.most_similar('uk',topn=20))
print(model.most_similar(['girl','father'],['boy'],topn=1))
print(model.similarity('woman','man'))
print(model.similarity('dog','chips'))
print(model.most_similar(positive=['woman','king'],negative=['man'],topn=1))
#woman + king - man -> queen in the slides shown today
print(model.most_similar(positive=['shorter','longer'],negative=['short'],topn=3))
#does the result here make any sense to you? If not, think of why.
print(model.doesnt_match('father mother grandfather dog'.split()))
#identify which one is not mathcing the rest
