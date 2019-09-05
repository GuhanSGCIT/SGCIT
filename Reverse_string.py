def reverse(r):
  input_string = r.split(" ")
  input_string = input_string[-1::-1]
  output = ' '.join(input_string)
  return output
if __name__ =='__main__':
  r=input()
  print (reverse(r))
