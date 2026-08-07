class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        a=[]
        for i in  range (len(asteroids)):
            alive=True
            
            while a and a[-1]>0 and asteroids[i]<0:
                top=a[-1]
                current=asteroids[i]
                if abs(current)>abs(top):
                    a.pop()
                elif abs(current)==abs(top):
                    a.pop()
                    alive=False
                    break
                else:
                    alive=False
                    break

            if alive:
                a.append(asteroids[i])
        return a





        