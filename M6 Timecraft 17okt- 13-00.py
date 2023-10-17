import datetime

schema = []
meny_user_action= {"c":"Create activity", "v":"View activitys", "d":"Delete activity", "e": "Edit activity"}


def create():
  user_input_namn = input("Skriva in aktivitets namn: ")
  user_input_time_start= input("När ska aktivitet börjar i format (xx,xx): ")
  user_input_time_end = input("När ska aktivitet slutar(xx,xx): ")
  starttime= user_input_time_start.split(",")
  endtime= user_input_time_end.split(",")
  return starttime, endtime, user_input_namn

def available(schema, starttime, endtime):
  for item in schema:
    if item["starttime"] > float(starttime) and item["starttime"]  > float(endtime) or item["endtime"] < float(starttime):
       #start time och endtime är listor just nu och kan inte convert till float !!!
       return not True
    else: return True
  
def create_in_schema(schema,starttime,endtime,name):
  schema.append({
     "starttime": datetime.time(int(starttime[0]),int(starttime[1])),
     "endtime": datetime.time(int(endtime[0]),int(endtime[1])),
     "name": name,})


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
          return 
    print("Kan inte hitta aktivitet")



            
        
#innan edit behöver man kolla upp om aktivitetet finns, denna görs i en annan funktion
def edit(): #man ändrar en aktivitet
    activity=input('Vilken aktivitet vill du ändra?')
    for item in schema: #kollar genom alla element i listan
        if item['name']==activity: #jämför med alla element
            print('Aktiviteten finns')
            schema.remove(item)
            start=input('Vilken tid ska aktiviteten börja istället? (skriv i format xx,xx) ')
            end=input('Vilken tid ska aktiviteten slutas istället? (skriv i format xx,xx) ')
            new_start=start.split(",")
            new_end=end.split(",")
            schema.append({
     "starttime": datetime.time(int(new_start[0]),int(new_start[1])),
     "endtime": datetime.time(int(new_end[0]),int(new_end[1])),
     "name": activity,
})
            
        
    


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
edit()
