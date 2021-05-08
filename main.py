import tkinter as tk
import random
 
global l
global img
global canvas
global nowCard
global nextNum
global label
global next_button

l = []
nextNum = list(range(52))
label = 0
next_button = 0

def createCardList():
  global l
  cards = ["s", "h", "d", "c"]
  numbers = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13"]
  for card in cards:
    for number in numbers:
      l.append(card + number + ".png")

# 次に進むボタンの処理
def nextCard():
  global img
  global nowCard

  # 画像表示
  nowCard = selectCard()
  img = tk.PhotoImage(file="./img/" + nowCard)
  canvas = tk.Canvas(bg="black", width=W_WIDTH, height=W_HEIGHT)
  canvas.place(x=0, y=0)
  canvas.create_image(W_WIDTH/2, W_HEIGHT/2, image=img, anchor=tk.NW)
  createLabel(nowCard)

def selectCard():
  global nextNum
  global l
  tmp_num = random.choice(nextNum)
  del nextNum[::tmp_num]
  return l[tmp_num]

def createLabel(nowName):
  global label
  global next_button

  if label != 0:
    label.destroy()

  if next_button != 0:
    next_button.destroy()

  # 時間計測結果表示ラベル
  label = tk.Label(
      root,
      text=createMenu(nowName),
      width=20,
      font=("", 50, "bold"),
  )
  label.pack(padx=10, pady=10)

  # 次に進むボタン
  next_button = tk.Button(
      root,
      width=30,
      height=10,
      text="NEXT",
      command=nextCard
  )
  next_button.pack(pady=5)

def createMenu(pngName):
  menu = ""
  
  if "s" in pngName:
    menu = "バービー"
  elif "h" in pngName:
    menu = "プッシュアップ"
  elif "d" in pngName:
    menu = "スクワット"
  elif "c" in pngName:
    menu = "腹筋"
  
  if "01" in pngName:
    menu += "10回"
  elif "02" in pngName:
    menu +=  "2回"
  elif "03" in pngName:
    menu +=  "3回"
  elif "04" in pngName:
    menu +=  "4回"
  elif "05" in pngName:
    menu +=  "5回"
  elif "06" in pngName:
    menu +=  "6回"
  elif "07" in pngName:
    menu +=  "7回"
  elif "08" in pngName:
    menu +=  "8回"
  elif "09" in pngName:
    menu +=  "9回"
  elif "10" in pngName:
    menu +=  "10回"
  elif "11" in pngName:
    menu +=  "11回"
  elif "12" in pngName:
    menu +=  "12回"
  elif "13" in pngName:
    menu +=  "13回"

  return menu

# ウィンドウ作成
root = tk.Tk()
root.title("新日式トランプトレーニング")
W_WIDTH=1300
W_HEIGHT=900
root.minsize(W_WIDTH, W_HEIGHT)

createCardList()
nextCard()

root.mainloop()
