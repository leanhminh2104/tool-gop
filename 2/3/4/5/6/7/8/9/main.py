import os
import sys
import subprocess
import platform
from pystyle import Colors, Colorate
from rich.console import Console
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
import time
from time import strftime
import requests
import json
from time import sleep
from datetime import datetime, timedelta
from pystyle import Colors, Colorate
import base64
from time import sleep


# Kiểm tra kết nối mạng
def check_connection():
    try:
        response = requests.get("https://www.google.com.vn", timeout=3)
        if response.status_code != 200:
            raise Exception("Phản hồi không hợp lệ")
        print("Đã kết nối mạng thành công!")
    except (requests.exceptions.ReadTimeout, requests.ConnectionError, requests.exceptions.RequestException, Exception):
        def clear_screen():
            try:
                if platform.system() == "Windows":
                    os.system("cls")
                else:
                    print("\033[2J\033[H", end="")
            except:
                print("\n" * 100)
        
        clear_screen()
        print("Mất kết nối mạng. Vui lòng kiểm tra lại!")
# đánh dấu bản quyền
LAMDev = "[🌸] => "
thanh = "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
###
def get_ip(url):
    try:
        return requests.get(url, timeout=5).text
    except:
        return "Không thể lấy"

ipv4 = get_ip("https://v4.ident.me")
ipv6 = get_ip("https://v6.ident.me")
#ip = requests.get("https://api.ipgeolocation.io/getip").json()
#ip = {'ip': '127.0.0.1'}
sleep=5

# Kiểm tra kết nối mạng
def check_connection():
    try:
        response = requests.get("https://www.google.com.vn", timeout=3)
        if response.status_code != 200:
            raise Exception("Phản hồi không hợp lệ")
        print("Đã kết nối mạng thành công!")
    except (requests.exceptions.ReadTimeout, requests.ConnectionError, requests.exceptions.RequestException, Exception):
        def clear_screen():
            try:
                if platform.system() == "Windows":
                    os.system("cls")
                else:
                    print("\033[2J\033[H", end="")
            except:
                print("\n" * 100)
        
        clear_screen()
        print("Mất kết nối mạng. Vui lòng kiểm tra lại!")
from pystyle import Colorate, Colors
import sys
from time import sleep
banner_text = """\n\n\nĐang vào tool\n\n\n"""
colored_banner = Colorate.Vertical(Colors.white, banner_text)
for char in colored_banner:
    sys.stdout.write(char)
    sys.stdout.flush()
    sleep(0.002)
sleep(4)
def check_connection():
    try:
        response = requests.get("https://www.google.com.vn", timeout=3)
        if response.status_code != 200:
            raise Exception("Phản hồi không hợp lệ")
        print("Đã kết nối mạng thành công!")
    except (requests.exceptions.ReadTimeout, requests.ConnectionError, requests.exceptions.RequestException, Exception):
        def clear_screen():
            try:
                if platform.system() == "Windows":
                    os.system("cls")
                else:
                    print("\033[2J\033[H", end="")
            except:
                print("\n" * 100)
        
        clear_screen()
        print("Mất kết nối mạng. Vui lòng kiểm tra lại!")

import sys
from time import sleep
from pystyle import Colorate, Colors
banner_lines = [
    "\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░██╗░░░░░░█████╗░███╗░░░███╗██████╗░███████╗██╗░░░░░██╗░",
    "░░██║░░░░░██╔══██╗████╗░████║██╔══██╗██╔════╝╚██╗░░░██╔╝░",
    "░░██║░░░░░███████║██╔████╔██║██║░░██║█████╗░░░╚██╗░██╔╝░░",
    "░░██║░░░░░██╔══██║██║╚██╔╝██║██║░░██║██╔══╝░░░░╚████╔╝░░░",
    "░░███████╗██║░░██║██║░╚═╝░██║██████╔╝███████╗░░░╚██╔╝░░░░",
    "░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░╚══════╝░░░░╚═╝░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"
]
colored_banner = "\n".join(Colorate.Diagonal(Colors.rainbow, line) for line in banner_lines)
for char in colored_banner:
    sys.stdout.write(char)
    sys.stdout.flush()
    sleep(0.00000125)
