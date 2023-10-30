# ゲームのメイン関数
def ant_game():
    print("アリをつぶす？ つぶさない？")
    user_choice = input("「つぶす」または「つぶさない」を入力してください： ").strip().lower()

    if user_choice == "つぶす":
        print("小学校入学です！")
    elif user_choice == "つぶさない":
        print("ミジンコです！")
        print("ゲームオーバー！ミジンコになりました。")
        return  # ゲーム終了
    else:
        print("無効な選択です。正しい選択を入力してください。")
        return  # ゲーム終了

    # 新しい質問
    print("次の質問:")
    print("無事に小学校に入学したあなた。今日はクラスで休みが出たよ。さて始まるのは牛乳じゃんけん。参加する？しない？")
    user_choice = input("「参加する」または「参加しない」を入力してください： ").strip().lower()

    if user_choice == "参加する":
        print("中学校入学！")
    elif user_choice == "参加しない":
        print("学校になじめず引きこもりからのニート！")
        print("ゲームオーバー！ニートになりました。")
        return  # ゲーム終了
    else:
        print("無効な選択です。正しい選択を入力してください。")
        return  # ゲーム終了
    # 新しい質問
    print("次の質問:")
    print("健全な証拠！スカートめくりあなたはする？しない？")
    user_choice = input("「する」または「しない」を入力してください： ").strip().lower()

    if user_choice == "する":
        print("高校入学！")
    elif user_choice == "しない":
        print("ニートです！")
        print("ゲームオーバー！ニートになりました。")
        return  # ゲーム終了
    else:
        print("無効な選択です。正しい選択を入力してください。")
        return  # ゲーム終了
    
     # 新しい質問
    print("次の質問:")
    print("晴れて高校となったあなた。制服をしっかり着る？着崩す？")
    user_choice = input("「しっかり着る」または「着崩す」を入力してください： ").strip().lower()

    if user_choice == "しっかり着る":
        print("大学入学！")
    elif user_choice == "着崩す":
        print("すこし制服を着崩すはずが次々と校則を破り悪い仲間とつるむように、、、エスカレートし逮捕")
        print("ゲームオーバー！更生頑張りましょう。")
        return  # ゲーム終了
    else:
        print("無効な選択です。正しい選択を入力してください。")
        return  # ゲーム終了
    
    # 新しい質問
    print("次の質問:")
    print("友達から誘われたサークルが飲みサーだった！入る？入らない？")
    user_choice = input("「入る」または「入らない」を入力してください： ").strip().lower()

    if user_choice == "入る":
        print("進級おめでとうございます！大学４年生になりました。")
    elif user_choice == "入らない":
        print("人脈を広げられなかったあなた。学校に馴染めず退学。")
        print("ゲームオーバー！大学が全てじゃないよ！＾＾")
        return  # ゲーム終了
    else:
        print("無効な選択です。正しい選択を入力してください。")
        return  # ゲーム終了
    
     # 新しい質問
    print("次の質問:")
    print("卒業後の進路どうする？")
    user_choice = input("「旅に出る」または「実家の旅館を継ぐ」を入力してください： ").strip().lower()

    if user_choice == "旅に出る":
        print("おめでとうございます。あなたは旅先で行ったインドで悟りを開き神になりました。")
    elif user_choice == "実家の旅館を継ぐ":
        print("皆を癒す愛される旅館をつくってね。")
        print("ゲームオーバー！神になれませんでした。")
        return  # ゲーム終了
    else:
        print("無効な選択です。正しい選択を入力してください。")
        return  # ゲーム終了
    

if __name__ == "__main__":
    ant_game()




