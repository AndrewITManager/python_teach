#задача if..elif

def route_info(info):
  if info.get('distance'):
    return f"Distance to your destination is {info.get('distance')}"
  elif info.get('speed') and info.get('time'):
    return f"Distance to your destination is {(info.get('speed') * info.get('time'))}"
  return f"No distance info is available"
  

info_dict = {
  #'distance': 45,
  #'speed': 5,
  'time': 4,
}

print(route_info(info_dict))