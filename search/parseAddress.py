import re

def parse_address(address):
    case_po = re.compile("경상북도 +")
    case0 = re.compile(".+ |[가-힣]+군|구")
    case1 = re.compile(".+ |[가-힣]+시 |[가-힣]+군|구")
    case2 = re.compile(".+ |[가-힣]+시")

    sido = address.split()[0]
    sido = sido[:2]
    gugoon = ''

    if case_po.match(address):
        sido = '경북'
        gugoon = address.split()[1]
    elif case0.match(address):
        gugoon = address.split()[1]
    elif case1.match(address):
        gugoon = address.split()[2]
    elif case2.match(address):
        gugoon = address.split()[1]

    return sido, gugoon
