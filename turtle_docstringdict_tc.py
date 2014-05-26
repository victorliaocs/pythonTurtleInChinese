﻿#
# Translated by Renyuan Lyu, in Taoyuan, Taiwan.
# renyuan.lyu@gmail.com 
# google.com/+Renyuan.lyu
#
docsdict = {

'Turtle.back':
        '''後退，一段距離。

        別名: 後退 | back | backward | bk

        參數:
        距離 -- 一個數字

        龜向後移動一段距離，方向為目前龜頭的反方向。
        不改變目前龜頭的方向。

        示例(物件名為「小龜」的實例):

        >>> 小龜.位置() # 位置 = position
        (0.00,0.00)
        >>> 小龜.後退(30) # 後退 = backward
        >>> 小龜.位置()
        (-30.00,0.00)

''',

'Turtle.begin_fill':
        '''開始填色，在一塊形狀要被填色之前呼叫。

        沒有參數。

        示例(物件名為「小龜」的實例):

        >>> 小龜.顏色(黑,紅)
        >>> 小龜.開始填色()
        >>> 小龜.畫圓(60)
        >>> 小龜.結束填色()

''',

'Turtle.begin_poly':
        '''開始紀錄多邊形的頂點。

        沒有參數。

        開始錄製多邊形的頂點。當前龜的位置
        是多邊形的第一點。

        示例(物件名為「小龜」的實例):

        >>> 小龜.開始多邊形()

''',

'Turtle.circle':
        '''畫圓，給定半徑。

        參數:
        半徑 - 一個數字
        圓弧角度(可選) - 一個數字
        步數(可選) - 一個整數

        繪製給定半徑的圓。該中心是左側橈單位
        烏龜的;程度 - 角 - 決定了哪一部分
        圓畫。如果情況沒有給出,繪製整個圓。
        如果範圍是不完整的圓,弧的一個端點是
        當前筆位置。繪製圓弧逆時針方​​向
        如果半徑為正,否則在順時針方向轉動。最後
        烏龜的方向由程度的量改變。

        由於圓是由一個內接正多邊形逼近,
        步確定步驟,使用的數量。如果沒有給出,
        它會自動計算。也許用於繪製常規
        多邊形。

        呼叫:圓(半徑)#完整的圓
        - 或:圓(半徑,圓弧角度)#弧
        - 或:圓(半徑,圓弧角度,步數)
        - 或:圓(半徑,步數= 6)#6邊形

        示例(物件名為「小龜」的實例):

        >>> 小龜.畫圓(50)
        >>> 小龜.畫圓(120,180) # 180度 代表 半圓

''',

'Turtle.clear':
        '''清除 龜在螢幕上所畫的圖， 不移動龜。

        沒有參數。

        從螢幕中刪除龜所畫的圖。不要移動龜。
        龜的位置和狀態以及其他的圖，
        不會受到影響。

        示例(物件名為「小龜」的實例):

        >>> 小龜.清除()

''',

'Turtle.clearstamp':
        '''清除蓋章 根據指定的編號

        參數:
        stampid  - 一個整數,必須是曾經回傳的蓋章的編號。

        示例(物件名為「小龜」的實例):

        >>> 小龜.顏色(藍)
        >>> 一個章= 小龜.蓋章()
        >>> 小龜.前進(50)
        >>> 小龜.清除蓋章(一個章)

''',

'Turtle.clearstamps':
        '''清除蓋章群，所有的或前後 n 個 小龜的蓋章。

        可選參數:
        北 - 一個整數

        if n is None, 清除全部,
        elif n > 0 清除前n個,
        elif n < 0 清除後n個。

        示例(物件名為「小龜」的實例):

        >>>for i in 範圍(8):
        ... 小龜.蓋章(); 小龜.前進(30)
        ...
        >>> 小龜.清除蓋章群(2)
        >>> 小龜.清除蓋章群(-2)
        >>> 小龜.清除蓋章群()

''',

'Turtle.clone':
        '''複製另一隻 龜。

        沒有參數。

        創建並回傳龜的複製品,有相同位置、標題
        和屬性。

        示例(物件名為「米克龜」的實例):

        米克龜= 龜類()
        喬伊龜= 米克龜.複製()

''',

'Turtle.color':
        '''回傳或設定 顏色 並且 填色。

        參數:
        多種輸入格式是允許的。
        它們用 0, 1, 2, 或3個參數, 如下所示:

        顏色()
            回傳當前的「筆色」和當前的「填色」
            成為一對顏色字串作為回傳值
            與 筆色() 和 填色() 2個函數的傳回值一樣。
        顏色(colorstring),顏色((r,g,b)),顏色(r,g,b)
            輸入筆色, 或同時輸入 筆色與填色,
            為給定值。
        顏色(colorstring1,colorstring2)
        顏色((R1,G1,B1),(R2,G2,B2))
            相當於筆色(colorstring1)和填色(colorstring2)
            並且類似地,如果使用其他顏色的格式也一樣。

        如果龜形是一個多邊形,輪廓和多邊形的內部
        以新設置的顏色來繪製。
        如需更多信息請參見: 筆色, 填色

        示例(物件名為「小龜」的實例):

        >>> 小龜.顏色(紅,綠)
        >>> 小龜.顏色()
        ('red',"green")
        >>> 顏色模式(255)
        >>>顏色((40,80,120),(160,200,240))
        >>>顏色()
        ('#285078','#a0c8f0')

''',

'Turtle.degrees':
        '''設 角的度量單位為 「度數」。

        可選參數:
        fullcircle  - 一個數字

        設定角度測量單位,即設定數
        '度'為一個完整的圓。Dafault值
        為 360 度。

        示例(物件名為「小龜」的實例):

        >>> 小龜.左轉(90)
        >>> 小龜.頭向()
        90

        可改變角的度量單位 為 grad ( 也稱作 gon, grade, 或 gradian)，
        定義為「直角」定為 100 grads，所以全圓定為 400 grads。
        >>> 小龜.角度(400.0)
        >>> 小龜.頭向()
        100


''',

'Turtle.distance':
        '''回傳 從 本身位置 到 座標 x, y 的距離。

        參數:
        x  - 一個數字或數字的一對/矢量或烏龜實例
        Ÿ - 一些無無

        呼叫: 距離(x,y)    # 兩個坐標
        - 或: 距離((x,y))  # 一對(元組)
        - 或: 距離(vec)    # 與 pos() 的回傳值一樣
        - 或: 距離(mypen)  # 其中 mypen 是另一個龜

        示例(物件名為「小龜」的實例):

        >>> 小龜.位置()
        (0.00,0.00)
        >>> 小龜.距離(30,40)
        50.0
        >>> 筆= 龜類()
        >>> 筆.前進(77)
        >>> 小龜.距離(筆)
        77.0

''',

'Turtle.dot':
        '''畫點，可指定直徑大小及顏色。

        可選參數:
        尺寸 - 一個整數 >= 1(如果有的話)
        顏色 - 一個 colorstring 或 顏色的數字元組(r,g,b)

        畫一個圓點, 使用給定的直徑大小及顏色。
        如果直徑大小沒有給定, 就用 pensize +4 和 2 * pensize 中較大的值。

        示例(物件名為「小龜」的實例):

        >>> 小龜.畫點()
        >>> 小龜.前進(50); 小龜.畫點(20,藍); 小龜.前進(50)

''',

'Turtle.down':
        '''下筆 - 移動時畫圖。

        別名: 下筆 | pendown | pd | down

        沒有參數。

        示例(物件名為「小龜」的實例):

        >>> 小龜.下筆()

''',

'Turtle.end_fill':
        '''結束填色，在呼叫過 開始填色() 後，呼叫本函數會把整個形狀填滿顏色。

        沒有參數。

        示例(物件名為「小龜」的實例):

        >>> 小龜.顏色("黑","紅")
        >>> 小龜.開始多邊形()
        >>> 小龜.circle(60)
        >>> 小龜.end_fill()

''',

'Turtle.end_poly':
        '''停止記錄多邊形的頂點。

        沒有參數。

        停止記錄多邊形的頂點。當前龜位置為多邊形
        最後一點。它將與第一點相連接。

        示例(物件名為「小龜」的實例):

        >>> 小龜.結束多邊形()

''',

'Turtle.fillcolor':
        '''回傳或設定 填色。

        參數:
        四個輸入格式是允許的:
          - 填色()
            回傳當前的填色之顏色字串,
            可能是十六進制數字格式(見示例)。
            可以作為輸入到另一個 顏色/ 筆色/填色 函數的呼叫。
          - 填色(colorstring)
            colorstring 是一個 Tk 顏色字串,如 "紅色" 或 "黃色"
          - 填色((r,g,b))
            一個(r,g,b)顏色元組,
            其中，每個 r,g,b 值的範圍在 0 .. colormode,
            其中，colormode 是 1.0 或 255
          - 填色(r,g,b)



        如果 龜形 是多邊形, 該多邊形的內部用
        新設定的顏色來填充。

        示例(物件名為「小龜」的實例):

        >>> 小龜.fillcolor('紫')
        >>>山坳= 小龜.筆色()
        >>> 小龜.fillcolor(COL)
        >>> 小龜.fillcolor(0,0.5,0)

''',

'Turtle.filling':
        '''測試是否正在填色。。

        沒有參數。

        示例(物件名為「小龜」的實例):

        >>> 小龜.開始多邊形()
        >>>if 小龜.正在填色():
        ...     小龜.筆大小(5)
        ... else:
        ...     小龜.筆大小(3)

''',

'Turtle.forward':
        '''龜前進指定的距離。

        別名: 前進 | forward | fd

        參數:
        距離 - 一個數字(整數或浮點數)

        龜前進指定的距離, 往
        龜頭的方向。

        示例(物件名為「小龜」的實例):

        >>> 小龜.位置()
        (0.00,0.00)
        >>> 小龜.前進(25)
        >>> 小龜.位置()
        (25.00,0.00)
        >>> 小龜.前進(-75)
        >>> 小龜.位置()
        (-50.00,0.00)

''',

'Turtle.get_poly':
        '''回傳最近記錄的多邊形。

        沒有參數。

        示例(物件名為「小龜」的實例):

        >>> p = 小龜.get_poly()
        >>> 小龜.register_shape("myFavouriteShape", p)

''',

'Turtle.get_shapepoly':
        '''回傳當前 多邊形 形狀 的 坐標 元組。

        沒有參數。

        示例(物件名為「小龜」的實例):

        >>> 小龜.shape("正方形")
        >>> 小龜.shapetransform(4,-1,0,2)
        >>> 小龜.get_shapepoly()
        ((50,-20),(30,20),(-50,20),(-30,-20))


''',

'Turtle.getpen':
        '''回傳 龜 物件。

        沒有參數。

        只有合理的使用:作為一個函數來回傳'匿名龜":

        例如:
        >>>寵物= getturtle()
        >>>寵物.fd(50)
        >>>寵物
        <turtle.Turtle object at 0x0187D810>
        >>>龜群()
        [<turtle.Turtle object at 0x0187D810>]

''',

'Turtle.getscreen':
        '''回傳 龜螢幕 物件, 龜就是在這上面畫圖。

        沒有參數。

        回傳 TurtleScreen 物件, 龜就是在這上面畫圖。
        所以 TurtleScreen-方法 可以 被該物件呼叫。

        示例(物件名為「小龜」的實例):

        >>> 小龜的螢幕 = 小龜.getscreen()
        >>> 小龜的螢幕
        <turtle.TurtleScreen object at 0x0106B770>
        >>> 小龜的螢幕.bgcolor("粉紅色")

''',

'Turtle.getturtle':
        '''回傳 龜物件 本身。

        沒有參數。

        只有合理的使用: 作為一個函數來回傳 '匿名龜':

        例如:
        >>>寵物= getturtle()
        >>>寵物.fd(50)
        >>>寵物
        <turtle.Turtle object at 0x0187D810>
        >>>龜群()
        [<turtle.Turtle object at 0x0187D810>]

''',

'Turtle.goto':
        '''龜前往一個絕對位置。

        別名: 前往 | setpos | setposition | goto:

        參數:
        x  -- 一個數字 或 一對數字/向量
        y  -- 一個數字  或    無

        呼叫: 前往(x,y)     # 兩個坐標值
        - 或: 前往((x,y))   # 一個元組
        - 或: 前往(vec)     # 與 pos() 回傳一樣。

        龜移動到一個絕對位置。如果筆是下筆狀態,
        將畫出一條線。龜頭的方向不會改變。

        示例(物件名為「小龜」的實例):

        >>> 位置 = 小龜.pos()
        >>> 位置
        (0.00,0.00)
        >>> 小龜.setpos(60,30)
        >>> 小龜.pos()
        (60.00,30.00)
        >>> 小龜.setpos((20,80))
        >>> 小龜.pos()
        (20.00,80.00)
        >>> 小龜.setpos(TP)
        >>> 小龜.pos()
        (0.00,0.00)

''',

'Turtle.heading':
        '''回傳當前龜頭的方向。

        沒有參數。

        示例(物件名為「小龜」的實例):

        >>> 小龜.左轉(67)
        >>> 小龜.頭向()
        67.0

''',

'Turtle.hideturtle':
        '''藏龜，把龜隱藏起來。

        別名: 藏龜 | 藏 | hideturtle | ht

        沒有參數。

        當你在畫複雜的圖時，
        這樣做是一個好主意，
        因為隱藏龜會加快畫圖速度。

        示例(物件名為「小龜」的實例):

        >>> 小龜.藏()

''',

'Turtle.home':
        '''回家，讓龜回到原點 - 坐標(0,0)。

        沒有參數。

        讓龜回到原點 - 坐標(0,0), 並設其龜頭方向
        為初始狀態。

        示例(物件名為「小龜」的實例):

        >>> 小龜.回家()

''',

'Turtle.isdown':
        '''測試是否為下筆狀態。傳回真假值(True/False)。

        沒有參數。

        示例(物件名為「小龜」的實例):

        >>> 小龜.提筆()
        >>> 小龜.isdown()
        True
        >>> 小龜.下筆()
        >>> 小龜.isdown()
        False

''',

'Turtle.isvisible':
        '''測試是否為可見狀態。傳回真假值(True/False)。

        沒有參數。

        示例(物件名為「小龜」的實例):

        >>> 小龜.hideturtle()
        >>>小龜.isvisible()
        False

''',

'Turtle.left':
        '''龜左轉一個角度。

        別名: 左轉 | left | lt

        參數:
        角度 - 一個數字(整數或浮點數)

        龜左轉一個角度。(單位預設為「度數」(0~360),
        但可以藉由設定 degrees() and radians() 來改變設置。)
        角方向取決於初始模式。(請參閱...。)

        示例(物件名為「小龜」的實例):

        >>> 小龜.heading()
        22.0
        >>> 小龜.left(45)
        >>> 小龜.heading()
        67.0

''',

'Turtle.onclick':
        '''針對 此龜在畫布上， 連結 點擊鼠鍵的事件 (mouse-click event) 到一個函數。

        參數:
        函數名 -- 有 2 個參數的函數之名稱,
                  該 2 個參數 代表 鼠鍵 點擊之位置的座標。
        鼠鍵號碼 -- 1,2,3 代表 左、中、右鍵，預設為 1 (滑鼠左鍵)。
        是否加 --  True或False。如果為True,新的連結將被加上, 否則
                它將取消之前的連結。

        舉例：針對「匿名龜」, 即較簡單的程序(procedural)的方式 (非物件導向型):

        >>>def 轉彎(x,y):
        ...     left(360)
        ...
        >>>onclick(轉彎) # 現在 點擊事件 與 轉彎 函數 連結在一起。
        >>>onclick(None) # 事件連結將被刪除

''',

'Turtle.ondrag':
        '''針對 此龜在畫布上， 連結 移動滑鼠的事件 (mouse-move event) 到一個函數。

        參數:
        函數名 -- 有 2 個參數的函數之名稱,
                  該 2 個參數 代表 鼠鍵 點擊之位置的座標。
        鼠鍵號碼 -- 1,2,3 代表 左、中、右鍵，預設為 1 (滑鼠左鍵)。

        針對龜所作的滑鼠移動事件, 每一個事件序列前面都有一個
        點擊鼠鍵的事件。

        示例(物件名為「小龜」的實例):

        >>> 小龜.ondrag(小龜.goto)

        隨後的滑鼠點擊並拖拉會 在螢幕上 移動 龜
        從而產生 handdrawings
        (如果目前是處於下筆狀態的話 )。

''',

'Turtle.onrelease':
        '''針對 此龜在畫布上， 連結 放開鼠鍵的事件 (mouse-button-release event) 到一個函數。

        參數:
        函數名 -- 有 2 個參數的函數之名稱,
                  該 2 個參數 代表 鼠鍵 點擊之位置的座標。
        鼠鍵號碼 -- 1,2,3 代表 左、中、右鍵，預設為 1 (滑鼠左鍵)。

        示例(物件名 為 喬伊龜 的 我的龜類 實例):
        >>>class 我的龜類(龜類):
        ...     def 發光(自己,x,y):
        ...             自己.填色("red")
        ...     def 不發光(自己,x,y):
        ...             自己.填色("")
        ...
        >>> 喬伊龜 = 我的龜類()
        >>> 喬伊龜.onclick(喬伊龜.發光)
        >>> 喬伊龜.onrelease(喬伊龜.不發光)

        點擊 喬伊龜 讓它變成紅色, 不點擊 則把它給
        變成透明的。

''',
################ ry @ 2014/03/14, 09:25 pm
'Turtle.pen':
        '''回傳或設置筆的屬性。

        參數:
            筆 - 一個 Python 字典 資料型態，記錄著一些下面列出的關鍵字。
            **筆字典  - 一個或多個 關鍵字=參數 的參數。
                        記錄著一些下面列出的關鍵字。

        回傳或設置畫筆的屬性,在"筆字典"
        用下面的 關鍵字/值 配對:
           "shown"      :   True/False
           "pendown"    :   True/False
           "筆色"   :   color-string or color-tuple
           "fillcolor"  :   color-string or color-tuple
           "pensize"    :   positive number
           "speed"      :   number in range 0..10
           "resizemode" :   "auto" or "user" or "noresize"
           "stretchfactor": (positive number, positive number)
           "剪切因子":   number
           "outline"    :   positive number
           "tilt"       :   number

        這本詞典可以作為參數進行後續
        筆()調用來恢復以前的筆狀態。而且一個
        以上這些屬性可以被設置為關鍵字參數。
        這可以用來在一個語句中設置幾筆的屬性。


        示例(物件名為「小龜」的實例):

        >>> 小龜.pen(fillcolor="black", 筆色="red", pensize=10)
        >>> 小龜.pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        '筆色': 'red', 'pendown': True, 'fillcolor': 'black',
        'stretchfactor': (1,1), 'speed': 3, '剪切因子': 0.0}
        >>> penstate=小龜.pen()
        >>> 小龜.顏色("yellow","")
        >>> 小龜.提筆()
        >>> 小龜.pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        '筆色': 'yellow', 'pendown': False, 'fillcolor': '',
        'stretchfactor': (1,1), 'speed': 3, '剪切因子': 0.0}
        >>> p.pen(penstate, fillcolor="green")
        >>> p.pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        '筆色': 'red', 'pendown': True, 'fillcolor': 'green',
        'stretchfactor': (1,1), 'speed': 3, '剪切因子': 0.0}

''',

'Turtle.pencolor':
        '''回傳或設 筆色。

        參數:
        四個輸入格式是允許的:
          -  筆色()
            回傳當前筆色顏色規範字符串,
            可能在十六進制數字格式(見示例)。
            可以作為輸入到另一個顏色/ 筆色 /填充顏色的呼叫。
          -  筆色(colorstring)
            s是一個Tk顏色規範字符串,如"紅色"或"黃色"
          -  筆色((R,G,B))
            * R,G,和B,它們代表,一個RGB彩色的元組*,
            並且每個R,G,B的範圍在0 .. colormode,
            其中colormode是1.0或255
          -  筆色(R,G,B)
            的r,g,和b表示RGB顏色和各r的,g和b
            的範圍是0 .. colormode

        如果龜形是多邊形,該多邊形的輪廓繪製
        與新設置的筆色。

        示例(物件名為「小龜」的實例):

        >>> 小龜.筆色('棕色')
        >>> TUP =(0.2,0.8,0.55)
        >>> 小龜.筆色(TUP)
        >>> 小龜.筆色()
        '#33cc8c"

''',

'Turtle.pendown':
        '''下筆 - 移動時繪製。

        別名:落筆| PD |跌

        沒有參數。

        示例(物件名為「小龜」的實例):

        >>> 小龜.下筆()

''',

'Turtle.pensize':
        '''設置或回傳線條的粗細。

        別名:pensize |寬度

        參數:
        寬度 - 正數

        設置線的粗細與寬度或退貨。如果resizemode設置
        "自動"和龜形是一個多邊形,該多邊形的繪製
        相同的線的粗細。如果沒有給出參數,電流pensize
        回傳。

        示例(物件名為「小龜」的實例):

        >>> 小龜.筆大小()
        1
        >>> 小龜.筆大小(10) #從現在開始以寬度為10線繪製

''',

'Turtle.penup':
        '''提筆 -- 移動時無畫線。

        別名:抬筆| PU |起來

        沒有參數

        示例(物件名為「小龜」的實例):

        >>> 小龜.提筆()

''',

'Turtle.position':
        ''' 回傳 龜的當前位置(X,Y),資料型態是Vec2D向量。

        別名:POS |位置

        沒有參數。

        示例(物件名為「小龜」的實例):

        >>> 小龜.pos()
        (0.00,240.00)

''',

'Turtle.radians':
        '''設置角度測量單位為弧度(單位圓的弧長)。

        沒有參數。

        示例(物件名為「小龜」的實例):

        >>> 小龜.heading()
        90
        >>> 小龜.radians()
        >>> 小龜.heading()
        1.5707963267948966

''',

'Turtle.reset':
        '''重設，刪除龜的圖和恢復其預設值。

        沒有參數。

        從螢幕中刪除龜的圖紙,重新置中龜
        並設置變量的缺省值。

        示例(物件名為「小龜」的實例):

        >>> 小龜.position()
        (0.00,-22.00)
        >>> 小龜.heading()
        100.0
        >>> 小龜.reset()
        >>> 小龜.position()
        (0.00,0.00)
        >>> 小龜.heading()
        0.0

''',

'Turtle.resizemode':
        ''' 重設大小模式: "auto", "user", "noresize"

        (可選)參數:
        RMODE  - 的琴弦"自動"之一,"用戶","NORESIZE"

        不同resizemodes具有以下效果:
          - "自動"適應龜的外觀
                   對應於pensize的值。
          - "用戶"適應龜根據外觀
                   的stretchFactor和outlinewidth(輪廓)的值,
                   這是由shapesize()設置
          - "NORESIZE"沒有適應龜的外觀發生。
        如果沒有給出參數,回傳當前resizemode。
        resizemode("用戶")被調用帶參數調用shapesize的。


        示例(物件名為「小龜」的實例):

        >>> 小龜.resizemode("noresize")
        >>> 小龜.resizemode()
        "noresize"

''',

'Turtle.right':
        '''右轉，一個角度。

        別名:右| RT

        參數:
        角度 - 一個數字(整數或浮點數)

        龜轉向右角度單位。(單位是默認度,
        但可以通過度()和弧度()函數來設置。)
        角方向取決於模式。(請參閱本。)

        示例(物件名為「小龜」的實例):

        >>> 小龜.heading()
        22.0
        >>> 小龜.right(45)
        >>> 小龜.heading()
        337.0

''',

'Turtle.setheading':
        '''設龜頭的方向。

        別名: setheading |賽斯

        參數:
        to_angle  - 一個數字(整數或浮點數)

        將龜to_angle的方向。
        這裡有度數一些常見的方向:

                標準模式  logo模式:
        ----------------|------------
           0  - 東      |    北
          90  - 北      |    東
         180  - 西      |    南
         270  - 南      |    西

        示例(物件名為「小龜」的實例):

        >>> 小龜.setheading(90)
        >>> 小龜.heading()
        90

''',

'Turtle.settiltangle':
        '''旋轉龜形到指定的方向

        參數:角度 - 數字

        旋轉龜形指向的角度所指定的方向,
        不管其目前的傾斜角度。不要更改龜的
        標題(運動方向)。


        示例(物件名為「小龜」的實例):

        >>> 小龜.shape("turtle")
        >>> 小龜.shapesize(5,2)
        >>> 小龜.settiltangle(45)
        >>> 蓋章()
        >>> 小龜.fd(50)
        >>> 小龜.settiltangle(-45)
        >>> 蓋章()
        >>> 小龜.fd(50)

''',

'Turtle.setundobuffer':
        '''設置或禁用回復暫存區。

        參數:
        尺寸 - 一個整數或無

        如果尺寸是整數給定大小的空白回復暫存區安裝。
        尺寸給出了龜的行動可撤消的最大數目
        使用undo()函數。
        如果大小是無,無回復暫存區存在。

        示例(物件名為「小龜」的實例):

        >>> 小龜.set回復暫存區(42)

''',

'Turtle.setx':
        '''設置龜的 x 坐標

        參數:
        x  - 一個數字(整數或浮點數)

        將龜的第一個坐標為x,離開第二個坐標
        不變。

        示例(物件名為「小龜」的實例):

        >>> 小龜.position()
        (0.00,240.00)
        >>> 小龜.setx(10)
        >>> 小龜.position()
        (10.00,240.00)

''',

'Turtle.sety':
        '''設置龜的 y 坐標

        參數:
        Ÿ - 一個數字(整數或浮點數)

        將龜的第一個坐標為x,第二個坐標遺骸
        不變。

        示例(物件名為「小龜」的實例):

        >>> 小龜.position()
        (0.00,40.00)
        >>> 小龜.sety(-10)
        >>> 小龜.position()
        (0.00,-10.00)

''',

'Turtle.shape':
        '''設置龜形狀，指定形狀名稱 或 回傳當前形狀名稱。

        可選參數:
        名稱 - 一個字符串,它是一個有效的shapename

        設置烏龜形狀塑造與給定的名稱,或者,如果名字沒有給出,
        回傳當前形狀的名稱。
        形狀與名必須存在於TurtleScreen的形狀字典。
        目前有下列多邊形形狀:
        'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'.
        要了解如何處理形狀看螢幕方法 register_shape。

        示例(物件名為「小龜」的實例):

        >>> 小龜.shape()
        'arrow'
        >>> 小龜.shape('turtle')
        >>> 小龜.shape()
        'turtle'

''',

'Turtle.shapesize':
        '''設置/回傳龜的 展延因子 /輪廓。設置 重設大小模式 為"user"。

        可選參數:
           stretch_wid:正數
           stretch_len:正數
           概述:正數

        回傳或設置畫筆的屬性的x / y-展延因子和/或輪廓。
        設置resizemode為"用戶"。
        當且僅當resizemode被設置為"用戶",龜將被顯示
        根據其展延因子拉伸:
        stretch_wid是的stretchFactor垂直方向
        stretch_len是的stretchFactor在龜定向方向。
        綱要確定的形狀輪廓的寬度。

        示例(物件名為「小龜」的實例):

        >>> 小龜.resizemode("user")
        >>> 小龜.shapesize(5,5,12)
        >>> 小龜.shapesize(outline=8)

''',

'Turtle.shapetransform':
        '''設置或回傳龜形狀的當前變換矩陣。

        可選參數: t11, t12, t21, t22 --  數字。

        如果沒有適合的矩陣元素被給定的,則回傳該變換
        矩陣。
        否則設置給定的元素,改造龜形
        根據矩陣組成的第一行T11,T12和
        第二行T21,22。
        根據修改的stretchFactor,剪切因子和tiltangle
        給定矩陣。

        示例(物件名為「小龜」的實例):

        >>> 小龜.shape("square")
        >>> 小龜.shapesize(4,2)
        >>> 小龜.shearfactor(-0.5)
        >>> 小龜.shapetransform()
        (4.0,-1.0,-0.0,2.0)

''',

'Turtle.shearfactor':
        '''設置或回傳當前剪切因子。

        可選參數:剪切 - 號,切線剪切角的

        根據給定的剪切因子剪切剪切龜形,
        這是剪切角的正切值。不要更改
        龜的標題(移動方向)。
        如果剪切沒有給出:回傳當前剪切因子,即
        剪切角的正切值,通過該線平行於
        標題烏龜被剪切。

        示例(物件名為「小龜」的實例):

        >>> 小龜.shape("circle")
        >>> 小龜.shapesize(5,2)
        >>> 小龜.shearfactor(0.5)
        >>> 小龜.shearfactor()
        >>> 0.5

''',

'Turtle.showturtle':
        '''顯龜，讓烏龜可見。

        別名:showturtle | ST

        沒有參數。

        示例(物件名為「小龜」的實例):

        >>> 小龜.hideturtle()
        >>> 小龜.showturtle()

''',

'Turtle.speed':
        '''回傳或設置龜的速度。

        可選參數:
        速度 - 範圍為0 .. 10或speedstring一個整數(見下文)

        範圍為0 .. 10集烏龜的速度為整數值。
        如果沒有給出參數:回傳當前速度。

        若輸入大於10的一些大於或小於0.5時,
        速度被設定為0。
        Speed​​strings被映射到speedvalues​​以下面的方式:
            'fastest' :  0
            'fast'    :  10
            'normal'  :  6
            'slow'    :  3
            'slowest' :  1
        速度從1至10的強制執行越來越快的動畫
        畫線和龜轉折點。

        注意:
        速度= 0:*沒有*動畫發生。前進/後退,使龜跳
        同樣地左/右使烏龜變成瞬間。

        示例(物件名為「小龜」的實例):

        >>> 小龜.speed(3)

''',

'Turtle.stamp':
        '''蓋章，印記龜形的副本到畫布上,並回傳其 id 編號。

        沒有參數。

        郵票烏龜形狀的副本到畫布上的電流
        龜位置。回傳stamp_id該郵票,它可以是
        用於通過調用clearstamp將其刪除(stamp_id)。

        示例(物件名為「小龜」的實例):

        >>> 小龜.顏色("藍")
        >>> 小龜.stamp()
        13
        >>> 小龜.fd(50)

''',

'Turtle.tilt':
        '''傾斜形狀，一個角度。

        參數:
        角度 - 一個數字

        通過角從目前的傾斜角度旋轉龜形,
        但是不改變龜的前進方向。

        示例(物件名為「小龜」的實例):

        >>> 小龜.shape(""circle"")
        >>> 小龜.shapesize(5,2)
        >>> 小龜.tilt(30)
        >>> 小龜.fd(50)
        >>> 小龜.tilt(30)
        >>> 小龜.fd(50)

''',

'Turtle.tiltangle':
        '''設置或回傳當前的傾斜角度。

        可選參數:角度 - 數字

        旋轉龜形指向的角度所指定的方向,
        不管其目前的傾斜角度。不要更改龜的
        標題(運動方向)。
        如果角度沒有給出:回傳當前的傾斜角度,即角
        該龜形的方位的標題之間
        龜(其運動方向)。

        Python 3.1 不贊成使用

        示例(物件名為「小龜」的實例):

        >>> 小龜.shape("圓")
        >>> 小龜.shapesize(5,2)
        >>> 小龜.tilt(45)
        >>> 小龜.tiltangle()

''',

'Turtle.towards':
        '''計算並回傳 龜頭朝向 點(x,y) 的角度，亦即從龜的位置 到點(X,Y) 的線 的角度 (角度的度量是以東或北為起點)。

        參數:
        x  - 一個數字或數字的一對/矢量或烏龜實例
        Ÿ - 一些無無

        呼叫:towards(X,Y) #兩個坐標
        - 或:towards((X,Y)) #一對(元組)
        - 或:towards(VEC) #例如,作為回傳()
        - 或:towards(mypen) #,其中mypen是另一個龜

        回傳的角度,該行從龜位置到位置之間
        由x,y和龜的開始方向指定。(取決於
        模式 - "標準"或"logo")

        示例(物件名為「小龜」的實例):

        >>> 小龜.pos()
        (10.00,10.00)
        >>> 小龜.towards(0,0)
        225.0

''',

'Turtle.undo':
        '''撤消(重複),最近的動作。

        沒有參數。

        撤消(重複),最後龜行動。
        可撤消動作的數量是根據大小來決定
        該回復暫存區。

        示例(物件名為「小龜」的實例):

        >>>for i in range(4):
        ...     小龜.fd(50); 小龜.lt(80)
        ...
        >>>for i in range(8):
        ...     小龜.undo()
        ...

''',

'Turtle.undobufferentries':
        '''回傳的條目數在回復暫存區。

        沒有參數。

        示例(物件名為「小龜」的實例):

        >>>while  undobufferentries():
        ...     undo()

''',

'Turtle.write':
        '''在當前位置 寫字。

        參數:
        精氨酸 - 信息,它被寫入到TurtleScreen
        移動(可選) - 真/假
        對齊(可選) - 在字符串中的一個"左","中心"或右"
        字體(可選) - 三(字體名,字號,fonttype)

        寫文字 -  arg的字符串表示形式 - 在當前
        根據對準龜位置("左","中心"或右")
        並用給定的字體。
        如果此舉是真,筆移動到右下角
        的文字。默認情況下,此舉為False。

        示例(物件名為「小龜」的實例):

        >>> 小龜.write('首頁=', True, align="center")
        >>> 小龜.write((0,0),True)

''',

'Turtle.xcor':
        '''回傳龜的x坐標。

        沒有參數。

        示例(物件名為「小龜」的實例):

        >>>重設()
        >>>小龜.left(60)
        >>>小龜.forward(100)
        >>>小龜.xcor()
        50.0

''',

'Turtle.ycor':
        '''回傳龜的y坐標
        ---
        沒有參數。

        示例(物件名為「小龜」的實例):

        >>>重設()
        >>>小龜.left(60)
        >>>小龜.forward(100)
        >>>小龜.ycor()
        86.6025403784

''',
### by renyuan, 2014/03/15
'_Screen.bgcolor':
        '''背景色，設置或回傳 TurtleScreen 中的 backgroundColor。

        參數(如果有):顏色字符串或三個數字
        在範圍0 .. colormode或一個三元組這樣的數字。

        示例(物件名為「螢幕」的實例):

        >>> 螢幕.bgcolor("橙色")
        >>> 螢幕.bgcolor()
        "橙色"
        >>> 螢幕.bgcolor(0.5,0,0.5)
        >>> 螢幕.bgcolor()
        '#800080'

''',

'_Screen.bgpic':
        '''背景圖，設置或回傳背景圖片。

        可選參數:
        picname  - 一個GIF文件或"nopic"的字符串,名稱。

        如果picname是一個文件名,設置相應的圖片作為背景。
        如果picname是"nopic",刪除將backgroundImage,如果存在的話。
        如果picname是無,回傳當前和backgroundImage的文件名。

        示例(物件名為「螢幕」的實例):

        >>> 螢幕.bgpic()
        "nopic"
        >>> 螢幕.bgpic("landscape.gif")
        >>> 螢幕.bgpic()
        "landscape.gif"

''',

'_Screen.bye':
        '''關閉 turtlegraphics 視窗。

        示例(物件名為「螢幕」的實例):

        >>> 螢幕.bye()

''',

'_Screen.clearscreen':
        '''清除螢幕，從 TurtleScreen 刪除所有圖和龜。

        沒有參數。

        復位空TurtleScreen到其初始狀態:白色背景,
        沒有將backgroundImage,沒有eventbindings和跟踪。

        示例(物件名為「螢幕」的實例):

        >>> 螢幕.clear()

        注意:這個方法不作函數使用。

''',

'_Screen.colormode':
        '''回傳 colormode 或將其設置為 1.0 或 255。

        可選參數:
        CMODE  - 值 1.0 或 255 之一

         r, g, b colortriples的B值必須在範圍0 .. CMODE。

        示例(物件名為「螢幕」的實例):

        >>> 螢幕.colormode()
        1.0
        >>> 螢幕.colormode(255)
        >>> 筆色(240,160,80)

''',

'_Screen.delay':
        '''回傳或設置畫面更新的延遲時間 以毫秒為單位。

        可選參數:
        延遲 - 正整數

        示例(物件名為「螢幕」的實例):

        >>> 螢幕.delay(15)
        >>> 螢幕.delay()
        15

''',

'_Screen.exitonclick':
        '''在點擊時離開。 進入到主​​迴圈, 直到鼠標點擊, 關閉視窗, 優雅地離開。。

        沒有參數。

        綁定再見()方法來點擊鼠標就TurtleScreen。
        如果"using_IDLE" - 在配置詞典值為False
        (默認值),進入主循環。
        如果空閒與-n開關(無子)時,該值應為
        設置為True 小龜.cfg。在這種情況下,空閒的主循環
        活躍也為客戶端腳本。

        這是絲網類的方法和沒有可用的
        TurtleScreen實例。

        示例(物件名為「螢幕」的實例):

        >>> 螢幕.exitonclick()


''',

'_Screen.getcanvas':
        '''回傳一個 畫布 物件 在這個 TurtleScreen 之上。

        沒有參數。

        示例(物件名為「螢幕」的實例):

        >>> 畫布 = 螢幕.getcanvas()
        >>>畫布
        <小龜.ScrolledCanvas instance at 0x010742D8>

''',

'_Screen.getshapes':
        '''取形狀列表，回傳所有當前可用的龜形狀的名稱列表。

        沒有參數。

        示例(物件名為「螢幕」的實例):

        >>> 螢幕.getshapes()
        ['arrow', 'blank', 'circle', ... , 'turtle']

''',

'_Screen.listen':
        '''聽，設置聚焦於 TurtleScreen 之上(為了收集鍵盤事件)

        沒有參數。
        偽參數是為了提供
        要能夠通過聽取的onclick方法。

        示例(物件名為「螢幕」的實例):

        >>> 螢幕.listen()

''',

'_Screen.mainloop':
        '''進入主迴圈，啟動事件循環 - 呼叫 Tkinter的主迴圈函數。

        沒有參數。

        必須是龜畫圖程式的最後一條語句。
        不得使用於程式是在IDLE 內部 -n 模式(無子程式 )下運行，
        亦即互動模式的龜畫圖程式。

        示例(物件名為「螢幕」的實例):

        >>> 螢幕.mainloop()


''',

'_Screen.mode':
        '''設置龜模式('standard', 'logo' or 'world'),並執行重設。

        可選參數:
        模式 - 在3 個字串('standard', 'logo' or 'world')選一個。

        模式,"標準"是小龜.py兼容。
        模式'標誌'是最標誌 - 龜背顯卡兼容。
        模式'世界'使用用戶自定義"worldcoordinates"。*注意*:在
        這種模式的角度看來,如果x / y的單位比不等於1扭曲。
        如果模式沒有給出,回傳當前的模式。

             模式初始龜標題正角
         ------------ | ------------------------- | ----------- --------
          "標準"向右(東)逆時針
            '標識'向上(北)順時針

        示例:
        >>>模式('logo') # 重設龜頭向北
        >>>模式()
        'logo'

''',

'_Screen.numinput':
        '''彈出一個對話窗口, 可以 輸入 一個數字。

        參數:
        title: 是對話框窗口的標題,
        prompt: 提示語， 主要是描述什麼數字信息輸入文本。
        default: 預設值
        minval: 最小值
        maxval: 最大值

        數字輸入必須在範圍MINVAL .. MAXVAL,如果這些是
        給出。如果沒有,有一絲簽發,對話框將保持打開的校正。回傳數字的輸入。
        如果取消該對話框,回傳None。

        示例(物件名為「螢幕」的實例):

        >>> 螢幕.numinput("撲克","你的賭注:",1000,minval=10, maxval=10000)


''',

'_Screen.onkey':
        '''在按鍵時，連結函數 於 鍵盤鍵鬆開事件。

        參數:
        函數 - 不帶參數的函數
        鍵盤鍵 - 一個字串: 文字鍵(如"a")或 符號鍵(如"空白")

        為了能夠收集鍵盤鍵事件 TurtleScreen
        必須取得聚焦。(參考 聽 函數。)

        示例(物件名為「螢幕」的實例):


        >>> def f():
        ...     fd(50)
        ...     lt(60)
        ...
        >>> 螢幕.onkey(f, 向上鍵)
        >>> 螢幕.listen()

        上面這段程式碼，讓使用者可以重複按向上鍵，
        來畫出一個六邊形。


''',

'_Screen.onkeypress':
        '''在按下鍵時，連結函數 於 單一鍵盤鍵按下事件。如果有指定鍵的話；
        或任何按鍵事件,如果沒有指定鍵的話。

        參數:
        函數 - 不帶參數的函數
        鍵盤鍵 - 一個字串: 文字鍵(如"a")或 符號鍵(如"空白")

        為了能夠收集鍵盤鍵事件 TurtleScreen
        必須取得聚焦。(參考 聽 函數。)

        示例(物件名為「螢幕」的實例):



        >>> def f():
        ...     fd(50)
        ...     lt(60)
        ...
        >>> 螢幕.onkeypress(f, 向上鍵)
        >>> 螢幕.listen()

        上面這段程式碼，讓使用者可以重複按向上鍵，
        來畫出一個六邊形。


''',

'_Screen.onkeyrelease':
        '''在按鍵時，連結函數 於 鍵盤鍵鬆開事件。

        參數:
        函數 - 不帶參數的函數
        鍵盤鍵 - 一個字串: 文字鍵(如"a")或 符號鍵(如"空白")

        為了能夠收集鍵盤鍵事件 TurtleScreen
        必須取得聚焦。(參考 聽 函數。)

        示例(物件名為「螢幕」的實例):


        >>> def f():
        ...     fd(50)
        ...     lt(60)
        ...
        >>> 螢幕.onkeyrelease(f, 向上鍵)
        >>> 螢幕.listen()

        上面這段程式碼，讓使用者可以重複按向上鍵，
        來畫出一個六邊形。


''',

'_Screen.onscreenclick':
        '''在螢幕點擊時，連結函數 於 畫布上的 點擊鼠標的事件。

        參數:
        函數 - 有兩個參數 x , y
               代表滑鼠點擊在畫布上的點坐標。
        鼠鍵號碼 - 預設為1的數，1,2,3分別代表左、中、右

        舉例(名為「螢幕」的 TurtleScreen 的實例)

        >>> 螢幕.onclick(goto)
        >>>#隨後點擊進入TurtleScreen會
        >>>#使龜移動到點擊點。
        >>> 螢幕.onclick(None) # 解除連結

''',

'_Screen.ontimer':
        '''設定計時器, t 毫秒後，就呼叫函數。

        參數:
        函數 - 不帶參數的函數。
        t - 一個數 > = 0

        示例(物件名為「螢幕」的實例):


        >>> 正在執行 = True
        >>> def f():
        ...     if 正在執行:
        ...             fd(50)
        ...             lt(60)
        ...             螢幕.ontimer(f, 250)
        ...
        >>> f()   # makes the turtle marching around
        >>> 正在執行 = False

''',

'_Screen.register_shape':
        '''添加一個龜形狀 TurtleScreen 的 形狀列表。

        參數:
        (1)名稱是一個GIF文件的檔案名而形狀是None。
            安裝相應的圖像形狀。
            ！轉彎時,圖像的形狀不會旋轉,
            ！所以他們不會顯示龜的頭！
        (2)名稱是一個任意的字串和形狀是一個元組(tuple)
            的坐標對子。設定相應的
            多邊形
        (3)名稱是一個任意的字符串,形狀是
            (複合的)Shape 物件。設定相應的
            複合形狀。
        使用形狀,你必須發出 形狀(shapename) 這個指令。

        呼叫:register_shape("小龜.gif")
        - 或者:register_shape("tri",((0,0),(10,10),(-10,10)))

        示例(物件名為「螢幕」的實例):

        >>> 螢幕.register_shape("三角形",((5,-3),(0,5),(-5,-3)))


''',

'_Screen.resetscreen':
        '''重設螢幕上的所有龜為其初始狀態。

        沒有參數。

        示例(物件名為「螢幕」的實例):

        >>> 螢幕.reset()

''',

'_Screen.screensize':
        '''重設畫布大小。

        可選參數:
        canvwidth  - 正整數,畫布以像素為單位的新寬度
        canvheight  - 正整數,畫布以像素為單位的新高度
        bg  -  colorstring或顏色元組,新的backgroundColor
        如果沒有指定參數,回傳目前的值(canvaswidth,canvasheight)

        不要改變繪圖窗口。觀察的隱蔽部位
        在畫布上使用滾動條。(可以使可見的部分
        的圖紙,這是在畫布前外！)

        示例(物件名為「小龜」的實例):

        >>> 小龜.screensize(2000,1500)
        >>>#例如,要尋找一個犯錯而逃脫的龜;-)

''',

'_Screen.setup':
        '''設主視窗的大小和位置。

        參數:
        寬: 若為整數就是以像素為單位，若為浮動數則是在螢幕的百分比。
          預設為值是螢幕的50%。
        高:若為整數就是以像素為單位，若為浮動數則是在螢幕的百分比。
          預設為值是螢幕的75%。
        startx: 如為正數,從左邊螢幕的邊緣開始算位置
          如為負數,從右邊螢幕的邊緣開始算位置
          預設情況下,startx = None 是水平居中。
        starty: 如為正數,從上邊螢幕的邊緣開始算位置
          如為負數,從下邊螢幕的邊緣開始算位置
          預設情況下,starty = None 是垂直居中。

        示例(物件名為「螢幕」的實例):

        >>> 螢幕.setup(width=200, height=200, startx=0, starty=0)

        設主視窗，寬高為 200×200 像素,在螢幕的左上角

        >>> 螢幕.setup(width=.75, height=0.5, startx=None, starty=None)

        設主視窗的寬高為螢幕寬高的75%及50%

''',

'_Screen.setworldcoordinates':
        '''設坐標系，設置一個使用者定義的坐標系。

        參數:
        llx -- 畫布的左下角x坐標
        lly -- 畫布的左下角y坐標
        urx -- 畫布的右上角x坐標
        ury -- 畫布的右上角y坐標

        設置用戶coodinat系統,並在必要時切換到'world'模式。
        這將執行一個螢幕.reset。如果'world'模式已經啟動,
        所有圖都會根據新的坐標系重畫。

        但要注意:在使用者定義的坐標系中，角度可能會出現
        扭曲。(見Screen.mode())

        示例(物件名為「螢幕」的實例):

        >>> 螢幕.setworldcoordinates(-10, -0.5, 50, 1.5)
        >>> for _ in range(36):
        ...     left(10)
        ...     forward(0.5)

''',

'_Screen.textinput':
        '''文字輸入，彈出一個對話窗, 可讓使用者輸入一個字串。

        參數:
        標題：是對話框視窗的標題,
        提示：主要是描述什麼信息輸入文本。
        回傳：輸入字串
        如果取消該對話框, 回傳 None。

        示例(物件名為「螢幕」的實例):

        >>> 螢幕.textinput("NIM","第一個球員的名字:")


''',

'_Screen.title':
        '''標題，設置龜視窗的標題

        參數:
        titlestring  - 一個字串,出現在龜視窗的標題欄


        這是螢幕類的方法。不適用於 TurtleScreen-
        物件。

        示例(物件名為「螢幕」的實例):

        >>> 螢幕.title("歡迎來到龜動物園！")

''',

'_Screen.tracer':
        '''追蹤器，開/關 龜動畫 並設置更新畫面的延遲時間。

        可選參數:
        n - 非負整數
        延遲 - 非負整數

        如果 n 有被指定的,只執行每n次定期螢幕更新。
        (可用於加速複雜圖形的繪製。)
        第二個參數設置延遲值(見 RawTurtle.delay() )

        示例(物件名為「螢幕」的實例):


        >>>螢幕.tracer(8,25)
        >>>距離= 2
        >>>for i in range(200):
        ...     fd(距離)
        ...     rt(90)
        ...     距離 += 2

''',

'_Screen.turtles':
        '''龜列表，回傳螢幕上龜列表。

        示例(物件名為「螢幕」的實例):


        >>> 螢幕.turtles()
        [<turtle.Turtle object at 0x00E11FB0>]

''',

'_Screen.update':
        '''執行 TurtleScreen 更新。

''',

'_Screen.window_height':
        '''視窗高，回傳龜視窗的高度。

        示例(物件名為「螢幕」的實例):


        >>> 螢幕.window_height()
        480

''',

'_Screen.window_width':
        '''視窗寬，回傳龜視窗的寬度。

        示例(物件名為「螢幕」的實例):


        >>> 螢幕.window_width()
        640

'''

}
# ver01, by Renyuan, 2014/03/16 01:49 am