import asyncio
from telegraph.aio import Telegraph


async def main():
    telegraph = Telegraph()
    print(await telegraph.create_account(short_name='Усатый Арбитражник'))

    response = await telegraph.create_page(
        title='Міцні акаунти Facebook для справжніх українців!',
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
        <p><img src="https://ik.imagekit.io/5owrhpglm/acc_poster_3.0__0xJiu_0Mu.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1655333413423"></p>
        <blockquote>Відгуки</blockquote>
        <p><img src="https://ik.imagekit.io/5owrhpglm/2_bsw5CUmST.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1655383714046"></p>
        <p><img src="https://ik.imagekit.io/5owrhpglm/5_2DIkqxrMXp.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1655383713913"></p>
        <p><img src="https://ik.imagekit.io/5owrhpglm/6_nBkQH8X3a.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1655383713864"></p>
        <p><img src="https://ik.imagekit.io/5owrhpglm/4_yrIZFdP5i.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1655383713915"></p>
        <p><img src="https://ik.imagekit.io/5owrhpglm/3_TPIcWA0Er.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1655383713897"></p>
        <p><img src="https://ik.imagekit.io/5owrhpglm/7_49ZFsmj2L.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1655383713943"></p>
        <p><img src="https://ik.imagekit.io/5owrhpglm/1_Vn5AAfGZ4.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1655383714052"></p>
        <p><img src="https://ik.imagekit.io/5owrhpglm/8_cvI-h7D-rG.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1655383714067"></p>
        <p><img src="https://ik.imagekit.io/5owrhpglm/11_H_lMoC03K.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1655383714893"></p>
        <p><img src="https://ik.imagekit.io/5owrhpglm/9_BL370Dkz-T.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1655383714321"></p>
        <p><img src="https://ik.imagekit.io/5owrhpglm/10_t8Zcnb2XI.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1655383714653"></p>
        <p><img src="https://ik.imagekit.io/5owrhpglm/12_rkhV-OxZV.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1655383715150"></p>
        <p><img src="https://ik.imagekit.io/5owrhpglm/16_g4yxxv0kr8.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1655383716052"></p>
        <p><img src="https://ik.imagekit.io/5owrhpglm/14_kIOWI15XLU.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1655383715651"></p>
        <p><img src="https://ik.imagekit.io/5owrhpglm/13_4Cg4afOL0.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1655383715357"></p>
        <p><img src="https://ik.imagekit.io/5owrhpglm/15_fAvhsUasEx.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1655383715886"></p>
        <p><img src="https://ik.imagekit.io/5owrhpglm/17_sitidD_iq.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1655383716242"></p>
        <p><img src="https://ik.imagekit.io/5owrhpglm/18_fa2flgFHN.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1655383716478"></p>
        <p><img src="https://ik.imagekit.io/5owrhpglm/19_prah7MBSY.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1655383716711"></p>
        """,
    )
    print(response['url'])


asyncio.run(main())