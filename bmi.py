# BMI計算ツール

history = []  # 履歴を保存するリスト

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
    return round(22.0 * (height_m ** 2), 1)

def show_history():
    if len(history) == 0:
        print("履歴がありません")
        return
    print("\n--- 履歴 ---")
    for i, h in enumerate(history):
        print(f"{i+1}. BMI: {h['bmi']} / {h['judge']}")

# メイン処理
while True:
    print("\n1: BMIを計算する")
    print("2: 履歴を見る")
    print("3: 終了")
    choice = input("選択: ")

    if choice == '1':
        height = float(input("身長（cm）: "))
        weight = float(input("体重（kg）: "))
        bmi = calc_bmi(height, weight)
        judge = judge_bmi(bmi)
        ideal = ideal_weight(height)
        print(f"\nBMI: {bmi}")
        print(f"判定: {judge}")
        print(f"理想体重: {ideal}kg")
        print(f"理想体重との差: {round(weight - ideal, 1)}kg")
        history.append({'bmi': bmi, 'judge': judge})

    elif choice == '2':
        show_history()

    elif choice == '3':
        print("終了します")
        break