shift = int(input('What is your cipher number? ')) % 26
text = input('What is your message? ')
output = ''
punctuation = ["?", "!", ".", ",", ";"]
for items in text:
  if ('A' <= items <= 'Z'):
    overrun = ord(items) + shift
    if (overrun > 90):
      overrun = overrun - 26
    output += chr(overrun)
  elif ('a' <= items <= 'z'):
      overrun = ord(items) + shift
      if (overrun > 122):
        overrun = overrun - 26
      output += chr(overrun)
  elif (items in punctuation or items == " "):
    pass
  else:
      output += chr(ord(items))
form_output = ''
columns = 0
rows = 0
for char in output:
  if columns == 5:
    form_output += ' '
    columns = 0
    rows += 1
   if rows == 10:
    form_output += "\n"
    rows = 0
  form_output += char
  columns += 1
print(form_output.upper())
