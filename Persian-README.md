برنامه چت در زمان واقعی با استفاده از Redis Pub/Sub و Stream

مقدمه

این پروژه یک برنامه چت در زمان واقعی است که از Redis Pub/Sub و Stream برای پیام‌رسانی همزمان بین کاربران استفاده می‌کند. این برنامه به کاربران اجازه می‌دهد کانال‌های چت ایجاد کنند، پیام ارسال کنند و به کانال‌ها مشترک شوند.

ویژگی‌ها

پیام‌رسانی در زمان واقعی با استفاده از Redis Pub/Sub و Stream

ایجاد و مدیریت کانال‌ها

اشتراک کاربران و پخش پیام‌ها

رابط کاربری ترمینال برای تعامل آسان کاربران

شروع به کار

پیش‌نیازها

نصب و اجرای Redis بر روی سیستم محلی یا استفاده از یک ارائه‌دهنده ابری

نصب Python نسخه 3.8 یا بالاتر بر روی سیستم محلی

نصب بسته‌های پایتون redis و hiredis با استفاده از pip

اجرای برنامه

مخزن را کلون کنید: git clone <https://github.com/PEMIDI/real-time-chat-app.git>

بسته‌های مورد نیاز را نصب کنید: pip install -r requirements.txt

سرور Redis را اجرا کنید: redis-server

برنامه را اجرا کنید: python app.py

استفاده از برنامه

یک ترمینال باز کرده و برنامه را اجرا کنید: python app.py

یک کانال ایجاد کنید: /join <نام_کانال>

پیام ارسال کنید: /send <پیام>

به یک کانال مشترک شوید: /join <نام_کانال>

از یک کانال خارج شوید: /leave

تمام کانال‌ها را لیست کنید: /channels

برنامه را ترک کنید: /quit

پیکربندی

پیکربندی Redis

REDIS_HOST: نام میزبان یا آدرس IP نمونه Redis (پیش‌فرض: localhost)

REDIS_PORT: شماره پورت نمونه Redis (پیش‌فرض: 6379)

REDIS_DB: شماره دیتابیس برای استفاده (پیش‌فرض: 0)

REDIS_PASSWORD: رمز عبور برای احراز هویت (اختیاری)

پیکربندی برنامه

CHANNEL_PREFIX: پیشوند نام کانال‌ها (پیش‌فرض: channel:)

MESSAGE_PREFIX: پیشوند شناسه پیام‌ها (پیش‌فرض: message:)

عیب‌یابی

بررسی لاگ‌های سرور Redis برای خطاها

بررسی لاگ‌های برنامه برای خطاها

اطمینان از اجرای نمونه Redis و قابل دسترس بودن آن

مشارکت

مشارکت‌ها خوش‌آمده هستند. لطفاً مخزن را فورک کرده و با تغییرات خود یک درخواست کشش (Pull Request) ارسال کنید.

مجوز

این پروژه تحت مجوز MIT منتشر شده است. برای جزئیات به فایل LICENSE مراجعه کنید.

تشکر و قدردانی

این پروژه از کتابخانه‌های متن‌باز زیر استفاده می‌کند:

redis: یک کلاینت پایتون برای Redis

hiredis: یک کلاینت پایتون برای Redis که از پارسر Hiredis استفاده می‌کند

امیدوارم این اطلاعات مفید باشد. اگر سؤالی دارید یا به کمک بیشتری نیاز دارید، لطفاً اطلاع دهید.

مستند نیازمندی‌های محصول

عنوان کار: برنامه چت در زمان واقعی با Redis Pub/Sub و Stream 📱💬

مستند نیازمندی‌های محصول

مقدمه:
یک برنامه چت در زمان واقعی با استفاده از Redis Pub/Sub و Stream ایجاد کنید. این برنامه باید به کاربران اجازه دهد پیام‌ها را در زمان واقعی ارسال و دریافت کنند. این برنامه باید ویژگی‌های زیر را داشته باشد:

کاربران می‌توانند کانال‌ها ایجاد کنند و پیام‌ها را به کانال‌های خاص ارسال کنند.

کاربران می‌توانند به کانال‌ها مشترک شوند و پیام‌ها را در زمان واقعی دریافت کنند.

پیام‌ها باید در یک Redis Stream برای ماندگاری و مقیاس‌پذیری ذخیره شوند.

