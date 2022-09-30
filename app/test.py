import json
from datetime import datetime
f = open('/home/ts/Desktop/test_task/CSV/app/csv.json')

data = json.load(f)

new_l = []
final_data = []
dict = {}
for mcode in data:
    if mcode['METERING_CODE'] not in new_l:
        new_l.append(mcode['METERING_CODE'])
        final_data.append(mcode)
        dict['mcode'] = mcode
    else:
        current_date = datetime.strptime(mcode['TIMESTAMP_UTC'], "%Y/%m/%dZ%H:%M:%S").date()
        old_date = datetime.strptime(dict['mcode']['TIMESTAMP_UTC'], "%Y/%m/%dZ%H:%M:%S").date()
        if current_date > old_date:
            for i in final_data:
                if i['METERING_CODE'] == mcode['METERING_CODE']:
                    i['TIMESTAMP_UTC'] = mcode['TIMESTAMP_UTC']
                    i["PRIMARY VALUE"] = mcode['PRIMARY VALUE']
                else:
                    pass
        else:
            pass

with open("uniq.json", "w") as file:
    json.dump(final_data, file, ensure_ascii=False)

    # for j in :
    #     if j == i:
    #         new_l.append(j)
# print(new_l)
# print('\n')
# print(final_data)
# print('\n')
# print(dict)          
# # mylist = list(dict.fromkeys(new_l))

# f.close()



# import json
# from datetime import datetime

# f = open('/home/ts/Desktop/test_task/CSV/app/csv.json')
# data = json.load(f)


# textbook_list = []
# output = []
# dict = {}
# for item in data:
#     if item['METERING_CODE'] not in textbook_list:
#         textbook_list.append(item['METERING_CODE'])
        
#         output.append(item)
        
#         dict['item'] = item
        
#     else:
#         current_date = datetime.strptime(item['TIMESTAMP_UTC'], "%Y/%m/%dZ%H:%M:%S").date()
#         old_date = datetime.strptime(dict['item']['TIMESTAMP_UTC'], "%Y/%m/%dZ%H:%M:%S").date()
#         if current_date > old_date:
#             for i in output:
#                 if i['METERING_CODE'] == item['METERING_CODE']:
#                     i['TIMESTAMP_UTC'] = item['TIMESTAMP_UTC']
#                     i["PRIMARY VALUE"] = item['PRIMARY VALUE']
#                 else:
#                     pass
#         else:
#             pass

# with open("uniq.json", "w") as file:
#     json.dump(output, file, ensure_ascii=False)