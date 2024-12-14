import discord
from discord.ext import commands
import asyncio
from colorama import Fore, Style
from datetime import datetime, timedelta


# Khởi tạo bot với token
TOKEN = 'MTMxNzQ3MTk2Nzk5NzMzMzU3NQ.G2ulXB.b1iycoFMzxmK0ARJpOoUQct1iYcTPw34PJuoDU'  # Thay bằng token của bot bạn
CHANNEL_ID = 1127474649333256232  # Thay bằng ID kênh bạn muốn gửi tin nhắn

def get_vietnam_time():
    utc_time = datetime.utcnow()
    vietnam_time = utc_time + timedelta(hours=7)
    return vietnam_time.strftime('%Y-%m-%d %H:%M:%S')

def read_last_line(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()  # Đọc tất cả dòng và loại bỏ ký tự xuống dòng
            for line in reversed(lines):
                if line.strip():  # Bỏ qua các dòng trống
                    return line.strip()
        return None  # Nếu file chỉ chứa dòng trống
    except FileNotFoundError:
        print(f"File '{file_path}' không tồn tại.")
        return None

class IPBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(command_prefix='!', intents=intents)
        self.ip_to_send = None
        self.message_sent = asyncio.Event()

    async def setup_hook(self):
        print(f"{Fore.GREEN}Bot đã sẵn sàng!")
        
    async def on_ready(self):
        if self.ip_to_send:
            channel = self.get_channel(CHANNEL_ID)
            if channel:
                try:
                    embed = discord.Embed(
                        title="IP Server Mới:",
                        description=f"```{self.ip_to_send}```",
                        color=discord.Color.green()
                    )
                    embed.set_footer(text=f"Thời gian: {get_vietnam_time()}")
                    await channel.send(embed=embed)
                    print(f"{Fore.GREEN}Đã gửi IP thành công qua Discord!")
                except Exception as e:
                    print(f"{Fore.RED}Lỗi khi gửi IP qua Discord: {e}")
            else:
                print(f"{Fore.RED}Không tìm thấy channel!")
        
        self.message_sent.set()  # Báo hiệu đã xong
        await self.close()  # Đóng bot sau khi gửi xong

async def send_ip_address(ip_address):
    bot = IPBot()
    bot.ip_to_send = ip_address
    
    try:
        await bot.start(TOKEN)
    except Exception as e:
        print(f"{Fore.RED}Lỗi khi khởi động bot: {e}")
    finally:
        if not bot.is_closed():
            await bot.close()
