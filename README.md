# ML_track

# datacamp
1.python list-list manipulation
 x = [1,2,3]. copy list的記憶體位址(reference)
 y = x        一樣也是copy list的記憶體位址(reference)
 y[1] = "z"
 print(x)=[1,"z",2] x也會跟著改,因為是指導相同的list記憶體位址(reference)

若要copy list的value
x = y[1]
y = list(x) new list reference
這樣改變y[1], 就不會改變x的值

