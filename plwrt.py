from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


word = "Помидоры (свежие)"

with sync_playwright() as p:

    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://fitaudit.ru/food ')
    page.is_visible('main')
    page.click(f'a[title="{word}"]')
    page.is_visible('p.him_bx__wrap')
    html = page.inner_html('.him_bx__wrap')
    soup = BeautifulSoup(html, 'lxml')

    data = soup.find_all('span', class_='js__msr_cc')

    calories = int(data[-6].text.split()[0])
    jiry = float(data[-5].text.split()[0].replace(',', '.'))
    belki = float(data[-4].text.split()[0].replace(',', '.'))
    uglevody = float(data[-3].text.split()[0].replace(',', '.'))
    voda = float(data[-2].text.split()[0].replace(',', '.'))
    zola = float(data[-1].text.split()[0].replace(',', '.'))

    output = {
        'calories': calories,
        'jiry': jiry,
        'belki': belki,
        'uglevody': uglevody,
        'voda': voda,
        'zola': zola
    }
    print(output)