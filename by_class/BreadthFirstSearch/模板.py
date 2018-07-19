    def serialize(self, root):
        # write your code here
        result = []
        q = deque()
        q.append(root)
        while q:
            n = q.popleft()
            if n:
                result.append(str(n.val))
                q.append(n.left)
                q.append(n.right)
            else:
                result.append('#')
        end = len(result) - 1
        while result[end] == '#' and end >= 0:
            end -= 1
        return '{' + ','.join(result[:end+1]) + '}'
        
        
    '''
    def deserialize(self, data):
        # write your code here
        nodes = data[1:-1].split(',')
        if not nodes:
            return None
        root = TreeNode(nodes[0])
        q = deque()
        q.append(root)
        i = 1
        while i < len(nodes):
            n = q.popleft()
            if nodes[i] != '#':
                left_node = TreeNode(int(nodes[i]))
                n.left = left_node
                q.append(left_node)
            i += 1
            if i >= len(nodes):
                break
            if nodes[i] != '#':
                right_node = TreeNode(int(nodes[i]))
                n.right = right_node
                q.append(right_node)
            i += 1
        return root
