import discord
from discord.ext import commands
import asyncio
from colorama import Fore, Style
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()

# Đọc token từ biến môi trường
TOKEN = os.getenv('DISCORD_TOKEN')

# Thêm các CHANNEL_ID mới
CHANNELS = {
    "Server Test": 1317155833964134451,
    "Server Chính": 1127474649333256232
}

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
        self.image_to_send = None
        self.message_with_image = None
        self.target_channels = []
        self.reset_schedule = None  # Thêm biến cho lịch reset

    async def setup_hook(self):
        print(f"{Fore.GREEN}Bot đã sẵn sàng!")
        
    async def on_ready(self):
        try:
            if self.ip_to_send:
                await self.send_ip()
            elif self.image_to_send:
                await self.send_image_message()
            elif self.reset_schedule:
                await self.send_reset_timeline()
            
            self.message_sent.set()
        except Exception as e:
            print(f"{Fore.RED}Lỗi trong on_ready: {e}")
        finally:
            await self.close()

    async def send_reset_timeline(self):
        off_time, on_time = self.reset_schedule
        embed = discord.Embed(
            title="PALWORLD SERVER RESET TIMELINE",
            color=discord.Color.blue()
        )
        
        embed.add_field(
            name="OFF-TIME",
            value=f"```diff\n- {off_time}```",
            inline=False
        )
        embed.add_field(
            name="ON-TIME",
            value=f"```diff\n+ {on_time}```",
            inline=False
        )
        
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1127474649333256232/1197549193501507726/palworld-logo.png")
        embed.set_footer(text=f"Cập nhật lúc: {get_vietnam_time()}")
        
        for channel_id in CHANNELS.values():
            try:
                channel = self.get_channel(channel_id)
                if channel:
                    await channel.send(embed=embed)
                    print(f"{Fore.GREEN}Đã gửi lịch reset server tới {channel.guild.name} - {channel.name}!")
                else:
                    print(f"{Fore.RED}Không tìm thấy channel {channel_id}")
            except Exception as e:
                print(f"{Fore.RED}Lỗi khi gửi tới channel {channel_id}: {e}")

    async def send_image_message(self):
        """Phương thức gửi hình ảnh kèm tin nhắn"""
        if not os.path.exists(self.image_to_send):
            print(f"{Fore.RED}Không tìm thấy file ảnh!")
            return

        embed = discord.Embed(
            description=self.message_with_image if self.message_with_image else None,
            color=discord.Color.blue()
        )
        embed.set_author(name="Thông báo từ Admin")
        embed.set_footer(text=f"Thời gian: {get_vietnam_time()}")
        
        for channel_id in self.target_channels:
            try:
                channel = self.get_channel(channel_id)
                if channel:
                    with open(self.image_to_send, 'rb') as f:
                        file = discord.File(f, filename="image.png")
                        embed.set_image(url="attachment://image.png")
                        await channel.send(file=file, embed=embed)
                    print(f"{Fore.GREEN}Đã gửi hình ảnh thành công tới {channel.guild.name} - {channel.name}!")
                    # Thêm delay nhỏ giữa các lần gửi
                    await asyncio.sleep(1)
                else:
                    print(f"{Fore.RED}Không tìm thấy channel {channel_id}")
            except Exception as e:
                print(f"{Fore.RED}Lỗi khi gửi tới channel {channel_id}: {e}")

    async def send_ip(self):
        """Phương thức gửi IP server"""
        for channel_id in CHANNELS.values():
            try:
                channel = self.get_channel(channel_id)
                if channel:
                    embed = discord.Embed(
                        title="IP Server Mới:",
                        description=f"```{self.ip_to_send}```",
                        color=discord.Color.green()
                    )
                    embed.set_footer(text=f"Thời gian: {get_vietnam_time()}")
                    await channel.send(embed=embed)
                    print(f"{Fore.GREEN}Đã gửi IP thành công tới {channel.guild.name} - {channel.name}!")
                    await asyncio.sleep(1)
                else:
                    print(f"{Fore.RED}Không tìm thấy channel {channel_id}")
            except Exception as e:
                print(f"{Fore.RED}Lỗi khi gửi tới channel {channel_id}: {e}")

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

async def send_image(image_path, message=None, target_channels=None):
    """Gửi hình ảnh kèm tin nhắn tới các kênh được chọn"""
    bot = IPBot()
    bot.image_to_send = image_path
    bot.message_with_image = message
    bot.target_channels = target_channels or list(CHANNELS.values())
    
    try:
        await bot.start(TOKEN)
    except Exception as e:
        print(f"{Fore.RED}Lỗi khi khởi động bot: {e}")
    finally:
        if not bot.is_closed():
            await bot.close()

def choose_channels():
    """Cho phép người dùng chọn kênh để gửi tin nhắn"""
    print(f"\n{Fore.CYAN}Chọn kênh để gửi tin nhắn:")
    for idx, (name, channel_id) in enumerate(CHANNELS.items(), 1):
        print(f"{idx}. {name} ({channel_id})")
    print("3. Gửi tới cả hai kênh")
    
    while True:
        choice = input(f"\n{Fore.YELLOW}Nhập lựa chọn (1/2/3): {Style.RESET_ALL}")
        if choice == "1":
            return [list(CHANNELS.values())[0]]
        elif choice == "2":
            return [list(CHANNELS.values())[1]]
        elif choice == "3":
            return list(CHANNELS.values())
        else:
            print(f"{Fore.RED}Lựa chọn không hợp lệ!")

async def send_reset_schedule(off_time="22:30", on_time="22:50"):
    """Gửi thông báo lịch reset server"""
    bot = IPBot()
    bot.reset_schedule = (off_time, on_time)
    bot.message_sent = asyncio.Event()
    
    try:
        await bot.start(TOKEN)
        await bot.message_sent.wait()
    except Exception as e:
        print(f"{Fore.RED}Lỗi khi gửi thông báo reset schedule: {e}")
    finally:
        if not bot.is_closed():
            await bot.close()