from pystyle import Colorate, Colors
print(Colorate.Diagonal(Colors.rainbow,   "\n\n╔═══════════════════════════════════════════════════════╗"))
print(Colorate.Diagonal(Colors.rainbow,   "║         TOOL GOP VIP BY LAMDev - LEANHMINH            ║"))
print(Colorate.Diagonal(Colors.rainbow,   "╠═══════════════════════════════════════════════════════╣"))
print(Colorate.Diagonal(Colors.rainbow,   "║ TOOL BY: LeAnhMinh - LAMDev          PHIÊN BẢN: 1.0.0 ║"))
print(Colorate.Diagonal(Colors.rainbow,   "║ BOX ZALO SUPPORT: https://zalo.me/g/boiqoq426         ║"))
print(Colorate.Diagonal(Colors.rainbow,   "║ PROFILE ADMIN: https://leanhminh.io.vn                ║"))
print(Colorate.Diagonal(Colors.rainbow,   "║ WEDSITE: https://dichvusale.io.vn                     ║"))
print(Colorate.Diagonal(Colors.rainbow,   "║ GIỚI HẠN THIẾT BỊ: 1 Thiết bị   KEY: LAMDev********** ║"))
print(Colorate.Diagonal(Colors.rainbow,   "╚═══════════════════════════════════════════════════════╝\n"))
print(Colorate.Horizontal(Colors.green_to_red, f"[🌐] => IP V4 CỦA BẠN : {ipv4}"))
print(Colorate.Horizontal(Colors.green_to_red, f"[🌐] => IP V6 CỦA BẠN : {ipv6}\n"))
print (Colorate.Diagonal(Colors.green_to_cyan, thanh + "."))
print (Colorate.Diagonal(Colors.black_to_white, "╔═════════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║  Tool Trao Đổi Sub  ║"))
print (Colorate.Diagonal(Colors.white_to_black, "╚═════════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [1] TDS TIKTOK [V1]"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [2] TDS TIKTOK [V2]"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [3] TDS TIKTOK & TIKTOK NOW"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [4] TDS FACEBOOK FULL JOB [ĐHP]"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [5] TDS INSTAGRAM AOTU PROXY"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [6] TOOL ĐỔI MK TĐS"))
print (Colorate.Diagonal(Colors.green_to_cyan, thanh + "."))
print (Colorate.Diagonal(Colors.black_to_white, "╔═══════════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║  Tool Tương Tác Chéo  ║"))
print (Colorate.Diagonal(Colors.white_to_black, "╚═══════════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [7] TTC TIKTOK [OFF]"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [8] TTC FACEBOOK [ĐHP]"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [9] TOOL TTC PRO5"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [10] TOOL TTC INSTAGRAM"))
print (Colorate.Diagonal(Colors.green_to_cyan, thanh + "."))
print (Colorate.Diagonal(Colors.black_to_white, "╔═════════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║  Tool Spam Sms      ║"))
print (Colorate.Diagonal(Colors.white_to_black, "╚═════════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [11] TOOL SPAM SMS V1"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [11] TOOL SPAM SMS V2"))
print (Colorate.Diagonal(Colors.green_to_cyan, thanh + "."))
print (Colorate.Diagonal(Colors.black_to_white, "╔═════════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║  Tool Đào Mail      ║"))
print (Colorate.Diagonal(Colors.white_to_black,"╚═════════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [13] TOOL ĐÀO MAIL"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [14] TOOL ĐÀO MAIL FULL MAIL"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [15] TOOL CHECK LIVE/DIE"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [16] TOOL CHECK VALID"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [17] TOOL REG ACC GARENA [NEW] "))
print (Colorate.Diagonal(Colors.green_to_cyan, thanh + "."))
print (Colorate.Diagonal(Colors.black_to_white, "╔═════════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║  Tool Facebook      ║"))
print (Colorate.Diagonal(Colors.white_to_black, "╚═════════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [18] TOOL BUFF LIKE "))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [19] KẾT BẠN FACEBOOK GỢI Ý"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [20] SHARE ẢO COOKIE "))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [21] SHARE ẢO TOKEN"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [22] TOOL BUFF VIEW STR"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [23] TOOL NUÔI FACEBOOK"))
print (Colorate.Diagonal(Colors.green_to_cyan, thanh + "."))
print (Colorate.Diagonal(Colors.black_to_white, "╔═════════════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║Tool Đào & Check Proxies ║"))
print (Colorate.Diagonal(Colors.white_to_black, "╚═════════════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [24] TOOL CHECK LIVE/DIE [V1] "))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [25] TOOL CHECK LIVE/DIE [V2 SIÊU VIP]"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [26] TOOL ĐÀO PROXY [V1]"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [27] TOOL ĐÀO PROXY [V2]"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [28] TOOL ĐÀO PROXY [V3]"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [29] TOOL ĐÀO PROXY [V4 SIÊU VIP]"))
print (Colorate.Diagonal(Colors.green_to_cyan, thanh + "."))
print (Colorate.Diagonal(Colors.black_to_white, "╔═════════════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║Tool Spam Messenger      ║"))
print (Colorate.Diagonal(Colors.white_to_black, "╚═════════════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [30] TOOL NHÂY CÓ DẤU  "))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [31] TOOL NHÂY KHÔNG DẤU "))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [32] TOOL NHÂY RÉO TÊN TRONG BOX "))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [33] TOOL NHÂY CODE LAG "))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [34] TOOL TREO SỚ "))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [35] TOOL NHÂY DISCORD"))
print (Colorate.Diagonal(Colors.green_to_cyan, thanh + "."))
print (Colorate.Diagonal(Colors.black_to_white, "╔═════════════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║Tool Encode & Dec        ║"))
print (Colorate.Diagonal(Colors.white_to_black, "╚═════════════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [36] TOOL DEC Hyperion_Deobf"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [37] TOOL DEC Kramer-Specter_Deobf"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [38] TOOL dump_marshal"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [39] TOOL Convert_Marshal-PYC"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [40] TOOL ENCODE MZB"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [41] TOOL ENCODE EMOJI "))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [42] TOOL ENCODE EJULY-DUYKHANH"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [43] TOOL ENCODE BY MEO [VIP]"))
print (Colorate.Diagonal(Colors.green_to_cyan, thanh + "."))
print (Colorate.Diagonal(Colors.black_to_white, "╔═════════════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║Tool Aotu Golike         ║"))
print (Colorate.Diagonal(Colors.white_to_black, "╚═════════════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [44] Tool Auto TikTok"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [45] Tool Auto TikTok [OFF] "))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [46] Tool Auto TikTok Tự Động [OFF] "))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [47] Tool Auto Instagram "))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [48] Tool Auto Twitter"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [49] Tool Auto Youtube [OFF]"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [50] Tool Auto Thread [OFF]"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [51] Tool Auto Linkedin [OFF]"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [52] Tool Auto Shoppe [OFF] "))
print (Colorate.Diagonal(Colors.green_to_cyan, thanh + "."))
print (Colorate.Diagonal(Colors.black_to_white, "╔═════════════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║Tool Của Các Idol Khác   ║"))
print (Colorate.Diagonal(Colors.white_to_black, "╚═════════════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [53] TOOL VLONG ZZ"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [54] TOOL TRỊNH HƯỚNG"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [55] TOOL MEOWMEOW"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [56] TOOL HDT-TOOL"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [57] TOOL LKZ TOOL"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [58] TOOL JIRAY TOOL"))
print (Colorate.Diagonal(Colors.green_to_cyan, thanh + "."))
print (Colorate.Diagonal(Colors.black_to_white, "╔════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║Tool Profile 5  ║"))
print (Colorate.Diagonal(Colors.white_to_black, "╚════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [59] Tool Buff Member Facebook"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [60] Tool Get Cookie Page Thường & Page Pro5"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [61] Tool Chuyển QTV Pro5"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [62] Tool Follow Page Pro5"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [63] TOOL REG PAGR PRO5 + UP AVT | ĐA LUỒNG"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [64] Tool Rút Gọn Link                       "))       
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [65] Get Phản Hồi Từ Link                     "))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [66] Lọc Link Từ File                         "))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [67] TOOL REG ACC FACEBOOK                    "))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [68] TOOL CHUYỂN QUYỀN + CHẤP NHẬN ADMIN PAGE "))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [69] TOOL KÍCH HOẠT PAGE                      "))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [70] TOOL GET TOKEN FB                        "))
print (Colorate.Diagonal(Colors.green_to_cyan, thanh + "."))
print (Colorate.Diagonal(Colors.black_to_white, "╔════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║Tool Tiện ích   ║"))
print (Colorate.Diagonal(Colors.white_to_black, "╚════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [71] TOOL DOSS WEB VIP         "))
print (Colorate.Diagonal(Colors.green_to_red, LAMDev + "Nhập Số [00] Thoát Tool                               "))   
print (Colorate.Diagonal(Colors.green_to_cyan, thanh + "."))
chon = str(input (Colorate.Diagonal(Colors.blue_to_cyan, '[🌸] => Nhập Số : ')))

