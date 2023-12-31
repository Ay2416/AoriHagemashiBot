import random

phrase = [
    "共テ前には何でもできる。君の力を信じて進もう！",
    "後悔せずに成功への道を歩もう。君は素晴らしい未来を築ける。",
    "モチベーションは波があるもの。少し休んでリフレッシュしよう！",
    "共テまでのカウントダウンは緊張感を与えてくれる。君はできる！",
    "遅くないよ、君の成功はまだ可能だ。準備を進めよう！",
    "お前、またスマホいじってるの？試験まであと100日を切ってるんだぞ？さっさと勉強しろよ、まだ教科書すら開いてないじゃないか。",
    "共テに向けての覚悟を持って、君の目標に向かって進もう！",
    "3教科も完成してないのに、何をしてるんだ？焦らないと間に合わないぞ。",
    "君のペースで進むことが大切だ。焦らずに頑張ろう。",
    "もう遊びはおしまいだよ。3教科も未完成ってどういうこと？",
    "君の成功に向けた道のりはユニークで、君だけのものだ。",
    "自分の成長に喜びを感じよう。君はすでに素晴らしい進捗をしている。",
    "他の人たちはもっと頑張ってるんだ。お前も負けないように頑張れ。",
    "君自身の進捗に焦点を当てて、他人と比較しないようにしよう。",
    "他の人たちと比較するのではなく、自分の進捗に焦点を当てよう。",
    "時間は貴重だが、君の努力はそれに値する。頑張り続けよう！",
    "100日の間、君は成長し続けている。自分を信じて進もう！",
    "他の人たちのペースに流されず、自分の進捗を信じて進もう。",
    "君の努力は無駄にはならない。着実に進む姿勢を持ち続けよう。",
    "100日の間に、君は驚くほど成長できる。目標に向かって進もう！",
    "競争が激しいんだから、今からでも遅くないと思うなよ。さっさと準備しろよ。",
    "こんなペースじゃ、共テに受かるのは難しいぞ。もっとスピードアップしないと。",
    "君の努力は一つ一つのステップで報われる。目標に向かって進もう！",
    "他の人たちは真剣に取り組んでいるんだぞ。お前も負けじと頑張れよ。",
    "競争が激しい世界だからこそ、努力が必要だ。怠けてる場合じゃない。",
    "何やってるんだよ、他の奴らはもう100日前から始めてるぞ。お前は遅すぎるんじゃないか？",
    "共テで成功するためには、もっと努力が必要だ。今のままじゃダメだ。",
    "今すぐにでも行動しないと、後悔することになるかもしれないぞ。",
    "100日は新たな可能性を切り開くチャンスだ。君の未来が明るいものになるように頑張ろう！",
    "何を待ってるんだ？成功のチャンスは今なんだ。",
    "共テまでの道のりは長いかもしれないが、君がコツコツと進んでいることに誇りを持とう！",
    "やる気がないのか？共テは人生の重要な試練だぞ。覚悟を決めろ。",
    "自信を持って、君はできる！共テまで100日でも大丈夫だよ。",
    "もう何をやってるんだ？成功をつかむためにはもっと努力しないと。",
    "成功への第一歩は今から始めることだ。頑張ろう！",
    "成功への道は一歩一歩の積み重ねから始まる。焦らず、コツコツと進もう。",
    "時間は有限だが、君の努力も無駄ではない。頑張ろう！",
    "お前の努力、何のためにしてるのか理解してるのか？",
    "100日は長い時間だ。君の目標を達成しよう！",
    "他の奴らはもう頑張ってるかもしれないぞ。負けるな！",
    "君の努力は実を結ぶ日が来る。信じて続けよう！",
    "競争が激化してるんだから、急がないと取り残されるぞ。",
    "おい、遊んでる場合じゃないぞ。共テまであと100日だって言ってんだろ？今すぐ勉強しろよ、3教科とも完璧にやりこめ。",
    "共テまでの道は険しいかもしれないが、君は困難を乗り越えられる力を持っている。",
    "成功は一日で手に入るものではない。君は着実に進んでいる。",
    "共テまで100日以内なんだから、ゆとりなんてないんだよ。",
    "100日はチャンスである。君の目標を達成するために、一歩ずつ進もう！",
    "競争が激化しているからこそ、君の努力が光るチャンスだ。",
    "時間は有限だぞ。今からでも遅くないから勉強しろ！",
    "共テまでのカウントダウンはワクワク感を増してくれる。目標に向かって進もう！",
    "成功のチャンスは常にある。君はそれを掴む力があるはずだ。",
    "君の努力は無駄じゃない。目標を達成するために進んでいるんだ。",
    "もっと頭を使わないと、共テで通用するスキルは身につかないぞ。",
    "共テまであと100日を切ったら、もう寝てる場合じゃないんだよ。",
    "遅れてる暇はないぞ、共テが迫っている。今からでも取り組むべきだ。",
    "君の成長と進化はすでに始まっている。目標に向かって進もう！",
    "勉強しないでいると後悔するぞ。共テに向けて頑張れ！",
    "時間を無駄にしないように、今日から行動を起こそう。共テに向けて頑張ろう！",
    "共テの成功は君の手の届くところにある。信じて進もう！",
    "共テまでの道は険しいかもしれないが、君の決意が勝利をもたらす。",
    "共テの成功に向けて、着実に進んでいる。継続しよう！",
    "お前のモチベーション、どこに行ったんだ？もっとやる気を見せろよ。",
    "100日しかないんだ。その間に何を達成するつもりなんだ？",
    "自分の進捗を振り返りながら、自信を持って前進しよう。",
    "お前まだまともに勉強してないの？もう共テまで100日しかないぞ！",
    "君の知識とスキルは確実に向上している。頑張って続けよう。",
    "成功はコミットメントと忍耐から生まれる。君はその両方を持っている。",
    "お前、まだゲームしてるのか？共テまで100日しかないぞ。勉強しろよ、ダメだな。",
    "後悔しないために、今から行動しよう。君ならできる！",
    "競争が激しいからこそ、君の独自のスキルが輝く機会だ。",
    "君の成功は未来に向けた道のりの中にある。自分を信じて進もう！",
    "未来の君は今日の君の努力に感謝するだろう。頑張り続けよう！",
    "100日はまだたくさんの時間がある。焦らず進んでいこう！",
    "未来の君が成功を手に入れるために、今日の君が頑張る。"
]

# フレーズをシャッフル
random.shuffle(phrase)

# シャッフル後のフレーズを表示
for p in phrase:
    print('"' + p + '",')
