import requests
from bs4 import BeautifulSoup

def get_free_numbers():
    # مثال: بتجيب الأرقام من موقع عام
    url = "https://receive-smss.com/"
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        numbers = []
        # هنا بتحدد كيف تجيب الأرقام حسب الموقع
        for div in soup.find_all('div', class_='number-box'):
            numbers.append(div.text.strip())
        return numbers
    except Exception as e:
        return f"خطأ: {e}"

if __name__ == "__main__":
    print("الأرقام المتاحة حاليا:")
    print(get_free_numbers())
