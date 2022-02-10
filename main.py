from pyverse import Pyverse
from gensim.models.keyedvectors import KeyedVectors

# Cargamos el word embedding.
wordvectors_file_vec = 'D:\DESCARGAS\embeddings-l-model.vec'
cantidad = 1313423
wordvectors = KeyedVectors.load_word2vec_format(wordvectors_file_vec, limit=cantidad)
print("WORD EMBEDDING CARGADO")

# Función auxiliar que te devuelve una lista de palabras relacionadas con una serie de temas
# y que rimen en consonante y asonante con una palabra dada.
def busca_rima_y_tema(palabra, temas):
    rimas = wordvectors.most_similar_cosmul(positive=temas,negative=[])
    if(len(rimas) == 0):
        print("No se han encontrado resultados")
    else:
        print(rimas)
        verse = Pyverse(palabra)
        res_consonante = []
        res_asonante = []
        for p in rimas:
            if(len(p[0])>1):
                cmp = Pyverse(p[0])
                if(cmp.consonant_rhyme == verse.consonant_rhyme and p[0] != palabra):
                    res_consonante.append(p[0])
                if(cmp.assonant_rhyme == verse.assonant_rhyme and p[0] != palabra):
                    res_asonante.append(p[0])
        print("Consonante: ", res_consonante)
        print("Asonante: ", res_asonante)

#PRUEBAS
busca_rima_y_tema("cuadro", ["lava"])