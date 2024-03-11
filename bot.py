import telebot
import scraping



TOKEN = "6199806449:AAFqHu25WaeLwZEznQyvjT52fAJSnEKdJ3E"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start_command(m):   
    scraping.start_scraping()
    bot.reply_to(m, f"""
        Bienvendido a Bolivares Bot
        Dolar BCV: {scraping.precios["Dolar BCV"]}
        Dolar Paralelo: {scraping.precios["Dolar Paralelo"]}
        Dolar Binance: {scraping.precios["Dolar Binance"]}
        Dolar Web:  {scraping.precios["Dolar Web"]}
        Dolar Today: {scraping.precios["Dolar Today"]}
        Dolar Paralelo VIP: {scraping.precios["Dolar Paralelo VIP"]}
    """)


bot.polling(timeout=120)  # Aumenta el tiempo de espera a 60 segundos
