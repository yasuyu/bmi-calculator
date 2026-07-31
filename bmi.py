# BMI計算ツール

def calc_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)

def judge_bmi(bmi):
    if bmi < 18.5:
        return "低体重"
    elif bmi < 25.0:
        return "普通体重"
    elif bmi < 30.0:
        return "肥満（1度）"
    else:
        return "肥満（2度以上）"

def ideal_weight(height_cm):
    height_m = height_cm / 100
    return round(22.0 * (height_m ** 2), 1)  # BMI22が理想

# メイン処理
height = float(input("身長を入力してください（cm）: "))
weight = float(input("体重を入力してください（kg）: "))

bmi = calc_bmi(height, weight)
judge = judge_bmi(bmi)
ideal = ideal_weight(height)

print(f"\nBMI: {bmi}")
print(f"判定: {judge}")
print(f"理想体重: {ideal}kg")
print(f"理想体重との差: {round(weight - ideal, 1)}kg")