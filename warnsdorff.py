'Author: Harsh Patel'
import time
ti=(time.perf_counter())
class Solution:
    
    def KnightTour(self,N):
    
        def legalmoves(x,y):
            #What positions are considered to be on the board, and also set all the unused postions to equal -1
            if x>=0 and x<N and y>=0 and y<N and bd[x][y]==-1:
                return True
            return False
        #Adding a count to every position accesible from the current position
        def countlegal(x,y):
            count = 0
            for i in range(8):
                new_x = x + x_move[i]
                new_y = y + y_move[i]
                if legalmoves(new_x,new_y):
                    count += 1
            return count
        
 
        def Backtracking(cur_x,cur_y, stepcount):
            #when you have done all possible moves on the board return True
            if stepcount>=N*N:
                return True
            
            #List for number of moves a position can make
            nb_moves_list = []
 
            #Consider all possible permutations of moves the knight is able to take
            for i in range(8):
                next_x=cur_x + x_move[i]
                next_y=cur_y + y_move[i]
 
                if legalmoves(next_x,next_y):
                    if countlegal(next_x,next_y) > 0:
                        # creating a tupple storing both i and move count
                        count_index = (countlegal(next_x,next_y),i);
                        # add tupple to list
                        nb_moves_list.append(count_index)
                        # delete the tuple because it can't be overwritten
                        del count_index
            # sort the list by the smallest number of legal moves
            priority_list = sorted(nb_moves_list, key=lambda tup: tup[0])
            priority_moves = [index[1] for index in priority_list]
            
            #advance to the priority move
            for j in range(0,len(priority_moves)):
                advance_x = cur_x + x_move[priority_moves[j]]
                advance_y = cur_y + y_move[priority_moves[j]]
 
                # if leads to another legal move and solution add a step to it or else return false
                bd[advance_x][advance_y] = stepcount
                if Backtracking(advance_x,advance_y,stepcount+1):
                   
                           
                    
                    return True
                
                return False
        
        #Making the NxN board
        bd= [[-1 for x in range(N)] for y in range(N)]
        #diffrent ways the knight can move, pairing the index of array x and y together
        x_move=[2,1,-1,-2,-2,-1,1,2]
        y_move=[1,2,2,1,-1,-2,-2,-1]
 
        
    
        #Choose intial position of the knight,(0,0) is the top left corner of the board, the first [ ] goes from the index 0 to N-1 (in a vertical way/row) whilst the second [ ] does the same thing(in a horizontal way/column)
        #So when choosing a position the first int decides how far down the board you will be and the second int picks the horizontal position of the knight in that row
        bd[0][0]=0
        
        #put in the postion and then step count of the knight
        Backtracking(0,0,1) 
          #Because of the range I coded in the lines above my last stepcount is -1, 
          #whilst still taking into account that if there is more than 1 unused space (-1) it means that there was no path found and the bactracking stopped at a certain path, meaning no solution
        flat_list= [item for sublist in bd for item in sublist]
        if flat_list.count(-1)>1:
            print('no solution')
            return False
        #the following lines will go through every row and find the last stepcount and then replace the value with the one it is supposed to have
        
        for row in bd:
            for step in row:
                if step==-1:
                    bd[bd.index(row)][row.index(step)]=(N*N)-1
            print(row)#this will print the board in the console, but you could also take this line out and use line 93 instead if you want to view the board in the variable explorer(in my opinion it looks nicer in the variable explorer)
        return bd
s=Solution() #initialize class
x=s.KnightTour(8)#Choose what N x N chessboard you want
#print(x) #looking at x in the variable explorer makes the visualization of the board easier
tf=(time.perf_counter())
print(f'Run time: {tf-ti}')