ساختار پروژه:

real-time-chat-app/
app.py
models.py
redis_config.py
requirements.txt
README.md
tests/
test_app.py
test_models.py

نیازمندی‌های کار:

بخش 1: راه‌اندازی Redis و کلاینت پایتون (1 ساعت) 🚀

نصب Redis بر روی سیستم محلی یا استفاده از یک ارائه‌دهنده ابری مانند Redis Labs.

نصب بسته‌های پایتون مورد نیاز، شامل:

redis برای تعامل با Redis.

hiredis برای پارس کردن پاسخ‌های Redis.

pytest برای تست واحد.

ایجاد یک فایل redis_config.py برای ذخیره تنظیمات اتصال Redis، شامل:

REDIS_HOST: نام میزبان یا آدرس IP نمونه Redis.

REDIS_PORT: شماره پورت نمونه Redis.

REDIS_DB: شماره دیتابیس برای استفاده.

REDIS_PASSWORD: رمز عبور برای احراز هویت (اختیاری).

بخش 2: پیاده‌سازی Redis Pub/Sub (2 ساعت) 📢

ایجاد یک فایل models.py برای تعریف مدل‌های زیر:

User: مدلی با یک id و username یکتا.

Channel: مدلی با یک id و name یکتا.

پیاده‌سازی یک تابع publish_message در app.py برای انتشار یک پیام به یک کانال خاص با استفاده از Redis Pub/Sub. این تابع باید:

یک channel_id و message به عنوان ورودی دریافت کند.

از کلاینت redis برای انتشار پیام به کانال مشخص شده استفاده کند.

یک پیام موفقیت‌آمیز که نشان می‌دهد پیام منتشر شده است را برگرداند.

پیاده‌سازی یک تابع subscribe_to_channel در app.py برای مشترک شدن به یک کانال خاص و دریافت پیام‌ها در زمان واقعی. این تابع باید:

یک channel_id به عنوان ورودی دریافت کند.

از کلاینت redis برای مشترک شدن به کانال مشخص شده استفاده کند.

یک پیام موفقیت‌آمیز که نشان می‌دهد اشتراک موفقیت‌آمیز بوده است را برگرداند.

بخش 3: پیاده‌سازی Redis Stream (2 ساعت) 📊

تغییر فایل models.py برای اضافه کردن یک مدل Stream با ویژگی‌های زیر:

id: یک شناسه یکتا برای پیام.

channel_id: شناسه کانالی که پیام به آن ارسال شده است.

message: متن پیام.

timestamp: زمانی که پیام ارسال شده است.

پیاده‌سازی یک تابع produce_message در app.py برای تولید یک پیام به یک Redis Stream. این تابع باید:

یک channel_id و message به عنوان ورودی دریافت کند.

از کلاینت redis برای تولید پیام به Redis Stream استفاده کند.

یک پیام موفقیت‌آمیز که نشان می‌دهد پیام تولید شده است را برگرداند.

پیاده‌سازی یک تابع consume_message در app.py برای مصرف پیام‌ها از یک Redis Stream و ذخیره آن‌ها در مدل Stream. این تابع باید:

یک channel_id به عنوان ورودی دریافت کند.

از کلاینت redis برای مصرف پیام‌ها از Redis Stream استفاده کند.

هر پیام را در مدل Stream ذخیره کند.

یک پیام موفقیت‌آمیز که نشان می‌دهد پیام‌ها مصرف شده‌اند را برگرداند.

بخش 4: ادغام Pub/Sub و Stream (2 ساعت) 🤝

تغییر تابع publish_message برای تولید یک پیام به یک Redis Stream به جای انتشار به یک کانال.

تغییر تابع subscribe_to_channel برای مصرف پیام‌ها از یک Redis Stream و پخش آن‌ها به مشترکان.

پیاده‌سازی یک تابع broadcast_message در app.py برای پخش یک پیام به تمام مشترکان یک کانال. این تابع باید:

یک channel_id و message به عنوان ورودی دریافت کند.

از کلاینت redis برای پخش پیام به تمام مشترکان کانال استفاده کند.

یک پیام موفقیت‌آمیز که نشان می‌دهد پیام پخش شده است را برگرداند.

بخش 5: تست و اشکال‌زدایی (1 ساعت) 🧐

نوشتن تست‌های واحد برای هر تابع با استفاده از pytest.

