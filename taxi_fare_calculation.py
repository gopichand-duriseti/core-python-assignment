def calc_fare(trips):
    base_fare=50
    dist_fare=10
    t=1
    tot=0
    for i in trips:
        print(f'Trip{t}:${base_fare+(dist_fare*i)}')
        tot=tot+(base_fare+(dist_fare*i))
        t+=1
    print(f'Total Fare:${tot}')
calc_fare([5,10,3])
