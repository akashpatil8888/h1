hp = 30

print 'This is the story of a 14year old boy. He stays at a school in the city. His home is in a remote village of Nonpur. On a fine summer night he comes hoem for holidays. He arrives at Begusarai at 10PM.This is a surprise visit he had planned.You play as him. What to do next?  #1 look for trasnport or #2 Buy some food '
 
door = raw_input('> ')

if door == "1":
    print 'All the buses to Nonpur have left.'
    print 'what do you want to do?'
    print '#1 Call Dad'
    print '#2 Stay at bus stand till dawn'

    bear = raw_input('> ')

    if bear == "1":
        print 'No you cant. The cell phone battery is dead. And you do not know the number.how would you call?'
        print '#1 Search the bag'
        print '#2 Walk home'
        print '#3 Find a spot at the bus stand and sleep'
        
        num = raw_input('> ')
        
        if num =="1":
           print 'You find an unopened letter. It was a Rakhi sent to you by your little sister. '
           print 'The letter tells about your unlces newly constructed house near the bustop'
           print '#1 Go to the house.'
           print '#2 Too tired to walk.'
           dan = raw_input('> ')
               
           if dan == "1":
                   print 'You go to the house. The house is locked. You find a key. You get in and sleep on the coach. Around midnight, there burglary in the house. The theives tie you up and lock you in the house!!!'
           else:
                   print 'Sit down. get some rest and try exploring these options again'                     
        elif num =="2":
            print 'Certainly its a cakewalk. Good luck if you find yourself company, down those miles'
        elif num =="3":
            print ' Yup its a good idea. Find a bus in the morning'
        else:
            print 'You should eat something and stay at the bus stop till the morning to catch the bus' 
    elif bear == "2":
        print 'If you made it through the night out in the open. You catch a bus in the morning. A happy ending!'

    else:
        print 'You certainly dont like my options. Dont you?' 
elif door == "2":
    print 'Its understood that you are hungry. You could have eaten chips from your bag.'
    print 'Not much money left. Yeah, you bought less money with you'
    print '#1. How much it is?'
    print '#2. look for transport'
    print '#3. I am still hungry'
    insanity = raw_input('> ')
    if insanity == "1":
         print 'The money is just enough to buy a bus ticket. here ar your options.'
         print '#1 Ask around if a stranger can give you a ride'
         print '#2 Call Dad.'
         stang = raw_input('> ')       
        
         if stang =="1":
                print 'A stranger with a bike agrees you to take home for free.'
                print 'But he takes you to the bandits. You are kidnapped!!!!!'
        
         elif stang =="2":   
                  print 'You call your dad. He comes and picks you up'
         else:
                 
                  print 'Wait till morning to catch the bus. Good night!!'         
    elif insanity == "2":
         print 'The money is just enough to buy a bus ticket. here ar your options.'
         print '#1 Ask around if a stranger can give you a ride'
         print '#2 Call Dad.'
         stang = raw_input('> ')       
        
         if stang =="1":
                print 'A stranger with a bike agrees you to take home for free.'
                print 'But he takes you to the bandits. You are kidnapped!!!!!'
        
         elif stang =="2":   
                  print 'You call your dad. He comes and picks you up'
         else:
                 
                  print 'Wait till morning to catch the bus. Good night!!' 
    else:
        print 'Why are you playing this game???'

else:
    print 'you think for a while and fall asleep in the bus. You are back at school'