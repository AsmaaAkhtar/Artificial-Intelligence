class Trie:
    def __init__(self):
        self.character = {}
        self.isLeaf = False  # true when the node is a leaf node
 
 
# Iterative function to insert a string into a Trie
def insert(root, s):
    # start from the root node
    curr = root
 
    for ch in s:
        curr = curr.character.setdefault(ch, Trie())
 
    curr.isLeaf = True
 
 
# (top, right, bottom, left, and four diagonal moves)
row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]
 
def isSafe(x, y, processed, board, ch):
    return (0 <= x < len(processed)) and (0 <= y < len(processed[0])) and \
           not processed[x][y] and (board[x][y] == ch)
 

def searchBoggle(root, board, i, j, processed, path, result):
    if root.isLeaf:
        result.add(path)
 
    processed[i][j] = True
 
    for key, value in root.character.items():
 
        for k in range(len(row)):
 
            if isSafe(i + row[k], j + col[k], processed, board, key):
                searchBoggle(value, board, i + row[k], j + col[k],
                             processed, path + key, result)
                processed[i][j] = False
 
 
def searchInBoggle(board, words):
    
    result = set()
     # base case
    if not board or not len(board):
        return
 
    
    root = Trie()
    for word in words:
        insert(root, word)
 
    # `M × N` board
    (M, N) = (len(board), len(board[0]))
 
    processed = [[False for x in range(N)] for y in range(M)]
 
    # consider each character in the matrix
    for i in range(M):
        for j in range(N):
            ch = board[i][j]  
 
            if ch in root.character:
                searchBoggle(root.character[ch], board, i, j, processed, ch, result)
 
    return result

board = [
    ['M', 'S', 'E', 'F'],
    ['R', 'A', 'T', 'D'],
    ['L', 'O', 'N', 'E'],
    ['K', 'A', 'F', 'B']
  ]

words = ['START', 'NOTE', 'SAND', 'STONED']
searchInBoggle(board, words)
validWords = searchInBoggle(board, words)
print(validWords)

\\note stoned(ans)
     
