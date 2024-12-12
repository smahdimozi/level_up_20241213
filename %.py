next_jalali_month = input('enter month:')
next_jalali_month = next_jalali_month % 13 or 1
if(next_jalali_month):
  print(f'you are in 2024 yet')
