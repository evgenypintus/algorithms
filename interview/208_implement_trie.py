class TrieNode:
    def __init__(self, text = ''):
        self.text = text
        self.children = dict()
        self.is_word = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, current_node=None):
        """
        :param current_node: TrieNode
        :type word: str
        :rtype: None
        """
        if current_node is None:
            current_node = self.root

        if len(word) == 0:
            current_node.is_word = True
            return

        letter = word[0]

        if letter not in current_node.children:
            t = TrieNode(letter)
            current_node.children[letter] = t
            current_node = t
        else:
            current_node = current_node.children[letter]

        self.insert(word[1:], current_node)

    def print_struct(self):

        def print_trie(node: TrieNode, level):
            print('level=', level, '-', node.text)

            for i in node.children.values():
                print_trie(i, level+1)

        print_trie(self.root,0)

    def search(self, word, current_node=None):
        """
        :param current_node: TrieNode
        :type word: str
        :rtype: bool
        """
        if current_node is None:
            current_node = self.root

        if len(word) == 0:
            if current_node.is_word is True:
                return True
            return False

        letter = word[0]

        if letter not in current_node.children:
            return False

        for i in current_node.children.values():
            if self.search(word[1:], i):
                return True

        return False

    def startsWith(self, prefix, current_node=None):
        """
        :type prefix: str
        :rtype: bool
        """

        if current_node is None:
            current_node = self.root

        letter = prefix[0]

        if len(prefix) == 1:
            if letter in current_node.children:
                return True

        if letter not in current_node.children:
            return False

        for i in current_node.children.values():
            if self.startsWith(prefix[1:], i):
                return True

        return False
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':

    trie = Trie()
    trie.insert("apple")
    trie.insert("apples")
    trie.insert("word")

    #trie.print_struct()

    print(trie.search("apple")) # return True
    print(trie.search("app")) # return False
    print(trie.startsWith("app")) # return True
    trie.insert("app")
    print(trie.search("app")) # return True
