for _ in range(int(input())):
    flag = True
    uid = input()
    
    count = {}
    for s in uid:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1

    for key in count:
        if count[key] > 1:
            flag = False
    
    if flag:
        if len(uid) == 10:
            if len([x for x in uid if x.isdigit()]) >= 3:
                if len([char for char in uid if char.isupper()])>=2:
                    print('Valid')
                else:
                    print('Invalid')
            else:
                print('Invalid')
        else:
            print('Invalid')
    else:
        print('Invalid')
