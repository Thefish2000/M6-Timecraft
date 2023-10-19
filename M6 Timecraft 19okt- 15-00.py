import datetime #importerar funktionen för att kunna skriva ut tiden

schema = [] #lista med dictionaries
meny_user_action= {"c":"Create activity", "v":"View activitys", "d":"Delete activity", "e": "Edit activity"}


def create(): #man tar emot användarens input
  user_input_namn = input("Skriva in aktivitets namn: ")
  user_input_time_start= input("När ska aktivitet börjar i format (xx,xx): ")
  user_input_time_end = input("När ska aktivitet slutar(xx,xx): ")
  starttime= user_input_time_start.split(",") #delar strängen 
  endtime= user_input_time_end.split(",")
  return starttime, endtime, user_input_namn 

####FIXA INPUT#####

def create_in_schema(schema,starttime,endtime,name): #
  schema.append({
     "starttime": datetime.time(int(starttime[0]),int(starttime[1])),
     "endtime": datetime.time(int(endtime[0]),int(endtime[1])),
     "name": name,})


def overlap(schema, starttime, endtime):
  new_starttime=datetime.time(int(starttime[0]),int(starttime[1]))
  new_endtime=datetime.time(int(endtime[0]),int(endtime[1]))
  for item in schema:
      item_starttime = item["starttime"]
      item_endtime = item["endtime"]
      if item_starttime < new_endtime and item_endtime > new_starttime:
        return True
      elif item_starttime == new_starttime and item_endtime == new_endtime:
        return True
  return  False

def delete(schema, prompt, beskrivning):
    user_input= input(prompt)
    user_input_starttime = input("När börjarde aktivitet?(format: xx,xx):")
    input_starttime = user_input_starttime.split(',')
    input_time_convert = datetime.time(int(input_starttime[0]),int(input_starttime[1]))
    for item in schema: 
       if item['name'] == user_input and item['starttime'] == input_time_convert:
          schema.remove(item)
          print(f"{user_input} {beskrivning}")
          return
    print("Kan inte hitta aktivitet")
        

def edit(): #redigerar en aktivite
   delete(schema, "Vilken aktivitet vill du ändra?", "kommer att ändras") #anropar delete-funktionen
   create_result = create() #man kan ändra alla parametrar i aktiviteten mha create funktionen
   starttime, endtime, user_input_namn = create_result
   overlap(schema, starttime, endtime)
   create_in_schema(schema,starttime,endtime,user_input_namn)
            

def sort_after_starttime(schema):
    sorted_list = sorted(schema, key=lambda x: x['starttime']) #lambda tar starttime som parameter från listan
    return sorted_list #returnerar sorterad lista
       

def view(schema):
  sort_list = sort_after_starttime(schema)
  today = datetime.date.today()
  print(today)
  for item in sort_list:
     starttime = item["starttime"].strftime("%H:%M")
     endtime = item["endtime"].strftime("%H:%M")
     print(f"{starttime}-{endtime}: {item['name']}")


def meny(options): 
 for key,value in options.items(): 
     print(f"{key}) {value}")
 while True:
  user_input = input("What do you want to do: ")
  if user_input in options:  
   print(f"You selected {user_input})"+ str(options.get(user_input)))
   return user_input  


def main():
   while True:
    user_action = meny(meny_user_action)
    if user_action == "c":
      while True:
       create_result = create()
       starttime, endtime, user_input_namn = create_result
       available = overlap(schema,starttime,endtime) 
       if available == False:
         create_in_schema(schema,starttime,endtime,user_input_namn)
         break
       print("Time not available")
    elif user_action == "v":
      view(schema)
    elif user_action == "d":
      delete(schema,"Skriva in namn på aktivitet som du vill tar bort: " , "raderades")
    elif user_action == "e":
      edit()

main()
