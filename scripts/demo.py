from common.read_data import read_data
raw_data = read_data()
data_list = []
case_ids = []
for item in raw_data:
    data_list.append((item['case_id'], item['case_name'], item['username'], item['password'], item['image_code'], item['status_code'], item['msg'], item['code']))
    case_ids.append(f"{item['case_id']}-{item['case_name']}")
print(data_list)

print(case_ids)
