import csv

apt_info_list = []
with open("apt_info_list.csv", "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row[0] != "null" and row[1] <= "2023-12-31":
            apt_info_list.append((int(row[0]), row[1]))

apt_info_list.sort(key=lambda info : info[1])

units_accum = 0     # 일별 배출량을 현재 RFID기반의 종량제를 이용하는 세대 수로 나누기 위해 세대 수 누적하여 더하기
apt_info_idx, last_idx = 0, len(apt_info_list) - 1

# RFID기반의 음식물쓰레기 세대단위 연 배출량(365일을 기준으로 했을 때의)
food_waste_discharge_quantities = []
with open("dis_date_and_quantity_list.csv", "r") as file:
    discharge_quantity = None
    year = "9999"
    day_count, csv_reader = 0, csv.reader(file)
    for row in csv_reader:
        if row[0][:4] != year:
            year = row[0][:4]

            if discharge_quantity:
                food_waste_discharge_quantities.append(discharge_quantity * (365 / day_count))

            discharge_quantity, day_count = 0, 0

        # 세대 수 누적하여 더하기
        while apt_info_idx <= last_idx and apt_info_list[apt_info_idx][1] <= row[0]:
            units_accum += apt_info_list[apt_info_idx][0]

            apt_info_idx += 1

        discharge_quantity += int(row[1]) / units_accum

        day_count += 1

    food_waste_discharge_quantities.append(discharge_quantity * (365 / day_count))
