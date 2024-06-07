#Generate a formatted full name
##def formatted_name(first_name, last_name):
##   full_name = first_name + ' ' + last_name
##   return full_name.title()

##def formatted_name(first_name, last_name, middle_name):
##   full_name = first_name + ' ' + middle_name + ' ' + last_name
##   return full_name.title()

#Generate a formatted full name including a middle name
def formatted_name(first_name, last_name, middle_name=''):
   if len(middle_name) > 0:
       full_name = first_name + ' ' + middle_name + ' ' + last_name
   else:
       full_name = first_name + ' ' + last_name
   return full_name.title()
