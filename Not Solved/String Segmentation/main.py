count = 0 
def can_segment_string(s, dictionary):
  global count 
  print(f"count : {count}")
  count += 1
  for i in range(1, len(s) + 1):
    
    first = s[0:i]
    print(f"first : {first}")
    if first in dictionary:
      second = s[i:]
      print(f"second : {second}")
      if not second or second in dictionary or can_segment_string(second, dictionary):
        return True
  return False
  
s = "hellonow"
dictionary= set(["hello","hell","on","now"])
if can_segment_string(s, dictionary):
  print("String Can be Segmented")
else:
  print("String Can NOT be Segmented")