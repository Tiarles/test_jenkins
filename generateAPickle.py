import pickle

lista = [1,2,3,4,5,'feijao']

with open("tmp_pickle.pkl", "wb") as fpkl:
    pickle.dump(lista, fpkl)
