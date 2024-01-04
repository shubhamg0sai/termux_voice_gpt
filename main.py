import datetime
from datetime import datetime
from wish.wish import speak , wish
from voiceinp.voiceinp import voiceinp
from ai.ai import ai

flag = 0
x=datetime.now()
t = x.strftime('%I:%M:%p')
y = x.year
d = x.strftime('%A')
wish()
print (t, y)
print(d)
if flag == 0:
   while True:
      query = voiceinp()
      if  query == '':
         speak('could not understand please say again')

      elif query == 'none':
         speak('could not understand please say again')

      else:
         ans = ai(query)
         print(ans)
         speak(ans)