if chon == '00' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/thoattool/main/.github/workflows/main.yml').text)
if chon == '1' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/TDS-TIKTOK-V1/main/tool.py').text)
if chon == '2':
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Tdstikv2/main/00.py').text)
if chon == '3' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Tik-tiknow/main/1.py').text) 
if chon == '4' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Tds3.12/main/12.py').text) 
elif chon == '5' : 
 exec(requests.get('https://raw.githubusercontent.com/Khanh23047/TDS-IG/main/3.py').text) 
if chon == '6' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Mktds/main/4.py').text)
if chon == '7' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/thoattool/main/.github/workflows/main.yml').text)
elif chon == '8' :
 exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Ttcfb312/main/ttcfb312.py').text)
elif chon == '9' :
 exec(requests.get('https://raw.githubusercontent.com/Khanh23047/TTCPR5/main/5.py').text)
if chon == '10' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/TTC-IG/main/6.py').text)
if chon == '11' :
    exec(requests.get(' https://raw.githubusercontent.com/Khanh23047/Spamsmsv1/main/sms.py').text)
if chon == '12' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Spamsmsv2/main/smsv2.py').text)
if chon == '13' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Daomail/main/8.py').text)
if chon == '14' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Full-mail/main/vietcode_toolmeow.py').text)
if chon == '15' :
    exec(requests.get(' https://raw.githubusercontent.com/Khanh23047/Checklivedie/main/p.py').text)
