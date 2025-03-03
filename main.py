import os
import time
import random
import asyncio
import platform
from datetime import datetime
from rich.console import Console
from rich.progress import Progress

os_type = platform.system()

console = Console()

class Logger:
    def __init__(self, colors: list = [], random_color: bool = False, bold: bool = True, 
                 emoji: dict = None, emoji_exist: bool = True, 
                 time_log: bool = True, msg_default_logger: bool = True):
        self.colors = colors
        self.random_color = random_color
        self.bold = bold
        self.emoji = emoji or {}
        self.emoji_exist = emoji_exist
        self.time_log = time_log
        self.msg_default_logger = msg_default_logger
        if os_type == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def get_emoji(self, emoji_status: int) -> str:
        if emoji_status in self.emoji:
            emoji_list = self.emoji[emoji_status].split("\n")
            return random.choice(emoji_list).replace(" ", "")
        return ""

    async def display_time(self, target_time: str):
        """
        Асинхронный таймер, который увеличивается от 00:00:00 до заданного времени.

        :param target_time: Целевое время в формате "HH:MM:SS".
        """
        target_h, target_m, target_s = map(int, target_time.split(":"))
        h, m, s = 0, 0, 0

        while True:
            formatted_time = f"{h:02}:{m:02}:{s:02}"
            print(formatted_time)

            if h == target_h and m == target_m and s == target_s:
                break

            await asyncio.sleep(1)

            s += 1
            if s == 60:
                s = 0
                m += 1
                if m == 60:
                    m = 0
                    h += 1

            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")

    def perfect_log(self, log: str, status: str):
        if self.emoji_exist:
            emoji = self.get_emoji(1 if status == "success" else 2 if status == "failed" else 3)
        else:
            emoji = ""
        log_alert = ""
        if status == "success" and self.msg_default_logger:
            style = "bold green"
            if self.time_log:
                log_alert = "[INFO"
            else:
                log_alert = "[INFO]"
        elif status == "failed" and self.msg_default_logger:
            style = "bold red"
            if self.time_log:
                log_alert = "[ERROR"
            else:
                log_alert = "[ERROR]"
        elif status == "warning" and self.msg_default_logger:
            style = "bold yellow"
            if self.time_log:
                log_alert = "[WARNING"
            else:
                log_alert = "[WARNING]"
        else:
            style = "bold white"
            if self.time_log:
                log_alert = "[UNKNOWN"
            else:
                log_alert = "[UNKNOWN]"

        if self.time_log:
            current_dateTime = datetime.now()
            time_str = current_dateTime.strftime("%H:%M:%S")
            log_message = f"{log_alert}|[{style}]{time_str}] {log}{emoji}"
            console.print(log_message, style=style)
            return
        log_message = f"{log_alert} {log}{emoji}"
        console.print(log_message, style=style)
        return

    @staticmethod
    def wait_progress(time_to_step: float = 0.2, advance: float = 0.5, color: str = "red", text: str = "", total: int = 1000, finish_msg: str = ""):
        with Progress() as progress:
            task1 = progress.add_task(f"[{color}]{text}...", total=total)
            while not progress.finished:
                progress.update(task1, advance=advance)
                time.sleep(time_to_step)
        console.print("best coder!", style="bold green")
        return ""

async def main():
    logger = Logger(emoji={1: "✅\n✔️\n☑️\n🆗\n💡\n⚡\n✨\n😎\n💯\n❤️\n🥋",
    2: "⚠️\n🛑\n🚧\n☢️",3: "☠️\n🛠️\n🔧\n⚙️\n📛\n🔴\n🚩\n🔺\n🆘\n🚨"},emoji_exist=True)
    while True:
        logger.perfect_log("Starting app", "success")
        await asyncio.sleep(2)
        logger.perfect_log("Loading data", "failed")
        await asyncio.sleep(2)
        logger.perfect_log("Processing", "warning")
        await asyncio.sleep(2)
        logger.perfect_log("Unknown status", "unknown")
        await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(main())
