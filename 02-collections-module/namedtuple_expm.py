from collections import namedtuple

Parts = namedtuple('Parts', 'id_num desc cost amount')
auto_parts = Parts(id_num='1234', desc='Ford Engine', cost=1200.00, amount=10)
print(auto_parts.id_num)


Parts = {'id_num':'1234', 'desc':'Ford Engine', 'cost':1200.00, 'amount':10}
parts = namedtuple('Parts', Parts.keys())(**Parts)
print (parts)
#Parts(amount=10, cost=1200.0, id_num='1234', desc='Ford Engine')