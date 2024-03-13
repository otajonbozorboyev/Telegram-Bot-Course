# http://github.com/fawazahmed0/quran-api
import requests
from pprint import pprint as print

surah = 1
oyat = 4
tafsiri = 'uzb-muhammadsodikmu'
url_surah = f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsiri}/{surah}.json'
url_oyat = f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsiri}/{surah}/{oyat}.json'

response = requests.get(url_surah)
# response = requests.get(url_oyat) # Agar quyidagicha qilsak oyatlar bo'yicha chiqargan bo'lar ekanmiz.
# print(response.status_code)
res = response.json()
print(res)
# print(res.keys()) # Agar responseda qanday keylar borligini bilmoqchi bo'lsak,
# shunday yozib qanday keylar aniqlashimiz va aynan o'sha keylar bilan quyidagicha amallar bajarishimiz mumkin.
# print(res['text']) # Faqat matnning o'zi chiqadi.
