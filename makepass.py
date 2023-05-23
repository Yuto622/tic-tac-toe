import pandas as pd

# 盤を作成する関数
def make_board():
    board = pd.DataFrame('', index=['0', '1', '2'], columns=['0', '1', '2'])
    return board

# 〇駒を置いて、盤を更新する関数
def place_piece_maru(board):
    i = int(input("行を選択してください（0-2）: "))
    n = int(input("列を選択してください（0-2）: "))
    board.iloc[i, n] = "〇"  
    board.to_csv("renew_board.csv", index=False)  
    
# ×駒を置いて、盤を更新する関数
def place_piece_batu(board):
    i = int(input("行を選択してください（0-2）: "))
    n = int(input("列を選択してください（0-2）: "))
    board.iloc[i, n] = "×"  
    board.to_csv("renew_board.csv", index=False)  

#盤を表示する関数
def display_board(board):
    print(board)

#〇が勝っているか判別する関数
def judge_maru(board):
    if (board.iloc[0, 0] == "〇") and (board.iloc[0, 1] == "〇") and (board.iloc[0, 2] == "〇"):
        return False
    elif (board.iloc[1, 0] == "〇") and (board.iloc[1, 1] == "〇") and (board.iloc[1, 2] == "〇"):
        return False
    elif (board.iloc[2, 0] == "〇") and (board.iloc[2, 1] == "〇") and (board.iloc[2, 2] == "〇"):
        return False

    elif (board.iloc[0, 0] == "〇") and (board.iloc[1, 0] == "〇") and (board.iloc[2, 0] == "〇"):
        return False
    elif (board.iloc[0, 1] == "〇") and (board.iloc[1, 1] == "〇") and (board.iloc[2, 1] == "〇"):
        return False
    elif (board.iloc[0, 2] == "〇") and (board.iloc[1, 2] == "〇") and (board.iloc[2, 2] == "〇"):
        return False

    elif (board.iloc[0, 0] == "〇") and (board.iloc[1, 1] == "〇") and (board.iloc[2, 2] == "〇"):
        return False
    elif (board.iloc[0, 2] == "〇") and (board.iloc[1, 1] == "〇") and (board.iloc[2, 0] == "〇"):
        return False
    
    else:
        return True

#×が勝っているか判別する関数
def judge_batu(board):
    if (board.iloc[0, 0] == "×") and (board.iloc[0, 1] == "×") and (board.iloc[0, 2] == "×"):
        return False
    elif (board.iloc[1, 0] == "×") and (board.iloc[1, 1] == "×") and (board.iloc[1, 2] == "×"):
        return False
    elif (board.iloc[2, 0] == "×") and (board.iloc[2, 1] == "×") and (board.iloc[2, 2] == "×"):
        return False

    elif (board.iloc[0, 0] == "×") and (board.iloc[1, 0] == "×") and (board.iloc[2, 0] == "×"):
        return False
    elif (board.iloc[0, 1] == "×") and (board.iloc[1, 1] == "×") and (board.iloc[2, 1] == "×"):
        return False
    elif (board.iloc[0, 2] == "×") and (board.iloc[1, 2] == "×") and (board.iloc[2, 2] == "×"):
        return False

    elif (board.iloc[0, 0] == "×") and (board.iloc[1, 1] == "×") and (board.iloc[2, 2] == "×"):
        return False
    elif (board.iloc[0, 2] == "×") and (board.iloc[1, 1] == "×") and (board.iloc[2, 0] == "×"):
        return False
    else:
        return True

#関数が置けるか判定する関数
def judge_possible(board,i,n):
    
    if (board.iloc[i, n] == "〇") or (board.iloc[i, n] == "×"):
        return False
    else:
        return True

def main():
    board = make_board()
    print(board)
   
    while True:
        i = int(input("行を選択してください（0-2）: "))
        n = int(input("列を選択してください（0-2）: "))
        
        if judge_possible(board,i,n):
            place_piece_maru(board,i,n)
            display_board(board)
            if judge_maru(board):
                i = int(input("行を選択してください（0-2）: "))
                n = int(input("列を選択してください（0-2）: "))
                
                while not judge_possible(board,i, n):
                    print("そこには置けないので別の場所を指定してください")
                    i = int(input("行を選択してください（0-2）: "))
                    n = int(input("列を選択してください（0-2）: "))

                place_piece_batu(board, i, n)
                display_board(board)

                if not judge_batu(board):
                    print("バツの勝ちです")
                    break
            else:
                print("〇の勝ちです")
                break
        else:
            print("そこには置けないので別の場所を指定してください")

if __name__ == "__main__":
    main()










    

            



    
