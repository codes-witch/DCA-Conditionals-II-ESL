def get_children_ud(sent, head_word):
    """
    Get all the words headed by head_word in the dependency graph
    """
    children = []
    
    for w in sent.all_words:
        if w.head == head_word.id:
            children.append(w)
    
            
    return children

