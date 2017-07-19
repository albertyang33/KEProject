import math
import sys
import numpy as np
reload(sys)
sys.setdefaultencoding('utf-8')

entity_vec = np.loadtxt('entity2vec.vec',dtype='float32')
relation_vec = np.loadtxt('relation2vec.vec',dtype='float32')
top_entity=np.argsort(np.sum(np.square(np.tile(entity_vec[118,:]+relation_vec[63,:],(entity_vec.shape[0],1))-entity_vec),axis=1))
print(top_entity[0])


