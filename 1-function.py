def co_occurrence(corpus,word1,word2,contextwindow,returncombinations='True'):
    '''
    this function has been created to help calculate a co-occurrence matrix.
    it takes 5 parameters as input:
    corpus - this is the document string
    word1 - this is the first word in the co-occurrence matrix
    word2 - this is the word being compaired to word1 of the co-occurrence matrix
    contextwindow - this is within what range you looking for the two words
    returncombinations - will return all the positions/ combinations
    '''
    # take the input document and tokenize it into a list of words
    samples = tokenize.word_tokenize(text=corpus,language='english')
    
    # set some initial variables:
    last_index = len(samples) - 1
    tokens = list(enumerate(samples))
    context_windows = list()
    final = list()
    data = list()
    counter = 0

    # for each word in the document:
    for word in tokens:
        start_bound = np.max([0,word[0] - contextwindow]) #get the start index of the context window
        end_bound = np.min([last_index,word[0] + contextwindow]) #get the end index of the context window
        context_windows.append(tokens[start_bound:word[0] + 1]) # this returns the first part of the context window (words before the word of interest)
        context_windows.append(tokens[word[0]:end_bound + 1]) # this return the second part of the context window (words after the word of interest)

    #  remove any duplicate context windows, since we do not want to count double (obvious ones)
    context_windows = np.unique(context_windows)
    # [list([(0, 'he')]) list([(0, 'he'), (1, 'is')])] -list of list of tuples
    # for each remaining context window
    for context_window in context_windows:
        # [(0, 'he')],[(0, 'he'), (1, 'is')] -for every list take it's tuples and join them
        tuple_combined = tuple()
        for tup in context_window:
            # (0, 'he'), (0, 'he', 1, 'is')
            tuple_combined = tuple_combined + tup
        if word1 in tuple_combined and word2 in tuple_combined and word1 != word2:
            data =  list(tuple_combined) 
            # [0, 'he'], [0, 'he', 1, 'is'] 
            for i in data:
                try:
                    # if (i) is a string and it is not one of the two words being compared as part of the co-occurrences matrix
                    if i.isalpha()==True and i not in [word1,word2]:
                        # remove the index position first and then the string
                        data.remove(data[data.index(i)-1])
                        data.remove(i)
                except(AttributeError):
                    # for every index position (int) continue (these int values is to keep track of the position in the document)
                    continue    
            final.append(data)
    # [[0, 'he', 1, 'is'], [0, 'he', 1, 'is'], [4, 'he', 5, 'is'], [4, 'he', 5, 'is'], [5, 'is', 7, 'he'], [7, 'he', 8, 'is'], [7, 'he', 8, 'is']]
    # clean memory
    del data
    del tokens
    del context_windows
    del tuple_combined
    for i,j in enumerate(Counter(str(e) for e in final)):
        # this enumerate object will return the unique combinations to ensure we do not count double
        # [(0, "[0, 'he', 1, 'is']"), (1, "[4, 'he', 5, 'is']"), (2, "[5, 'is', 7, 'he']"), (3, "[7, 'he', 8, 'is']")]
        if returncombinations == 'True':
            print(i,j) # only if one wants to see the actual combinations
        counter += 1
    return(counter)