if chon == '16' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/checkvali/main/10.py').text)
if chon == '17' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Reggrn/main/Reggrn').text)
if chon == '18' :
  exec(requests.get('https://raw.githubusercontent.com/Khanh23047/LIKE-FACEBOOK-/main/p.py').text)
if chon == '19' :   
   exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Ketbangoiy/main/p.py').text)
if chon == '20' :  
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Shareaocookie/main/share.py').text)
if chon == '21' :
    exec(requests.get(' https://raw.githubusercontent.com/Khanh23047/Shareaotoken/main/shareao.py').text)
if chon == '22' :
     exec(requests.get(' https://raw.githubusercontent.com/Khanh23047/Viewpr5/main/p.py').text)
if chon == '23' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Nuoi-fb/main/10.py').text)
if chon == '24' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Checklivedieproxy/main/p.py').text)
if chon == '25' :
	exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Checklivediev2/main/p.py').text)
if chon == '26' :
  exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Daoprxv2/main/p.py').text)
if chon == '27' :   
   exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Daoproxyv3/main/p.py').text)
if chon == '28' :  
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Daoproxyv4/main/p.py').text)
if chon == '29' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Daoproxyv4vip/main/p.py').text)
if chon == '30' :
     exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Nh-y-c-d-u/main/p.py').text)
