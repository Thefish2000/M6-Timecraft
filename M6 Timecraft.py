import datetime

schema = []
meny_user_action= {"c":"Create activity", "v":"View activitys", "d":"Delete activity", "e": "Edit activity"}


def create(schema):
  user_input_namn = input("Skriva in aktivitets namn: ")
  user_input_time_start= input("När ska aktivitet börjar i format (xx,xx): ")
  user_input_time_end = input("När ska aktivitet slutar(xx,xx): ")
  starttime= user_input_time_start.split(",")
  endtime= user_input_time_end.split(",")
  schema.append({
     "starttime": datetime.time(int(starttime[0]),int(starttime[1])),
     "endtime": datetime.time(int(endtime[0]),int(endtime[1])),
     "name": user_input_namn,
})
  #man behöver vara säkert på att det inte finns en aktivitet med samma name eller samma tid som redan finns i lista
  #fixa problem med input


def view(schema):
  today = datetime.date.today()
  print(today)
  for item in schema:
     starttime = item["starttime"].strftime("%H:%M")
     endtime = item["endtime"].strftime("%H:%M")
     print(f"{starttime}-{endtime}: {item['name']}")


def delete(schema):
    user_input= input("Skriva in namn på aktivitet som du vill tar bort: ")
    for item in schema: 
       if item['name'] == user_input:
          schema.remove(item)
          print(f"{user_input} raderades")
          return None
    print("Kan inte hitta aktivitet")

def edit():
    print("edit")


def meny(options): 
 for key,value in options.items(): 
     print(f"{key}) {value}")
 while True:
  user_input = input("What do you want to do")
  if user_input in options:  
   print(f"You selected {user_input})"+ str(options.get(user_input)))
   return user_input  
  


def main():
    print("main")

create(schema)
view(schema)
delete(schema)
view(schema)