import os
import logging
from dotenv import load_dotenv
from telegram.ext import (
    Application,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

from handlers import BotHandlers, (
    WAITING_FOR_INPUT,
    WAITING_FOR_FRACTION,
    WAITING_FOR_PERCENTAGE,
    WAITING_FOR_DISCOUNT,
    WAITING_FOR_AGE,
    WAITING_FOR_DATE,
    WAITING_FOR_LENGTH,
    WAITING_FOR_WEIGHT,
    WAITING_FOR_TEMPERATURE,
    WAITING_FOR_AVERAGE,
)

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
    # Get token from environment
    token = os.getenv('BOT_TOKEN')
    if not token:
        logger.error("No BOT_TOKEN found in .env file!")
        return
    
    # Create application
    application = Application.builder().token(token).build()
    
    # Initialize handlers
    handlers = BotHandlers()
    
    # Add conversation handlers
    conv_handlers = [
        # Calculator
        ConversationHandler(
            entry_points=[CommandHandler('calc', handlers.calc_start)],
            states={
                WAITING_FOR_INPUT: [MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.calc_input)]
            },
            fallbacks=[CommandHandler('cancel', handlers.cancel)]
        ),
        # Percentage
        ConversationHandler(
            entry_points=[CommandHandler('percentage', handlers.percentage_start)],
            states={
                WAITING_FOR_PERCENTAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.percentage_input)]
            },
            fallbacks=[CommandHandler('cancel', handlers.cancel)]
        ),
        # Fraction
        ConversationHandler(
            entry_points=[CommandHandler('fraction', handlers.fraction_start)],
            states={
                WAITING_FOR_FRACTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.fraction_input)]
            },
            fallbacks=[CommandHandler('cancel', handlers.cancel)]
        ),
        # Average
        ConversationHandler(
            entry_points=[CommandHandler('average', handlers.average_start)],
            states={
                WAITING_FOR_AVERAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.average_input)]
            },
            fallbacks=[CommandHandler('cancel', handlers.cancel)]
        ),
        # Discount
        ConversationHandler(
            entry_points=[CommandHandler('discount', handlers.discount_start)],
            states={
                WAITING_FOR_DISCOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.discount_input)]
            },
            fallbacks=[CommandHandler('cancel', handlers.cancel)]
        ),
        # Age
        ConversationHandler(
            entry_points=[CommandHandler('age', handlers.age_start)],
            states={
                WAITING_FOR_AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.age_input)]
            },
            fallbacks=[CommandHandler('cancel', handlers.cancel)]
        ),
        # Date
        ConversationHandler(
            entry_points=[CommandHandler('date', handlers.date_start)],
            states={
                WAITING_FOR_DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.date_input)]
            },
            fallbacks=[CommandHandler('cancel', handlers.cancel)]
        ),
        # Length
        ConversationHandler(
            entry_points=[CommandHandler('length', handlers.length_start)],
            states={
                WAITING_FOR_LENGTH: [MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.length_input)]
            },
            fallbacks=[CommandHandler('cancel', handlers.cancel)]
        ),
        # Weight
        ConversationHandler(
            entry_points=[CommandHandler('weight', handlers.weight_start)],
            states={
                WAITING_FOR_WEIGHT: [MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.weight_input)]
            },
            fallbacks=[CommandHandler('cancel', handlers.cancel)]
        ),
        # Temperature
        ConversationHandler(
            entry_points=[CommandHandler('temp', handlers.temp_start)],
            states={
                WAITING_FOR_TEMPERATURE: [MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.temp_input)]
            },
            fallbacks=[CommandHandler('cancel', handlers.cancel)]
        ),
    ]
    
    # Add all conversation handlers
    for handler in conv_handlers:
        application.add_handler(handler)
    
    # Add basic command handlers
    application.add_handler(CommandHandler('start', handlers.start))
    application.add_handler(CommandHandler('help', handlers.help_command))
    
    # Add error handler
    application.add_error_handler(handlers.error_handler)
    
    # Start the bot
    logger.info("Bot is starting...")
    application.run_polling(allowed_updates=[])

if __name__ == '__main__':
    main()
