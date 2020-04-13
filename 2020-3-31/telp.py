cl1 = input()
list = cl1.split()
shop_number = int(list[0])
telp_number = int(list[1])
school_place= int(list[2])
limit_time = int(list[3])
#print(list)
shop_place = input().split()
telp_place = input().split()
count_shop_place = shop_place
result_point = [0]
result_time = [10000000]


def all(now_place,now_time,now_point,count_shop_place):
#  print(now_place)
  if(now_time > limit_time):
    return 0
  elif(now_place == school_place):
#    print(now_point)
    if(result_point[0] < now_point):
        if(result_time[0] > now_time):
            result_point[0] = now_point
            result_time[0] = now_time
    return 0
#普通の移動  
  all(now_place+1,now_time+1,now_point,count_shop_place)
  all(now_place-1,now_time+1,now_point,count_shop_place)
# ワープ
  if(str(now_place) in telp_place):
    for ite in range(shop_number):
      all(int(shop_place[ite]),now_time+1,now_point,count_shop_place)
# 店に寄り道
  if(str(now_place) in shop_place):
   # count_shop_place.remove(str(now_place))
    all(now_place,now_time+1,now_point+1,count_shop_place)

result = all(0,0,0,count_shop_place)
print(result_point[0],result_time[0])