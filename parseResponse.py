import ast
import pprint

from search.getLocation import get_location

response_data = get_location("아무거나")

data = ast.literal_eval(response_data)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)

print("length of data is %d" %data['display'])
