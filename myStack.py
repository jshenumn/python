#IMPLEMENT A STACK USE LIST

class myStack:
    __data   = []
    __count  = 0
    __CAPACITY = 10

    def __init__(self):
        self.__data  = []
        self.__count = 0

    def pop(self):
        if self.__count == 0:
           print('Stack underflow!')
        else:
           self.__count -= 1
           return self.__data.pop()

    def push(self, dat):
        if self.__count == 10:
           print('Tring to')
           print('Stack overflow!')
        else:
           self.__data.append(dat)
           self.__count += 1

    def peak(self):
        if self.__count == 0:
           print('Stack is empty!')
        else:
           return self.__data[self.__count-1]





if __name__ == '__main__':
   '''empty pop test'''
   s = myStack()
   assert(s.pop() == None)

   '''push one element'''
   s.push(1)
   assert(s.peak() == 1)
   print('Top of stack is', s.peak())

   '''push one more and pop test'''
   s.push(2)
   assert(s.pop() == 2)
   assert(s.peak() == 1)
   print('Top of stack is', s.peak())

   '''Overflow test'''
   s.pop()
   print(s.peak())
   for i in range(0,11):
       s.push(i)
       print('Top of stack is', s.peak())

