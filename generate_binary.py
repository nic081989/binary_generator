# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: GENERATE BINARY NUMBER STRINGS
#
# NAME:         Nicholas Ngobi
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue

# generate & return a queue of binary number strings from 1 to N 
# front of queue begins @ '1', returns empty Queue otherwise
def generate_binary_numbers(N):
    temp   =  Queue([]) # temporary queue 
    outPut =  Queue([]) ## The real queue to store binary numbers
    if N < 1:
        return Queue([]) #Empty queue
    temp.enq("1") # adding "1" to the output queue
    for i in range(N):
        current = temp.deq() # r
        outPut.enq(current)
        temp.enq(current + "0")
        temp.enq(current  +"1")
    return outPut
        
def main():
    generate_binary_numbers(2).print()
    generate_binary_numbers(3).print()
    generate_binary_numbers(6).print()
    generate_binary_numbers(15).print()

#Don't run main on import
if __name__ == "__main__":
    main()

