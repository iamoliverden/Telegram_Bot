# main.py
from extensions import CurrencyConverter, APIException
import telebot
from config import TELEGRAM_BOT_TOKEN

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Welcome! Use /help for instructions.")


@bot.message_handler(commands=['help'])
def handle_help(message: telebot.types.Message):
    instructions = (
            "To get the price of a currency, use the following format:\n"
            "<currency_to_check> <currency_to_convert_to> <amount>\n"
            "Example: USD EUR 100\n"
            "Use /values to see the list of available currencies."
        )
    bot.send_message(message.chat.id, instructions)


@bot.message_handler(commands=['values'])
def handle_values(message: telebot.types.Message):
    available_currencies = ("Available currencies include:\n- USD (US Dollar)\n- EUR (Euro)\n- CAD (Canadian Dollar)"
                            "\n- INR (Indian Rupee)\n- BDT (Bangladeshi Taka)\n More currecies are available. Check currency ISO: https://www.worlddata.info/currencies/")
    bot.send_message(message.chat.id, available_currencies)

@bot.message_handler(func=lambda message: True)
def handle_currency_conversion(message):
    try:
        input_params = message.text.split()
        if len(input_params) != 3:
            raise APIException("Invalid command. Use /help for instructions.")

        base_currency, quote_currency, amount = input_params
        amount = float(amount)

        result = CurrencyConverter.get_price(base_currency, quote_currency, amount)
        bot.send_message(message.chat.id, f"{amount} {base_currency} is equal to {result:.2f} {quote_currency}")

    except APIException as e:
        bot.send_message(message.chat.id, f"Error: {str(e)}. Check the correct spelling of the currency ISO. Use /help for instructions.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Unexpected error: {str(e)}. Use only the suggested entry format: USD EUR 100")


if __name__ == "__main__":
    bot.polling(none_stop=True)
