# Land Live+ MVP (Django Backend)

👋 Welcome to Land Corporation's first MVP!

This is a **Minimal Viable Product (MVP)** that consists of `reservation system` and `KakaoTalk notification` features along with visual guide line to help users understand the work flow. Main purpose of this MVP is to **_test whether there exists market needs for live-streaming tour for Real Estate_** while investing as minimum development as possible.

> Note that this is a MVP which does not contain any **real-time streaming** feature. Actual real-time streaming feature will be developed on next cycle; prototyping.

<p><br></p>

## Background

Please refer **[here](https://github.com/Land-Corporation/land-live-web#background)**

<p><br></p>

## Installation

Use the package manager [yarn](https://yarnpkg.com/) to install land-live-web

```bash
pip install -r requirements
```

<p><br></p>

## Usage

```bash
python manage.py migrate
python manage.py runserver
```

And open `http://localhost:8000/`

<p><br></p>

## Look & Feel

To see how it looks, please visit 👉 **[landcorp.io](https://landcorp.io)**

<p align="center">
  <img src="https://github.com/Land-Corporation/land-live-web/blob/devel/photo/landing_page.png" width="100%" title="hover text">
</p>


## Troubleshooting

### 1. **Mysql Insert throws error when sending `emoji` in POST payload**

#### Problem
```python3
    err.raise_mysql_exception(self._data)
  File "/Users/jinj/.virtualenvs/landapp/lib/python3.7/site-packages/pymysql/err.py", line 107, in raise_mysql_exception
    raise errorclass(errno, errval)
django.db.utils.DataError: (1366, "Incorrect string value: '\\xF0\\x9F\\x98\\x8A\\xF0\\x9F...' for column 'content' at row 1")
```

#### Solution
* MySQL DB Setting
  * utf8mb4_unicode_ci, utf8mb4

<p align="center">
  <img src="https://github.com/Land-Corporation/land-live-web/blob/master/photo/mysql_emoji.png" width="70%" title="hover text">
</p>
Screen Shot 2021-01-09 at 7.44.56 PM.png

* Table Setting
  * Room
  * Feedback
`ALTER TABLE <table_name> CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;`

* Django Setting
```python3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'use_unicode': True, },
    }
```

<p><br></p>

## Guide

Please refer **[here](https://github.com/Land-Corporation/land-live-web#guide)**

## Contributing

- All rights reserved to Land Corporation, Inc.
- Main developer: [@JinJis](https://github.com/JinJis)

<p><br></p>

## License

[MIT](https://choosealicense.com/licenses/mit/)
