'''Implement Queue using list'''

class myQueue:
      __data     = []
      __count    = 0
      __capacity = 10

      def __init__(self):
          self.__data  = []
          self.__count = 0

      def enqueue(self, dat):
          if self.__count == self.__capacity:
             print('Queue overflow!', 'Was trying to enqueue', dat)
          else:
             self.__data.append(dat)
             self.__count += 1

      def dequeue(self):
          if self.__count == 0:
             print('Empty queue')
          else:
             self.__count -= 1
             dat = self.__data[0]
             self.__data.remove(dat)
             return dat

      def peak(self):
          if self.__count == 0:
              print('Queue is empty!')
          else:
              return self.__data[0]


if __name__ == '__main__':
   '''empty pop test'''
   q = myQueue()
   assert(q.dequeue() == None)

   '''push one element'''
   q.enqueue(1)
   assert(q.peak() == 1)
   print('Top of queue is', q.peak())

   '''push one more and pop test'''
   q.enqueue(2)
   assert(q.dequeue() == 1)
   assert(q.peak() == 2)
   print('Top of queue is', q.peak())

   '''Overflow test'''
   q.dequeue()
   print(q.peak())
   for i in range(0,11):
       q.enqueue(i)
       print('Top of stack is', q.peak())