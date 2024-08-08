def simplifyPath(path):
        path = path.split('/')
        print("Before stacking up",path)
        stack = []
        for i in len(path):
                if path[i] != "..":
                        stack.append(path[i])
                
        print("After stacking up",'/'.join(stack))

# path ="/home/"
# simplifyPath(path)

path = "/home//foo/"
simplifyPath(path)
# path = '/home/user/Documents/../Pictures'
# simplifyPath(path)

