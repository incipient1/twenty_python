import uuid

id = 'id'
coupon_num = 'coupon_num'
file_coupon = open('file_coupon_u.csv','w')
file_coupon.write('{},{}\n'.format(id,coupon_num))

for id in range(10):
    coupon_num = str(uuid.uuid4()).upper()
    coupon_num = coupon_num[0:4]+'-'+coupon_num[4:28
    ]+'-'+coupon_num[28:32]+'-'+coupon_num[32:]
    file_coupon.write('{},{}\n'.format(id,coupon_num))

file_coupon.close()