تست سناریوهای زیر:

انتشار یک پیام به یک کانال و تأیید اینکه توسط مشترکان دریافت شده است.

تولید یک پیام به یک Redis Stream و تأیید اینکه در مدل Stream ذخیره شده است.

مصرف پیام‌ها از یک Redis Stream و تأیید اینکه به مشترکان پخش شده‌اند.

اشکال‌زدایی و رفع هرگونه مشکلاتی که در حین تست رخ می‌دهند.

زمان تخمینی: 8 ساعت

تحویل‌دادنی‌ها:

یک برنامه چت در زمان واقعی با استفاده از Redis Pub/Sub و Stream.

یک فایل README.md با دستورالعمل‌های نح

وه اجرای برنامه.

یک فایل requirements.txt با بسته‌های پایتون مورد نیاز.

تست‌های واحد برای هر تابع با استفاده از pytest.

توجه: این وظیفه برای حدود 8 ساعت طراحی شده است، اما می‌توانید محدوده و پیچیدگی آن را بر اساس نیازهای خود تنظیم کنید. موفق باشید 💪

معماری

در اینجا یک طراحی سطح بالا برای برنامه چت در زمان واقعی با استفاده از Redis Pub/Sub و Stream ارائه شده است:

اجزاء:

کلاینت: یک کلاینت وب که به کاربران اجازه می‌دهد کانال‌ها را ایجاد کنند، پیام ارسال کنند و به کانال‌ها مشترک شوند.

سرور: یک سرور مبتنی بر پایتون که درخواست‌های ورودی از کلاینت‌ها را پردازش می‌کند، پیام‌ها را به Redis Pub/Sub منتشر می‌کند و پیام‌ها را به Redis Stream تولید می‌کند.

Redis: یک نمونه Redis که اطلاعات کانال‌ها، اشتراک کاربران و داده‌های پیام را ذخیره می‌کند.

معماری:

          \+---------------+
          |  کلاینت       |
          \+---------------+
                  |
                  |  (درخواست‌های HTTP)
                  v
          \+---------------+
          |  سرور         |
          \+---------------+
                  |
                  |  (Redis Pub/Sub)
                  v
          \+---------------+
          |  Redis        |
          \+---------------+
                  |
                  |  (اطلاعات کانال)
                  |  (اشتراک کاربران)
                  |  (داده‌های پیام)
                  v
          \+---------------+
          |  Redis Stream |
          \+---------------+

اجزای سرور:

مدیر کانال: مسئول ایجاد، بروزرسانی و حذف کانال‌ها.

مدیر اشتراک: مسئول مدیریت اشتراک کاربران به کانال‌ها.

ناشر پیام: مسئول انتشار پیام‌ها به Redis Pub/Sub.

تولیدکننده پیام: مسئول تولید پیام‌ها به Redis Stream.

مصرف‌کننده پیام: مسئول مصرف پیام‌ها از Redis Stream و پخش آن‌ها به مشترکان.

ساختارهای داده Redis:

کانال‌ها: یک Redis Hash که اطلاعات کانال‌ها، شامل شناسه کانال، نام و توضیحات را ذخیره می‌کند.

اشتراک کاربران: یک Redis Set که اشتراک کاربران به کانال‌ها، شامل شناسه کاربر و شناسه کانال را ذخیره می‌کند.

داده‌های پیام: یک Redis Stream که داده‌های پیام، شامل شناسه پیام، شناسه کانال، متن پیام و زمان ارسال را ذخیره می‌کند.

جریان:

یک کلاینت درخواست ایجاد کانال به سرور ارسال می‌کند.

سرور یک کانال جدید ایجاد کرده و آن را در Redis ذخیره می‌کند.

یک کلاینت درخواست اشتراک به کانال به سرور ارسال می‌کند.

سرور کاربر را به لیست اشتراک‌های کانال در Redis اضافه می‌کند.

یک کلاینت یک پیام به کانال ارسال می‌کند.

سرور پیام را به Redis Pub/Sub منتشر می‌کند.

سرور پیام را به Redis Stream تولید می‌کند.

مصرف‌کننده پیام پیام را از Redis Stream مصرف کرده و به تمام مشترکان کانال پخش می‌کند.

مزایا:

