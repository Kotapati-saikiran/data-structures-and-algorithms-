price = [100,80,60,70,60,75,85]
stack = []
ans=[]
for num in price:
    span = 1
    while stack and stack[-1][1] <= num:
        popped_span,popped_element = stack.pop()
        span+=popped_span
    stack.append((span,num))
    ans.append(span)
print(ans)

#--------------------------------------------------
""" def __init__(self):
       self. stack =[]
        
    def next(self, price):
        span=1
        while self.stack and self.stack[-1][0]<=price:
            span+=self.stack.pop()[1]
        self.stack.append((price,span))
        return span"""