if chon == '31' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Nhaykodau/main/p.py').text)
if chon == '32' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Reotentrongbox/main/p.py').text)
if chon == '33' :
	exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Nhaycodelag/main/p.py').text)
if chon == '34' :
  exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Treoso/main/p.py').text)
if chon == '35' :   
   exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Nhaydis/main/p.py').text)
if chon == '36' :  
    exec(requests.get('https://raw.githubusercontent.com/KhanhNguyen9872/hyperion_deobfuscate/main/hyperion_deobf.py').text)
if chon == '37' :
    exec(requests.get('https://raw.githubusercontent.com/KhanhNguyen9872/kramer-specter_deobf/main/kramer-specter-deobf.py').text)
if chon == '38' :
     exec(requests.get('https://raw.githubusercontent.com/KhanhNguyen9872/dump_marshal_py/main/dump_marshal.py').text)
if chon == '39' :
    exec(requests.get('https://raw.githubusercontent.com/KhanhNguyen9872/Convert_Marshal-PYC/main/cv_marshal_pyc.py').text)
if chon == '40' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Encode-MZB/main/en.py').text)
if chon == '41' :
	exec(requests.get(' https://raw.githubusercontent.com/Khanh23047/Encode-Emoji-/main/p.py').text)
if chon == '42' :
  exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Encode-ejuly-DUYKHANH/main/encode.py').text)
if chon == '43' :   
   exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Encode-MEO/refs/heads/main/meo.py').text)
if chon == '44' :  
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Golike/main/golike.py').text)
if chon == '45' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/thoattool/main/.github/workflows/main.yml').text)
if chon == '46' :
     exec(requests.get('https://raw.githubusercontent.com/Khanh23047/thoattool/main/.github/workflows/main.yml').text)
if chon == '47' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Golike-ig/main/p.py').text)
if chon == '48' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Golike-Twitter-/main/p.py').text)
if chon == '49' :
	exec(requests.get('https://raw.githubusercontent.com/Khanh23047/thoattool/main/.github/workflows/main.yml').text)
if chon == '50' :
  exec(requests.get('https://raw.githubusercontent.com/Khanh23047/thoattool/main/.github/workflows/main.yml').text)
if chon == '51' :   
   exec(requests.get('https://raw.githubusercontent.com/Khanh23047/thoattool/main/.github/workflows/main.yml').text)
if chon == '52' :  
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/thoattool/main/.github/workflows/main.yml').text)
if chon == '53' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Tool-vlong/main/p.py').text)
if chon == '54' :
     exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Tool-trinh-huong/main/huong.py').text)
if chon == '55' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Full-mail/main/vietcode_toolmeow.py').text)
if chon == '56' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Tool-hdt/main/p.py').text)
if chon == '57' :
	exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Tool-lkz/main/p.py').text)
if chon == '58' :
	exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Tool-jray/main/haha.py').text)
if chon == '59' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Buff-mem-FB/main/10.py').text)
if chon == '60' :
     exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Getcookie-pro5/main/10.py').text)
if chon == '61' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Buff-member-fb/main/10.py').text)
if chon == '62' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Buff-member-fb/main/10.py').text)
if chon == '63' :
	exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Reg-pro5-vip/main/reg.py').text)
if chon == '64' :
	exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Rutgonlink/main/10.py').text)
if chon == '65' :
	exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Phanhoilink/main/10.py').text)
if chon == '66' :
	exec(requests.get('https://raw.githubusercontent.com/Khanh23047/L-c-Link-T-File/main/10.py').text)
if chon == '67' :
	exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Reg-fb/main/10.py').text)
if chon == '68' :
	exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Chuyenquyen-chapnhan/main/10.py').text)
if chon == '69' :
	exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Kichhoatpage/main/10.py').text)
if chon == '70' :
	exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Get-token/main/10.py').text)
if chon == '71' :
	exec(requests.get('https://raw.githubusercontent.com/Khanh23047/DOSS-WEB/main/dos.py').text)
else :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/thoattool/main/.github/workflows/main.yml').text)
