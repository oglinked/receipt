""" WollPay Receipt (Version 03.03) """

import random
import datetime
from datetime import date
import pytz
import csv
from pathlib import Path
import os

log_name = 'log.csv'

#The Greeting & information.
print('Hello Host!')
print('Please input the Data of the new Transaction.')
print('\nFull Path to log.csv file will be: \n' + os.path.abspath(log_name))
input('\nClick "ENTER" to input the Data: ')

# The transactions loope.
i = 'y'
while i == 'y' or i == 'Y':
    os.system('cls') # Clearing the Screen.
    #The Input Data Block.
    cid = input('CID: ')
    input_currency = input('Currency IN: ')
    input_summ = input('Amount IN: ')
    output_currency = input('Currency OUT: ')
    output_summ = input('Amount OUT: ')
    comment = input('Comment: ')
    cash_in = input('Cash Registrar IN: ')
    cash_out = input('Cash Registrar OUT: ')
    new_client_data = input('New data about client: ')
    general1 = input('General1: ')
    general2 = input('General2: ' )
    
    time_zone = 'GMT+2'
    

    # The calculating of rate.
    input_summ_float = float(input_summ)
    output_summ_float = float(output_summ)

    if input_summ_float >= output_summ_float: 
        rate = input_summ_float / output_summ_float
    else:
        rate = output_summ_float / input_summ_float

    rate = "{:.2f}".format(rate)

    # The random Transaction ID calculating.
    transaction_ID = random.randint(100000000000, 999999999999)
    transaction_ID = str(transaction_ID)

    # Current Date & Time getting (for Poland).
    current_time = datetime.datetime.now(pytz.timezone('Poland')) \
                .strftime('%I:%M %p')
    # current_date = date.today()
    # current_date = current_date.strftime("%m/%d/%Y") # mm/dd/YY

    # Input the current date manualy.
    current_date = input('Date: ')
    if len(current_date) < 2:
        current_date = datetime.datetime.now(pytz.timezone('Poland')) \
                       .strftime("%m/%d/%Y")
    else:
        current_date = current_date

    #The Receipt printing (the output to console).
    print('\n\n----------Welcome to WollPay!----------\n')
    print('Transfer:       ',
        input_currency,
        input_summ,
        ' --> ',
        output_currency,
        output_summ)
    print('Date:           ', current_date)
    print('Time:           ', current_time, ' ', '(' + time_zone + ')')
    print('TransactionID:  ', transaction_ID)
    print('Rate:           ', rate)
    print('\nThank you for being a WollPay customer!')
    print('----------------WollPay----------------\n\n')

    # The receipt appanding in receipt.txt file.
    with open('receipt.txt', 'a') as f:
        f.write('\n----------Welcome to WollPay!----------\n')
        f.write('\nTransfer:       '
                + input_currency 
                + ' '
                + input_summ
                + ' --> ' 
                + output_currency
                + ' ' 
                + output_summ)
        f.write('\nDate:           ' + current_date)
        f.write('\nTime:           ' + current_time 
                                    + ' ' + '(' + time_zone + ')')
        f.write('\nTransactionID:  ' + transaction_ID)
        f.write('\nRate:           ' + rate)
        f.write('\n\nThank you for being a WollPay customer!\n')
        f.write('----------------WollPay----------------\n\n')
        
    # log.csv file data:

    # field names
    fields = [
            'TransactionID',
            'Date',
            'Time',
            'TZ',
            'CID',
            'Currency1',
            'Amount1',
            'Currency2',
            'Amount2',
            'Rate',
            'Comment',
            'CashRegistrarIN',
            'CashRegistrarOUT',
            'NewData',
            'General1',
            'General2'
            ]
    # Fields values.
    row = [
        transaction_ID,
        current_date,
        current_time,
        time_zone,
        cid,
        input_currency,
        input_summ,
        output_currency,
        output_summ,
        rate,
        comment,
        cash_in,
        cash_out,
        new_client_data,
        general1,
        general2
        ]

    # Checking the log.csv file existing and writing to log.csv.
    path = Path(log_name)
    result = path.is_file()

    if result == True:
        with open(log_name, 'a', encoding='UTF8', newline='') as f:
            csvwriter = csv.writer(f, dialect='excel')
            csvwriter.writerow(row)
    else:
        with open(log_name, 'w', encoding='UTF8', newline='') as f:
            csvwriter = csv.writer(f, dialect='excel')
            csvwriter.writerow(fields) # Writing the fields.
            csvwriter.writerow(row)
    
    i = input('\nAnother Transaction? (y/n) : ')

input('Click "ENTER" to exit: ')
