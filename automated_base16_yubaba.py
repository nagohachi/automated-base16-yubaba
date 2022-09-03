import os
import time
from math import isnan
import csv
import pandas as pd

class AutomatedBase16Yubaba:
    def __init__(self, input_file_name="aburaya_data.csv") -> None:
        self.columns = ["old_name", "new_name"]
        if not os.path.isfile(input_file_name):
            with open(input_file_name, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(self.columns)
        self._aburaya_data = pd.read_csv(input_file_name, encoding="cp932")

    def explain_operation(self) -> None:
        print("\n湯婆婆: お前の名前をターミナルから標準入力でお入れ。入れ終わったら Enter をお押し\n")

    def get_next_name(self) -> int:
        if isnan(self._aburaya_data["new_name"].max()):
            return 0
        return self._aburaya_data["new_name"].max() + 1
    
    def point_out_extravagant_name(self, new_name, old_name) -> None:
        print("湯婆婆: {0}というのかい？贅沢な名だね。\n湯婆婆: 今からお前の名は{1}だ。いいかい、{1}だよ。\n湯婆婆: 分かったら返事をするんだ、{1}！".format(old_name, hex(new_name)))

    def is_old_name_valid(self, old_name) -> bool:
        space_deleted_name = old_name.replace(" ", "").replace("　", "").replace("\t", "")
        if not space_deleted_name:
            print("ちゃんと名前をお入れ！")
            return False
        return True
    
    def rename(self, old_name, input_file_name="aburaya_data.csv") -> None:
        new_name = self.get_next_name()
        self.point_out_extravagant_name(new_name, old_name)
        new_clerk = pd.DataFrame({
            "old_name": [old_name],
            "new_name": [new_name],
        })
        self._aburaya_data = pd.concat([self._aburaya_data, new_clerk], ignore_index=True)
        self._aburaya_data.to_csv(input_file_name, index=False, encoding="cp932")
        print("\n湯婆婆: 次の方～")

def main() -> None:
    yubaba = AutomatedBase16Yubaba()
    yubaba.explain_operation()
    while True:
        old_name = input("あなた: ")
        if not yubaba.is_old_name_valid(old_name):
            continue
        yubaba.rename(old_name)
        time.sleep(0.2)

if __name__ == "__main__":
    main()