# -*- coding: utf-8 -*-
"""
@author: Harsh Patel
"""
import time

ti=(time.perf_counter()) #Start timer
class Solution:
    
    def KnightTour(self,N):
    
        def legalmoves(x,y):
            #What positions are considered to be on the board, and also set all the unused postions to equal -1
            if x>=0 and x<N and y>=0 and y<N and bd[x][y]==-1:
                return True
            return False
        
    
        def Backtracking(cur_x,cur_y, stepcount):
            #when you have done all possible moves on the board return True
            if stepcount>=N*N:
                return True
        
            #Consider all possible permutations of moves the knight is able to take
            for i in range(8):
                next_x=cur_x + x_move[i]
                next_y=cur_y + y_move[i]
        
                #check if the next move is a legal one
                if legalmoves(next_x,next_y):
                    #Take this move if it is legal
                    bd[next_x][next_y]=stepcount
            
                    #Does this move lead to a solution...Recursion
                    if Backtracking(next_x,next_y,stepcount+1):
                        return True
                    #If move does not work(meaning does not return True),Bactrack and chose another one from the set of moves that was allowed
                    bd[next_x][next_y]= -1
            #no move worked from the possible 8, meaning have to re-try and backtrack to original position and pick a different move in the for loop
            return False
    
        
        
        #Making the NxN board
        bd= [[-1 for x in range(N)] for y in range(N)]
        #diffrent ways the knight can move, pairing the index of array x and y together
        x_move=[2,1,-1,-2,-2,-1,1,2]
        y_move=[1,2,2,1,-1,-2,-2,-1]

        
    
        #Choose intial position of the knight,(0,0) is the top left corner of the board, the first [ ] goes from the index 0 to N-1 (in a vertical way/row) whilst the second [ ] does the same thing(in a horizontal way/column)
        #So when choosing a position the first int decides how far down the board you will be and the second int picks the horizontal position of the knight in that row (don't change what it equals, since that is what sets up the board)
        bd[0][0]=0
        #put in the postion and then step count of the knight(which is 1 since you are inputting the starting position)
        Backtracking(0,0,1) 
        #if the algorithm determines after a certain point there are no moves that will lead to a path it will stop running and moving the knight
        #this also means that the function will save the moves it made up to that point and place the stepcount on the board, however since the path is not complete there are still some unused spaces
        #the unused spaces are labelled -1 so the following code will look through the board and if it finds a -1 somewhere it will basically tell us that no path was found, thus no solution.
        flat_list= [item for sublist in bd for item in sublist]
        if flat_list.count(-1)>=1:
            print('no solution')
            return False
        return bd


s=Solution()
x=s.KnightTour(8)
print(x) #looking at x in the variable explorer makes the visualization of the board easier
tf=(time.perf_counter()) #Stop timer
print(f'Run time: {tf-ti}') #time to run program


