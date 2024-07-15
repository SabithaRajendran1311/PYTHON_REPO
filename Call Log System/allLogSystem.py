def find_call_log(call_log,phone_number):
   found_entries=set()
   for entry in call_log:
      if call_log[entry]==phone_number:
        found_entries.add(entry)
   return found_entries
call_log={
    'John doe':'123-456-7890',
    'Jane Smith':'987-654-3210',
    'Arun':'555-123-4567',
    'sabi':'123-456-7890',
    'priya':'555-123-4567',
    }
phone_number='123-456-7890'
found_entries=find_call_log(call_log,phone_number)
if found_entries:
    print(f"call log entries for phone number{phone_number}:")
    for entry in found_entries:
        print(entry)
else:
       print(f"No call log entries found for phone number{phone_number}")













