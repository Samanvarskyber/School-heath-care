class Tool:
    dict_ave={
'aveheight' : 0 ,
'aveweight' : 1 , 
'aveage' : 2
}
#-----------<<AVG HEIGHT>>-------------
    @staticmethod
    def Ave_height(arr):
      n = len(arr)
      sum = 0 
      for i in range(n):
        sum= sum+arr[i].height
      Tool.dict_ave['aveheight']=sum/n
 
 
#-----------<<AVG Weight>>-------------

    @staticmethod
    def Ave_weight(arr):
      n = len(arr)
      sum = 0 
      for i in range(n):
        sum= sum+arr[i].weight
      Tool.dict_ave['aveweight']=sum/n
 
 #-----------<<AVG Age>>-------------

    @staticmethod
    def Ave_age(arr):
      n = len(arr)
      sum = 0 
      for i in range(n):
        sum= sum+arr[i].calculate_age()
      Tool.dict_ave['aveage']=sum/n
 