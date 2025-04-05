## this is the lecturer's evaluation script
import json
import time
import pandas as pd
import os
import xlsxwriter
from solution.extractor import Solution, normalize, same_province, same_district, same_ward

TEAM_NAME = 'TEAM_THREE'
EXCEL_FILE = f'{TEAM_NAME}.xlsx'

# Load test file
TEST_FILE = "data/test.json"
if not os.path.exists(TEST_FILE):
    raise FileNotFoundError(f"❌ Test file not found: {TEST_FILE}")

with open(TEST_FILE, encoding='utf-8') as f:
    data = json.load(f)

df = []
solution = Solution()
timer = []
correct = 0

for test_idx, data_point in enumerate(data):
    address = data_point["text"]
    answer = data_point["result"]

    answer["province_normalized"] = normalize(answer["province"], same_province)
    answer["district_normalized"] = normalize(answer["district"], same_district)
    answer["ward_normalized"] = normalize(answer["ward"], same_ward)

    start = time.perf_counter_ns()
    result = solution.process(address)
    finish = time.perf_counter_ns()
    timer.append(finish - start)

    result["province_normalized"] = normalize(result["province"], same_province)
    result["district_normalized"] = normalize(result["district"], same_district)
    result["ward_normalized"] = normalize(result["ward"], same_ward)

    province_correct = int(answer["province_normalized"] == result["province_normalized"])
    district_correct = int(answer["district_normalized"] == result["district_normalized"])
    ward_correct = int(answer["ward_normalized"] == result["ward_normalized"])

    ok = province_correct + district_correct + ward_correct
    correct += ok

    df.append([
        test_idx,
        address,
        answer["province"],
        result["province"],
        answer["province_normalized"],
        result["province_normalized"],
        province_correct,
        answer["district"],
        result["district"],
        answer["district_normalized"],
        result["district_normalized"],
        district_correct,
        answer["ward"],
        result["ward"],
        answer["ward_normalized"],
        result["ward_normalized"],
        ward_correct,
        ok,
        timer[-1] / 1_000_000_000,
    ])

# Score summary
total = len(data) * 3
score = round(correct / total * 10, 2)
max_time = round(max(timer) / 1_000_000_000, 4)
avg_time = round(sum(timer) / len(timer) / 1_000_000_000, 4)

summary_df = pd.DataFrame([[correct, total, score, max_time, avg_time]],
                          columns=['correct', 'total', 'score / 10', 'max_time_sec', 'avg_time_sec'])

columns = [
    'ID', 'text',
    'province', 'province_student',
    'province_normalized', 'province_student_normalized',
    'province_correct',
    'district', 'district_student',
    'district_normalized', 'district_student_normalized',
    'district_correct',
    'ward', 'ward_student',
    'ward_normalized', 'ward_student_normalized',
    'ward_correct',
    'total_correct',
    'time_sec'
]

df = pd.DataFrame(df, columns=columns)

# Save to Excel
writer = pd.ExcelWriter(EXCEL_FILE, engine='xlsxwriter')
summary_df.to_excel(writer, index=False, sheet_name='summary')
df.to_excel(writer, index=False, sheet_name='details')
writer.close()

print(f"\n✅ DONE. Your score is {score}/10\nSaved result to: {EXCEL_FILE}")
