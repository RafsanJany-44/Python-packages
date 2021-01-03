def key_search(dict,value):
  list_of_keys = list(dict.keys())
  list_of_value = list(dict.values())
  position = list_of_value.index(value)
  return list_of_keys[position]



def value_sort(dict,type=False):
  d={}
  values=sorted(dict.values(),reverse=type)
  for i in values:
    d[key_search(dict,i)]=i
  return d


def key_sort(dict,type=False):
  d={}
  keys=sorted(dict.keys(),reverse=type)
  for i in keys:
    d[i]=dict[i]
  return d



def to_json(dict,file_name_or_path):
  import json
  with open(file_name_or_path, 'w') as outfile:
    json.dump(dict, outfile)


def from_json(file_name_or_path):
  import json
  with open(file_name_or_path) as infile:
    return json.load(infile)

