def fu(st):
    if len(st) < 4:
        return "No"
    
    sze = len(st)

    for i in range(sze):
        st[i] = st[i].lower()

    i = 0
    j = 1 

    while True:
        if st[i] == st[j]:
            st.remove(st[j])
            sze = len(st)
        else:
            i += 1
            j += 1
        if i == sze or j == sze:
            break
    
    if ("".join(st) == "meow"):
        return "Yes"
    else:
        return "No"
        
t = int(input())

for i in range(t):
    size = int(input())
    st = list(input())
    print(fu(st))