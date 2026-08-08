# Error Handling Notes

## Error Types

- ValueError: وقتی مقدار مناسب نیست
- IndexError: وقتی index بیرون از محدوده است
- NameError: وقتی اسم اشتباه نوشته شده یا وجود ندارد
- ZeroDivisionError: وقتی تقسیم بر صفر انجام شود
- TypeError: وقتی نوع داده اشتباه باشد

## try / except

- try: کدی که ممکن است خطا بدهد
- except: گرفتن خطا

## except specific

- بهتر است خطای مشخص را بگیریم
- مثال:
  - ValueError
  - IndexError

## as e

- خطا را داخل e نگه می‌داریم
- با {e} پیام خطا را نشان می‌دهیم

## else

- فقط وقتی اجرا می‌شود که خطا نباشد

## finally

- همیشه اجرا می‌شود

## return

- مقدار معتبر را از تابع برمی‌گرداند

## raise

- خودمان خطا می‌سازیم
- وقتی ورودی از نظر منطقی غلط است

## Important Rule

- traceback را از پایین به بالا بخوان
- آخرین خط معمولاً مهم‌ترین خط است

my_project/
├── src/
│ └── my_project/
│ ├── **init**.py
│ └── main.py
├── tests/
│ └── test_main.py
├── README.md
├── requirements.txt
└── .gitignore
