import datetime #importerar funktionen för att kunna skriva ut tiden
import re #modul som kollar för ett mönster, används för input

schema = [] #lista med dictionaries
meny_user_action= {"c":"Create activity", "v":"View activitys", "d":"Delete activity", "e": "Edit activity"}
meny_continue = {"t":"try again", "q" :"quit"}

def validate_input(input_string):
    pattern = r'^\d{2},\d{2}$' #kontrollerar om formatet av input stämmer
    if re.match(pattern, input_string):
        return True
    else:
        return False
    
def create(): #man tar emot användarens input
    user_input_namn = input("Write the name of the activity: ")
    while True: #skapar en loop for starttime
        user_input_time_start = input("When is the activity going to start? Write in format (xx,xx): ")
        if validate_input(user_input_time_start):
            while True: #skapar en loop for endtime
                user_input_time_end = input("When is the activity going to finish? Write in format (xx,xx): ")
                if validate_input(user_input_time_end):
                    starttime = user_input_time_start.split(",") 
                    endtime = user_input_time_end.split(",")
                    return starttime, endtime, user_input_namn
                else:
                    print('You have inserted the end time in a wrong format.')
                    user_input = meny(meny_continue, "Do you want to try again?: ")
                    if user_input == "t":
                      continue
                    else: return 
        else:
            print('You have inserted the start time in a wrong format.')
            user_input = meny(meny_continue, "Do you want to try again?: ")
            if user_input == "t":
             continue
            else: return
   
        
      
    
def create_in_schema(schema,starttime,endtime,name): #
  schema.append({
     "starttime": datetime.time(int(starttime[0]),int(starttime[1])),
     "endtime": datetime.time(int(endtime[0]),int(endtime[1])),
     "name": name,})
  print(f"{name} added")


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
    while True:
        user_input= input(prompt)
        user_input_starttime = input("When does the activity start(format: xx,xx):")
        if validate_input(user_input_starttime):
            input_starttime = user_input_starttime.split(',')
            input_time_convert = datetime.time(int(input_starttime[0]),int(input_starttime[1]))
            for item in schema: 
               if item['name'] == user_input and item['starttime'] == input_time_convert:
                  schema.remove(item)
                  print(f"'{user_input}' {beskrivning}")
                  return item
            print("Could not find activity")
        else: 
            print('You have inserted the starttime in a wrong format')
        user_input = meny(meny_continue, "Do you want to try again?: ")
        if user_input == "t":
           continue
        else: return
   
        

def edit(): #redigerar en aktivite
 while True:
   delete_output= delete(schema, "Which activity do you want to edit?", "will change") #anropar delete-funktionen
   if delete_output is not None:
     create_result = create() #man kan ändra alla parametrar i aktiviteten mha create funktionen
     if create_result is not None:
       starttime, endtime, user_input_namn = create_result
       available = overlap(schema,starttime,endtime) 
       if available == False:
         create_in_schema(schema,starttime,endtime,user_input_namn)
         break
       else: print("Time not available")
       user_input = meny(meny_continue, "Do you want to try again?: ")
       if user_input == "t":
         continue
       else: break
     else: schema.append(delete_output)
   else: break
   

     

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


def meny(options, description): 
 for key,value in options.items(): 
     print(f"{key}) {value}")
 while True:
  user_input = input(description)
  if user_input in options:  
   print(f"You selected {user_input})"+ str(options.get(user_input)))
   return user_input  


def main():
   while True:
    user_action = meny(meny_user_action,"What do you want to do: ")
    if user_action == "c":
      while True:
       create_result = create()
       if create_result is not None:
         starttime, endtime, user_input_namn = create_result
         available = overlap(schema,starttime,endtime) 
         if available == False:
           create_in_schema(schema,starttime,endtime,user_input_namn)
           break
         print("Time not available")
         user_input = meny(meny_continue, "Do you want to try again?: ")
       else:break
       if user_input == "t":
         continue
       else: break
    elif user_action == "v":
      view(schema)
    elif user_action == "d":
      delete(schema,"Write the name of the activity you want to delete: " , "has been deleted")
    elif user_action == "e":
      edit()
    else:
        print('That is not an option. Try again.')

main()


