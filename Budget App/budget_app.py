#This is my solution to the Budget App Problem in FCC's Scientific Computing with Python.
#You can view the original question and my repl solution @ https://repl.it/@atelicious/FCC-budget-app-solution


class Category:

    def __init__(self, category):
        # Initiates two values for category object, its name and its ledger
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=''):
        if description == ' ':
            self.ledger.append({'amount':amount, 'description': ''})
        else:
            self.ledger.append({'amount':amount, 'description': description})

    def check_funds(self, amount):
        #Checks if the amount passed in the argument is less than the total balance
        initial_balance = self.get_balance()

        if amount <= initial_balance:
            return True
        else:
            return False

    
    def withdraw(self, amount, description=''):
        #Checks if the amount can be withdrawn, if yes, withdraw then return True, otherwise return False

        if self.check_funds(amount) == True:
            if description == '':
                self.ledger.append({'amount':-amount, 'description': ''})
                return True
            else:
                self.ledger.append({'amount':-amount, 'description': description})
                return True
        else:
            return False


    def transfer(self, amount, category):
        #Checks if the amount can be transferred, if yes, transfer then return True, otherwise return False

        if self.check_funds(amount) == True:
            transfer_desc = f'Transfer to {category.category}'
            self.ledger.append({'amount':-amount, 'description':transfer_desc})
            deposit_desc = f'Transfer from {self.category}'
            category.deposit(amount, deposit_desc)
            return True
        else:
            return False

    def get_balance(self):
        #Checks the current balance of the ledger
        trial_balance = 0
        for entries in self.ledger:
            trial_balance += entries['amount']

        return trial_balance

    def __str__(self):
        #This will be the output string if we print the object
        output_string = ''

        #based on the FCC Example output, by counting the top string, we have a 30 character space to work with
        #to place the category name, we need to place it in the middle of the 30 character space, and then divide
        #the length of the name itself into two, the first half will be placed len_of_name/2 to the left of 15th space
        #and the second half will be placed len/2 to the right of the 15th space, the rest will be filled with '*'

        to_be_inserted = 15 - int(len(self.category)/2) #results of division is always float, so value is typecasted in int
        initial_stars = '*' * to_be_inserted
        output_string += initial_stars
        output_string += self.category
        output_string += '*' * (30 - len(initial_stars) - len(self.category)) + '\n'



        for keys in self.ledger:

            if len(keys['description']) > 23:
        #if len of description exceeds 23, it will exceed the 30 spaces if combined with the spaces reserved for the amount
        #therefore, we need to slice the description up to the 23th character only.
                output_string += keys['description'][0:23] 
            else:
                output_string += keys['description'].ljust(23)

            corr_amount = "%.2f" % float(keys['amount'])
            
            if len(corr_amount) > 7:
        #the same is also the case here, we need to slice the amount to 7th character only because it will exceed the 30 space limit
                output_string += corr_amount[0:7]
            else:
                output_string += corr_amount.rjust(7)
            
            output_string += '\n'

        output_string += f'Total: {str(self.get_balance())}'

        return output_string
        
    
def create_spend_chart(categories):

    #This will be the output string if the function is called
    output_string = "Percentage spent by category\n"

    #List of every category name passed in the categories argument
    category_names = []
    #List of the corresponding percentage of spending per category
    percent_list = []
    #List of the corresponding withdrawal per category
    withdraw_list = []  

    #this is the total spending for all categories
    global_categories_total = 0  
    for names in categories:
        #this is the total spending for each category
        per_category_total = 0   
        for ledger_entry in names.ledger:  
            if ledger_entry['amount'] < 0:
                per_category_total += abs(ledger_entry['amount']) 
        withdraw_list.append(per_category_total)  
        global_categories_total += per_category_total  
        category_names.append(names.category)


    for i in range(0, len(category_names)):
        #This calculates the raw percents of the corresponding spending
        raw_percents = (withdraw_list[i] / global_categories_total) * 100
        #This rounds down the raw_percentage ex. 36.5 --> 36
        round_down_percents = round(raw_percents)
        #this rounds down the round_down_percentage to nearest tens 36 --> 30 then appends to percent list
        percent_list.append(int(round_down_percents/10)*10)

    current_percent = 100
    while current_percent >= 0:
        #this prints the y-axis bar starting from 100
        output_string += str(current_percent).rjust(3) + "| "
        for percent in percent_list:
            #if percent is higher than the current count it means that an 'o' should be printed
            if percent >= current_percent:
                output_string += "o  "
            else:
                output_string += "   "
        output_string += "\n"
        current_percent -= 10
    
    #this is the dashes on the bottom
    output_string += "    -" + "-" * (len(percent_list) * 3) + "\n"

    #checks for the maximum length of names in the category_names list
    max_len = 0
    for entry in category_names:
        if len(entry) > max_len:
            max_len = len(entry)

    #iterates the printing of categories for the chart label character by character
    for i in range (0, max_len):  
        output_string += "     " 
        for names in category_names:  
            if len(names) > i:  
                output_string += names[i:i+1] + "  "
            else:
                output_string += "   "
        if i < max_len - 1: 
            output_string += "\n"
        else: 
          #do not forget this! it will return an extra line if not initialized
           output_string = output_string.rstrip('\n')
    
    return output_string