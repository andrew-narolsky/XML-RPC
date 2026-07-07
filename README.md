# XML-RPC

Набір скриптів для роботи зі списком сайтів (домен + логін/пароль) та створення
тестових постів через WordPress XML-RPC API.

## Робочий процес

1. `sites.txt` — вхідний список у форматі `site<TAB>login<TAB>password` (по одному сайту на рядок).
2. `sites_to_csv.py` перетворює `sites.txt` на `sites.csv`.
3. `add_post_content.py` додає до `sites.csv` колонки `title`/`description` з тестовими значеннями.
4. `test_login.py` перевіряє логін/пароль на кожному сайті та записує результат у колонку `valid`.
5. `post_via_xmlrpc.py` створює пост на кожному сайті через XML-RPC і записує лінк на нього у колонку `url`.

## Скрипти

### sites_to_csv.py
Конвертує `sites.txt` у `sites.csv` (колонки `site, login, password`).
Заодно нормалізує `http://` → `https://`, прибирає дублікати за доменом (`site`) і сортує за доменом.

```
python3 sites_to_csv.py [вхідний.txt] [вихідний.csv]
# за замовчуванням: sites.txt -> sites.csv
```

### add_post_content.py
Додає до `sites.csv` колонки `title` та `description` з однаковими тестовими значеннями для всіх рядків.

```
python3 add_post_content.py [вхідний.csv] [вихідний.csv]
# за замовчуванням: sites.csv -> sites.csv (перезаписує той самий файл)
```

### test_login.py
Перевіряє логін/пароль кожного сайту через XML-RPC (`wp.getUsersBlogs`), нічого не створює.
Записує результат (`true`/`false`) у колонку `valid` в тому ж CSV.

```
python3 test_login.py [sites.csv]
# за замовчуванням: sites.csv
```

### post_via_xmlrpc.py
Для кожного рядка в `sites.csv` створює пост на сайті через XML-RPC (`metaWeblog.newPost`),
використовуючи `title`/`description` з CSV, і записує лінк створеного посту в колонку `url`.

```
python3 post_via_xmlrpc.py [sites.csv]
# за замовчуванням: sites.csv
```

⚠️ Цей скрипт реально публікує пост на сайті — запускати лише коли це дійсно потрібно.
