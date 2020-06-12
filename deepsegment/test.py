# print('Loading word2vec model ...')
# from gensim.models import Word2Vec
# from gensim.models import KeyedVectors
# from gensim.test.utils import datapath
#
# # word2vec_model = Word2Vec.load_word2vec_format("/Users/trinhgiang/Downloads/wiki.vi.model.bin", binary=True)
# wv_from_bin = KeyedVectors.load_word2vec_format(datapath("/Users/trinhgiang/Downloads/wiki.vi.model.bin"), binary=True)
# key_list = list(wv_from_bin.vocab.keys())
# with open("/Users/trinhgiang/Downloads/wiki.txt", "w+", encoding="utf-8", errors='ignore') as f:
#     for i in range(231486):
#         f.write(key_list[i])
#         for j in range(400):
#             f.write(' ')
#             f.write(str(wv_from_bin.vectors[i][j]))
#         f.write("\n")
# # print(wv_from_bin.vectors[0][1])
# # key_list = list(wv_from_bin.vocab.keys())
# # print(key_list[0])
#

with open("/Users/trinhgiang/Downloads/sent3.txt", "w+", encoding="utf-8", errors='ignore') as save_file:
    lines1=[]
    lines2=[]
    with open("/Users/trinhgiang/Downloads/sent2.txt","r",encoding="utf-8", errors='ignore') as f1:
        lines1 = f1.readlines()
    with open("/Users/trinhgiang/Downloads/sentence_true_check_acc_2.txt", "r", encoding="utf-8",errors='ignore') as f2:
        lines2=f2.readlines()
    j=0
    for i in range(len(lines1)):
        save_file.write(lines1[i])
        # save_file.write("\n")
        if (i >10000 and j<len(lines2)):
            save_file.write(lines2[j])
            j+=1
            # save_file.write("\n")

