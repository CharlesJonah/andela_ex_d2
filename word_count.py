def words(txt):
   burst = txt.split()
   dict_res = {}
   for i in burst:
       if i.isdigit():
           i = int(i)
       if i in dict_res:
           dict_res[i]+=1
       else:
           dict_res[i] = 1
   return dict_res
