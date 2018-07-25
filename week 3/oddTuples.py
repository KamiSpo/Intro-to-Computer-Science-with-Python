def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    index = 0
    newTup = ()
    for element in aTup:
        if index % 2 == 0:
            newTup += tuple(aTup[index:index+1])
            
        index += 1
 
    return newTup
    

oddTuples(('I', 'am', 'a', 'test', 'tuple'))