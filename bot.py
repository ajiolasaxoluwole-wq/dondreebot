import os
import logging
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, ConversationHandler, MessageHandler, filters

# IMPORTANT: Import everything from handlers properly
import handlers
from handlers import BotHandlers

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    """Start the bot"""
    token = os.getenv('BOT_TOKEN')
    if not token:
        logger.error("No BOT_TOKEN found in .env file!")
        return
    
    application = Application.builder().token(token).build()
    
    # Initialize handlers
    bot_handlers = BotHandlers()
    
    # Add conversation handlers with proper state references
    conv_handlers = [
        # Calculator
        ConversationHandler(
            entry_points=[CommandHandler('calc', bot_handlers.calc_start)],
            states={
                handlers.WAITING_FOR_INPUT: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot_handlers.calc_input)]
            },
            fallbacks=[CommandHandler('cancel', bot_handlers.cancel)]
        ),
        # Percentage
        ConversationHandler(
            entry_points=[CommandHandler('percentage', bot_handlers.percentage_start)],
            states={
                handlers.WAITING_FOR_PERCENTAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot_handlers.percentage_input)]
            },
            fallbacks=[CommandHandler('cancel', bot_handlers.cancel)]
        ),
        # Fraction
        ConversationHandler(
            entry_points=[CommandHandler('fraction', bot_handlers.fraction_start)],
            states={
                handlers.WAITING_FOR_FRACTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot_handlers.fraction_input)]
            },
            fallbacks=[CommandHandler('cancel', bot_handlers.cancel)]
        ),
        # Average
        ConversationHandler(
            entry_points=[CommandHandler('average', bot_handlers.average_start)],
            states={
                handlers.WAITING_FOR_AVERAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot_handlers.average_input)]
            },
            fallbacks=[CommandHandler('cancel', bot_handlers.cancel)]
        ),
        # Discount
        ConversationHandler(
            entry_points=[CommandHandler('discount', bot_handlers.discount_start)],
            states={
                handlers.WAITING_FOR_DISCOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot_handlers.discount_input)]
            },
            fallbacks=[CommandHandler('cancel', bot_handlers.cancel)]
        ),
        # Age
        ConversationHandler(
            entry_points=[CommandHandler('age', bot_handlers.age_start)],
            states={
                handlers.WAITING_FOR_AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot_handlers.age_input)]
            },
            fallbacks=[CommandHandler('cancel', bot_handlers.cancel)]
        ),
        # Date
        ConversationHandler(
            entry_points=[CommandHandler('date', bot_handlers.date_start)],
            states={
                handlers.WAITING_FOR_DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot_handlers.date_input)]
            },
            fallbacks=[CommandHandler('cancel', bot_handlers.cancel)]
        ),
        # Length
        ConversationHandler(
            entry_points=[CommandHandler('length', bot_handlers.length_start)],
            states={
                handlers.WAITING_FOR_LENGTH: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot_handlers.length_input)]
            },
            fallbacks=[CommandHandler('cancel', bot_handlers.cancel)]
        ),
        # Weight
        ConversationHandler(
            entry_points=[CommandHandler('weight', bot_handlers.weight_start)],
            states={
                handlers.WAITING_FOR_WEIGHT: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot_handlers.weight_input)]
            },
            fallbacks=[CommandHandler('cancel', bot_handlers.cancel)]
        ),
        # Temperature
        ConversationHandler(
            entry_points=[CommandHandler('temp', bot_handlers.temp_start)],
            states={
                handlers.WAITING_FOR_TEMPERATURE: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot_handlers.temp_input)]
            },
            fallbacks=[CommandHandler('cancel', bot_handlers.cancel)]
        ),
    ]
    
    # Add all conversation handlers
    for handler in conv_handlers:
        application.add_handler(handler)
    
    # Add basic command handlers
    application.add_handler(CommandHandler('start', bot_handlers.start))
    application.add_handler(CommandHandler('help', bot_handlers.help_command))
    
    # Add error handler
    application.add_error_handler(bot_handlers.error_handler)
    
    # Start the bot
    logger.info("Bot is starting...")
    application.run_polling(allowed_updates=[])

if __name__ == '__main__':
    main()
