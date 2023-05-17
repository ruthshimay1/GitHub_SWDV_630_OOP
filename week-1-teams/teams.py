class Teams:
  def __init__(self, members):
    self.__myTeam = members

  def __len__(self):
    return len(self.__myTeam)

  def __contains__(self, member):
    #Will return a boolean value True or False
    return member in self.__myTeam

  def __iter__(self):
    #Will go through the list of values
    return iter(self.__myTeam)
  
 
def main():
    classmates=Teams(['John','Steve','Tim'])   
    print ('\n', len(classmates))
    print('Tim' in classmates)
    print('Sam' in classmates)
    
    iterator = iter(classmates)   #we get iterable object reference
    # for member in classmates:
    for member in iterator:          
        print(member,end="  ")  #print each member of the classmates object
    print('\nclassmates object has len method available? : ', "__len__" in dir(classmates),'\n')  #Question #3    

 # calling the function 
main()
    
    


 