پیام‌رسانی در زمان واقعی: Redis Pub/Sub و Stream پیام‌رسانی در زمان واقعی بین کلاینت‌ها را ممکن می‌سازند.

مقیاس‌پذیری: Redis Stream امکان مقیاس‌پذیری افقی و پردازش پیام با توان بالا را فراهم می‌کند.

ماندگاری: Redis Stream ماندگاری داده‌های پیام را فراهم می‌کند و اطمینان می‌دهد که پیام‌ها در صورت خرابی‌ها از دست نمی‌روند.

این طراحی یک معماری پایه برای برنامه چت در زمان واقعی با استفاده از Redis Pub/Sub و Stream را فراهم می‌کند. شما می‌توانید آن را بر اساس نیازهای خاص خود تغییر داده و گسترش دهید.

رابط کاربری

در اینجا یک طراحی برای رابط کاربری ترمینال برای برنامه چت در زمان واقعی با استفاده از Redis Pub/Sub و Stream ارائه شده است:

اجزای رابط کاربری ترمینال:

سربرگ: نمایش نام برنامه و نسخه.

لیست کانال‌ها: نمایش لیستی از کانال‌های موجود.

ورودی پیام: اجازه به کاربران برای وارد کردن و ارسال پیام‌ها.

لاگ پیام‌ها: نمایش لاگی از پیام‌های دریافت شده از کانال.

نوار وضعیت: نمایش کانال فعلی و وضعیت اشتراک کاربر.

چیدمان رابط کاربری ترمینال:

  \+---------------------------------------+
  |                  سربرگ                |
  \+---------------------------------------+
  |  نام برنامه: برنامه چت در زمان واقعی  |
  |  نسخه: 1.0                            |
  \+---------------------------------------+
  |              لیست کانال‌ها            |
  \+---------------------------------------+
  |  کانال 1: عمومی                       |
  |  کانال 2: توسعه                       |
  |  کانال 3: طراحی                       |
  \+---------------------------------------+
  |              ورودی پیام               |
  \+---------------------------------------+
  |  > یک پیام وارد کنید...               |
  \+---------------------------------------+
  |              لاگ پیام‌ها              |
  \+---------------------------------------+
  |  [10:00] کاربر1: سلام                 |
  |  [10:01] کاربر2: سلام                 |
  |  [10:02] کاربر3: سلام                 |
  \+---------------------------------------+
  |              نوار وضعیت               |
  \+---------------------------------------+
  |  کانال فعلی: عمومی                    |
  |  مشترک شده: بله                       |
  \+---------------------------------------+

دستورات رابط کاربری ترمینال:

/join <نام_کانال>: به یک کانال پیوسته و به پیام‌های آن مشترک شوید.

/leave: از کانال فعلی خارج شده و از پیام‌های آن انصراف دهید.

/channels: تمام کانال‌های موجود را لیست کنید.

/send <پیام>: یک پیام به کانال فعلی ارسال کنید.

/quit: برنامه را ترک کنید.

ویژگی‌های رابط کاربری ترمینال:

پیام‌رسانی در زمان واقعی: پیام‌ها به محض دریافت از کانال به صورت زنده نمایش داده می‌شوند.

تغییر کانال: کاربران می‌توانند با استفاده از دستور /join بین کانال‌ها جابه‌جا شوند.

ورودی پیام: کاربران می‌توانند پیام‌ها را در فیلد ورودی پیام وارد و ارسال کنند.

لاگ پیام‌ها: لاگ پیام‌ها تاریخچه‌ای از پیام‌های دریافت شده از کانال را نمایش می‌دهد.

نوار وضعیت: نوار وضعیت کانال فعلی و وضعیت اشتراک کاربر را نمایش می‌دهد.

طرح رنگ:

سربرگ: #333 (خاکستری تیره)

لیست کانال‌ها: #666 (خاکستری متوسط)

ورودی پیام: #999 (خاکستری روشن)

لاگ پیام‌ها: #CCC (خاکستری بسیار روشن)

نوار وضعیت: #666 (خاکستری متوسط)

فونت:

فونت تک فاصله: Consolas یا Courier New

این طراحی یک رابط کاربری ترمینال پایه برای برنامه چت در زمان واقعی با استفاده از Redis Pub/Sub و Stream را فراهم می‌کند. شما می‌توانید آن را بر اساس نیازهای خاص خود تغییر داده و گسترش دهید.