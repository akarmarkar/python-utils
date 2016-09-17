
# A helper function
def lcp_len(seq1, seq2):
    """
    Compute the longest common prefix for 2 sequences.
    When used with strings, it returns the the longest common prefix.
    :param seq1: 1st sequence
    :param seq2: 2nd sequence
    :return: length of the match,
    bool representing if the first sequence matched completely,
    bool representing if the second sequence matched completely
    """
    idx = 0
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)
    while idx < min(len_seq1, len_seq2):
        if seq1[idx] != seq2[idx]:
            break
        idx += 1

    seq1_complete_match = seq2_complete_match = False

    if idx == len_seq1:
        seq1_complete_match = True

    if idx == len_seq2:
        seq2_complete_match = True

    return idx, seq1_complete_match, seq2_complete_match


class STNode(object):
    def __init__(self, parent=None, prefix='', frag='', childnodes=None):
        if parent is None:
            parent = self

        self.parent = parent

        self.prefix = prefix
        self.frag = frag

        if childnodes is None:
            childnodes = []
        self.childnodes = childnodes

    def add_child(self, child):
        self.childnodes.append(child)

    def child_frags(self) -> list:
        return [node.frag for node in self.childnodes]

    def words(self):
        """
        Returns the words under a node
        :return:
        """
        # For all children, make recursive call. In base case,
        # return self.prefix + self.frag
        if self.frag == '' or not self.childnodes:
            return self.prefix + self.frag
        else:
            l = []
            for child in self.childnodes:
                child_words = child.words()
                l.extend(child_words)
            return l

    def __repr__(self):
        return '{0}:({1}){2}'.format(self.prefix, self.frag, self.childnodes)

    def __len__(self):
        return len(self.childnodes)

    def find(self, word_frag:str):
        """
        Return the node having longest match
        :param word_frag: word fragment/complete word
        :return: node and the remaining word_frag that has not matched
        """
        for node in self.childnodes:
            prefix_len, word_full_match, frag_full_match = lcp_len(word_frag,
                                                                   node.frag)
            if prefix_len > 0:
                # return node.find()
                if not word_full_match and not frag_full_match:
                    # Split node. eg:
                    #           "Ca"
                    #     * "re"   "ll"
                    #    "d"
                    #  word = "cart", word_frag ="rt"
                    #
                    #           "Ca"
                    #       "r"     "ll"
                    #    "e" "t"
                    #   "d"
                    pass
                elif word_full_match and not frag_full_match:
                    # ?
                    pass
                elif frag_full_match and not word_full_match:
                    # ?
                    pass
                else:
                    # frag_full_match and word_full_match implies that the
                    # word was already inserted if a '' node is among the
                    # children, if there are any children.
                    child_frags = node.child_frags()
                    if not child_frags or '' in child_frags:
                        print("Word {0} already inserted".format(word_frag))
                    else:
                        node.add_child(STNode(node,))

        return self, word_frag

    def insert(self, word, search=True):
        if search:
            node, word_frag = self.find(word)
            node.insert(word_frag, search=False)
        else:
            self.childnodes.append(STNode(self, self.prefix + self.frag, word))


with open("dict.txt", "r") as f:
    root = STNode()

    for word in f:
        word = word.strip()
        root.insert(word)
    print("root=", root)
