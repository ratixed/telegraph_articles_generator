import asyncio
from telegraph.aio import Telegraph


async def main():
    telegraph = Telegraph()
    print(await telegraph.create_account(short_name='Усатый Арбитражник'))

    response = await telegraph.create_page(
        title='Крепкие украинские аккаунты Facebook',
        author_name='Усатый Арбитражник',
        author_url='https://t.me/usaffiliate',
        html_content="""
        <p>🇺🇦  [UA] Мощнейший ручной фарм от 28 дней! Полностью заполненая ФП и соц. акк, более 10-ти фото на соце, много постов в ленте, БЕЗ БМОВ, ТОЛЬКО ЛИЧКА, 100+ друзей; 2FA (двух факторка установлена, коды есть в комплекте); 100+ действий вне ФБ, много реклама в ленте; </p>
        <p>🔥 Идеально подходят под Кингов</p>
        <p>💰 Цена 8$</p>
        <p>📲 Оплата USDT или Binance PAY</p>
        <p>😎 Возможна передача прямо в ваш Dolphin {Anty}</p>
        <p>✅ 1. Километровые кукисы для входа в формате .json</p>
        <p>✅ 2. Таблица с даными (Ключ 2FA для расширения Google Authificator, логин, пароль от акка и логин пароль от почты)</p>
        <p><img src="https://ik.imagekit.io/5owrhpglm/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2022-06-15_%D0%B2_21.43.22_AShncDY_r.png?ik-sdk-version=javascript-1.4.3&updatedAt=1655318607964"></p>
        """,
    )
    print(response['url'])


asyncio.run(main())