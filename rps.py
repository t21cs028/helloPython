import random

def janken():
    # プレイヤーAとプレイヤーBの手をランダムに選択
    player_a_choice = random.randint(0, 2)
    player_b_choice = random.randint(0, 2)

    # じゃんけんの手を表す辞書
    hands = {0: "グー", 1: "チョキ", 2: "パー"}

    # 勝敗判定
    if player_a_choice == player_b_choice:
        result = "引き分け"
    elif (player_a_choice == 0 and player_b_choice == 1) or (player_a_choice == 1 and player_b_choice == 2) or (player_a_choice == 2 and player_b_choice == 0):
        result = "Aの勝ち"
    else:
        result = "Bの勝ち"

    # 結果を出力
    output = f"Aの手: {hands[player_a_choice]}  vs.  Bの手: {hands[player_b_choice]}  →  {result}"
    return output

# モジュールとして使う場合の例
if __name__ == "__main__":
    result = janken()
    print(result)
