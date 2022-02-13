class Test(n=2):
    def reduce_(self,n):
        n= n-1
    def print_(self, n):
        while n is not 0:
            print(n,"")
            self.reduce_(n)

            
class App():
      app=Test(30)
      app.run()


            