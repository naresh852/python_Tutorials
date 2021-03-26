# prirotyy queue code
class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

        # for checking if the queue is empty

    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

        # for popping an element based on Priority

    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()
        # from heapq import heapify,heappop,heappush
# def cookies(A,k):
#     heapify(A)
#     c=0
#     try:
#         while A[0]<k:
#             c1=heappop(A)
#             c2=heappop(A)
#             f=int(c1+2*c2)
#             heappush(A,f)
#             c+=1
#         return c
#     except:
#         return "-1"
# nn,kk=input().split()
# n=int(nn)
# k=int(kk)
# A=[map(int,input().split())]
# print(cookies(A,k))

print(dir(PriorityQueue()))

