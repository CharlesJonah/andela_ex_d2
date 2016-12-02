def find_max_min(li):
	res=[]
	mn=min(li)
	mx=max(li)
	if max(li)== min(li):
	    res.append(len(li))
	else:
	    res.append(mn)
	    res.append(mx)
	return res