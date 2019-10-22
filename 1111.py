body = input("まだ生きてるか[yes or no]")
if body == "no":
    print("もし来世があれば、もっと幸せいになりたい。")
     
elif body == "yes":
    print("生きてる良かった。")

    work = input("人工知能に関する仕事をしてるんですか[yes or no]")
    if work == "yes":
        print("理想に到達したね。")
    elif work == "no":
        print("人生には多くの欠陥があります。")
    else:
        print("無駄なことを入力しないでください。")

    wife = input("奥さんがいますか[yes or no]")
    if wife == "yes":
        print("奥さんは必ず可愛いでしょう")
        
        child = input("子供がいますか[yes or no]")
        if child == "yes":
            print("自分の子供が大事にしてるかなあ。")
        elif child == "no":
            print("5年の時間で、子供がいなくでもおかしいではない。")
        else:
            print("無駄なこと入力しないでください。")
            
    elif wife == "no":
        print("この五年、自分が何をしたか。")
    else:
        print("無駄なこと入力しないでください。")

else:
    print("無駄なこと入力しないでください。")
    
    
