from Entities.entity import Entity
from patchfinding.BFS import BFS


class Creature(Entity):

    def __init__(self, y, x, speed, health):
        super().__init__(y, x)
        self.speed = speed
        self.health = health
        self.moves = []
        self.hungry = 100
        
    def update(self, pathfinding, map: Map, eat_action, move_counter):
        if move_counter % 2 == 0:
            self.hungry -= 5

        if self.hungry == 0 or self.hungry < 0:
            map.remove_object(self)
    
        elif self.hungry < 100:
            if not self.moves:
                self.moves = pathfinding.get_moves(self.y, self.x, self.target)
           
            if self.moves:
                if self.speed >= len(self.moves):
                    self.moves = [self.moves[0]]
                else:
                    self.moves = self.moves[::self.speed]
                
                ny, nx = self.moves.pop()

                if (map.grid[ny][nx] == None) or (isinstance(map.grid[ny][nx], self.target)):
                    self.y, self.x = ny, nx
                    if isinstance(map.grid[self.y][self.x], self.target):
                        eat_action.run(self, self.target)
                else: 
                    self.moves = []
                    


            
            
            


    

    
        
