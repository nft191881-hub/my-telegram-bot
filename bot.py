import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# 替换为你的 BotFather 申请到的 Token
BOT_TOKEN = "8795865633:AAGpCgeCEWjXsfzKC78qGX-kF0ZStM47NM0"

# 替换为你的 Mini App 网页地址（前端 H5 页面链接）
WEB_APP_URL = "https://your-mini-app-domain.com"

# 初始化 Bot 和 Dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username or "未知用户"
    
    # 欢迎文本（模拟你截图中的样式）
    welcome_text = (
        f"🏆 **欢迎来到 TG 商城/钱包**\n\n"
        f"👤 昵称：{username}\n"
        f"🆔 ID：`{user_id}`\n\n"
        f"汇聚全球热门商品与优质服务，打造一站式数字资产消费生态。"
    )
    
    # 创建内联键盘按钮
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🛍️ 打开 TG 商城", 
                    web_app=WebAppInfo(url=WEB_APP_URL)
                )
            ],
            [
                InlineKeyboardButton(text="💰 充值提现", callback_data="wallet_deposit"),
                InlineKeyboardButton(text="👥 个人中心", callback_data="user_profile")
            ]
        ]
    )
    
    await message.answer(welcome_text, reply_markup=keyboard, parse_mode="Markdown")

@dp.message(F.text == "充值提现") # 或者通过回调按钮触发
@dp.callback_query(F.data == "wallet_deposit")
async def process_deposit(event):
    # 兼容消息和回调查询的简易处理
    message = event.message if hasattr(event, "message") else event
    user_id = event.from_user.id
    
    # 模拟生成的 TRC20 充值地址（实际开发中可以为每个用户绑定独立或公共充值地址）
    mock_address = "TKcaDrspJJ56eiothSSHXVZBTQMXmrvt4"
    
    deposit_text = (
        f"💳 **钱包网络：** TRC20\n"
        f"📍 **充值地址：**\n`{mock_address}`\n\n"
        f"*(点击上方地址可直接复制)*\n"
        f"⚠️ 请向以上地址充值 USDT 或 TRX，系统会自动到账。"
    )
    
    if hasattr(event, "message"):
        await message.answer(deposit_text, parse_mode="Markdown")
        await event.answer()
    else:
        await message.answer(deposit_text, parse_mode="Markdown")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("机器人正在启动...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
