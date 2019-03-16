# using context window of size 5:
if os.path.exists('co_occurrence_matrix.csv') == False:
    doc_counter = 1
    for doc in combined:
        co_occurrence_matrix_doc = np.zeros(shape=(len(vocab),len(vocab)))
# ==========================================================================================
        i = 0
        while i < len(list(pairs.values())) - 1:
            return_vals = list(map(process_word_pairs,list(pairs.values())[i:i+10001]))
            for tup in return_vals: #fill all the values in the upper triangular matrix
                co_occurrence_matrix_doc[tup[0][0],tup[0][1]] = tup[1]            
            i += 10000
# ==========================================================================================
        co_occurrence_matrix_doc = co_occurrence_matrix_doc + np.transpose(co_occurrence_matrix_doc) #symmetric property
        co_occurrence_matrix_corpus = co_occurrence_matrix_corpus + co_occurrence_matrix_doc
        if doc_counter%20 == 0:
            print('doc: ',doc_counter,' complete')
        elif doc_counter == len(combined):#tfidf_dataframe.shape[0]:
            print('doc: ',doc_counter,' complete')
            print('***DONE***')
        doc_counter += 1                
##     co_occurrence_matrix_corpus = co_occurrence_matrix_corpus + co_occurrence_matrix(doc.split(),vocab)
    co_occurrence_matrix_df = pd.DataFrame(data=co_occurrence_matrix_corpus,index=vocab,columns=vocab)
    co_occurrence_matrix_df.to_csv('co_occurrence_matrix.csv',columns=vocab, header=True)
    co_occurrence_matrix_df = pd.read_csv('co_occurrence_matrix.csv')
else:
    co_occurrence_matrix_df = pd.read_csv('co_occurrence_matrix.csv') 