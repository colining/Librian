import os
import json
from pathlib import Path
import shutil
from .環境 import 配置

from .Librian虛擬機 import 虛擬機環境
from .Librian虛擬機 import 讀者

此處 = os.path.dirname(os.path.abspath(__file__))


def 演出固化(劇本文件):
    讀者實例 = 讀者.讀者(劇本文件)
    演出步 = list(讀者實例.迭代器())
    return 演出步


def 虛擬核心():
    圖片文件夾 = os.path.join(f'../../{虛擬機環境.工程路徑}', 虛擬機環境.圖片文件夾).replace('\\', '/')
    音樂文件夾 = os.path.join(f'../../{虛擬機環境.工程路徑}', 虛擬機環境.音樂文件夾).replace('\\', '/')
    視頻文件夾 = os.path.join(f'../../{虛擬機環境.工程路徑}', 虛擬機環境.視頻文件夾).replace('\\', '/')
    臨時立繪文件夾 = os.path.join(f'../../{虛擬機環境.工程路徑}', 虛擬機環境.臨時立繪文件夾).replace('\\', '/')
    自定css = [os.path.join(f'../../{虛擬機環境.工程路徑}', i).replace('\\', '/') for i in 虛擬機環境.自定css]

    主題css = os.path.join(f'主題', 虛擬機環境.主題css + '.css').replace('\\', '/')

    演出步 = 演出固化(f'{虛擬機環境.工程路徑}/{虛擬機環境.劇本入口}')

    虛擬核心 = {
        '作品名': 虛擬機環境.標題,
        '解析度': 虛擬機環境.主解析度,
        '邊界': int(配置["顯示繪圖邊界"]),
        '圖片文件夾': 圖片文件夾,
        '音樂文件夾': 音樂文件夾,
        '視頻文件夾': 視頻文件夾,
        '臨時立繪文件夾': 臨時立繪文件夾,
        '自定css': 自定css,
        '主題css': 主題css,
        '演出步': 演出步
    }
    json數據 = json.dumps(虛擬核心, indent=2, ensure_ascii=False)
    return f'window.虛擬核心 = {json數據}'


def 幻象化(目標路徑):
    目標路徑 = Path(目標路徑)
    依賴 = [
        '黑科技',
        'Librian本體/前端/dist',
        'Librian本體/前端/素材',
        'Librian本體/前端/主題',
        'Librian本體/前端/adv.html',
        f'{虛擬機環境.工程路徑}',
    ]
    for i in 依賴:
        源路徑 = Path(此處) / '..' / i
        if 源路徑.is_dir():
            shutil.copytree(源路徑, 目標路徑 / i)
        elif 源路徑.is_file():
            shutil.copy(源路徑, 目標路徑 / i)
        else:
            raise Exception('哈？')

    with open(目標路徑 / 'Librian本體/前端/虛擬核心.js', 'w', encoding='utf-8') as f:
        f.write(虛擬核心())

