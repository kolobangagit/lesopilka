from aiohttp import web

from django.core.management.base import BaseCommand
from aiogram import Bot, Dispatcher, Router, types
from apps.lesopilka_bot.bot import BASE_WEBHOOK_URL, WEBHOOK_PATH, WEB_SERVER_HOST, WEB_SERVER_PORT, on_startup, dp
from aiogram.enums import ParseMode
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application


TOKEN = '6569461259:AAEu8HfH6vohmD3QK93CUkDKX6D5nLuRzV4'


router = Router()


def main() -> None:
    # Dispatcher is a root router
    dp = dp
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(router)

    # Register startup hook to initialize webhook
    dp.startup.register(on_startup)

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

    # Create aiohttp.web.Application instance
    app = web.Application()

    # Create an instance of request handler,
    # aiogram has few implementations for different cases of usage
    # In this example we use SimpleRequestHandler which is designed to handle simple cases
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,

    )
    # Register webhook handler on application
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)

    # Mount dispatcher startup and shutdown hooks to aiohttp application
    setup_application(app, dp, bot=bot)

    # And finally start webserver
    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)


class Command(BaseCommand):
    help = "System To People Telegram Bot"

    def handle(self, *args, **options):
        main()
