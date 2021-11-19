<h1 align="center">@amirh-moshfeghi/kudo-box</h1>

<p align="center">
  <b>This is the instruction to run and customize a simple kudo service </b></br>
<br />





<details>
<summary>📖 Table of Contents</summary>
<br />


## ➤ Table of Contents

* [➤ Pre-Requisites]
* [➤ Installation]
* [➤ Compile]
* [➤ Execute and Run]
* [➤ Usage]
* [➤ How Rescue Simulation Works]
* [➤ Contributors]
* [➤ License]

</details>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#installation)

## ➤ Pre-Requisites

```
- Python 
- Django 
- Django REST Framework
- Djangorestframework-simplejwt
- Swagger
```

These are same Pre-Requisites for both Linux and Windows

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#installation)

## ➤ Installation

```bash
$ git clone https://github.com/amirh-moshfeghi/kudo_cards.git
```

After you cloned the repository, you want to create a virtual environment, so you have a clean python installation. You can do this by running the command :


```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this here

You can install all the required dependencies by running

```
pip install -r requirements.txt
```



[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#getting-started-slower)

## ➤ Execute and Run



We can test the API using curl or httpie, or we can use Postman
First, we have to start up Django's development server.

```bash
python manage.py runserver
```

Only authenticated users can use the API services, for that reason if we try this:

```
http  http://127.0.0.1:8000/api/v1/kudos/
```

we get:

```
{
    "detail": "Authentication credentials were not provided."
}
```

Instead, if we try to access with credentials:

```
http http://127.0.0.1:8000/api/v1/kudos/3 "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA4Mjk1LCJqdGkiOiI4NGNhZmMzMmFiZDA0MDQ2YjZhMzFhZjJjMmRiNjUyYyIsInVzZXJfaWQiOjJ9.NJrs-sXnghAwcMsIWyCvE2RuGcQ3Hiu5p3vBmLkHSvM"
```
[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#getting-started-slower)

### ➤ Create users and Tokens

First we need to create a user, so we can log in

```
http POST http://127.0.0.1:8000/api/v1/auth/register/ email="email@email.com" username="USERNAME" password1="PASSWORD" password2="PASSWORD"
```

After we create an account we can use those credentials to get a token

To get a token first we need to request:
```
http http://127.0.0.1:8000/api/v1/auth/token/ username="username" password="password"
```

after that, we get the token

```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNjI5MjMyMSwianRpIjoiNGNkODA3YTlkMmMxNDA2NWFhMzNhYzMxOTgyMzhkZTgiLCJ1c2VyX2lkIjozfQ.hP1wPOPvaPo2DYTC9M1AuOSogdRL_mGP30CHsbpf4zA",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA2MjIxLCJqdGkiOiJjNTNlNThmYjE4N2Q0YWY2YTE5MGNiMzhlNjU5ZmI0NSIsInVzZXJfaWQiOjN9.Csz-SgXoItUbT3RgB3zXhjA2DAv77hpYjqlgEMNAHps"
}
```

We got two tokens, the access token will be used to authenticated all the requests we need to make, this access token will expire after some time. We can use the refresh token to request a need access token.

requesting new access token

```
http http://127.0.0.1:8000/api/v1/auth/token/refresh/ refresh="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNjI5MjMyMSwianRpIjoiNGNkODA3YTlkMmMxNDA2NWFhMzNhYzMxOTgyMzhkZTgiLCJ1c2VyX2lkIjozfQ.hP1wPOPvaPo2DYTC9M1AuOSogdRL_mGP30CHsbpf4zA"
```

and we will get a new access token

```
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA4Mjk1LCJqdGkiOiI4NGNhZmMzMmFiZDA0MDQ2YjZhMzFhZjJjMmRiNjUyYyIsInVzZXJfaWQiOjJ9.NJrs-sXnghAwcMsIWyCvE2RuGcQ3Hiu5p3vBmLkHSvM"
}
```

The API has some restrictions:

-   The kudos are associated with a creator (user who created it).
-   Only authenticated users may create and see kudos.
-   Only the creator of a kudo may update or delete it(or manager or team leader dependent on situation).
-   The API doesn't allow unauthenticated and unauthorized requests.


| Endpoint                | HTTP Method	                                             | CRUD/Result	                                      |
|-----------------------|--------------------------------------------------|--------------------------------------------------|
| kudos         | GET                                           | READ/Get all kudos|
| kudos/:id    | GET |READ/Get single object of kudo |
| kudos         | POST                                           | CREATE/Create a single kudo   |
| kudos/:id          | PUT                                           | UPDATE/Update a kudo |
| kudos/:id            | DELETE                                                 |DELETE/Delete a kudo                       |



<br>
<br>


### ➤ Pagination
<sub>
The API supports pagination, by default responses have a page_size=10 but if you want change that you can pass through params page_size={your_page_size_number}

```
http http://127.0.0.1:8000/api/v1/kudos/?page=1 "Authorization: Bearer {YOUR_TOKEN}"
```

### ➤ Filters
<br>
The API supports filtering, you can filter by the attributes of a kudo like this:

```
http http://127.0.0.1:8000/api/v1/kudos/?creator__username="myUsername" "Authorization: Bearer {YOUR_TOKEN}"
```

</sub>
<p align="right"> توضیحات تکمیلی</p>
<p align="right"> من در این مینی پروژه سعی کردم استانداردها و پروپوزال های رایج اصول کدنویسی تمیز رو رعایت کنم ،همچنین سعی کردم برای هر سرویس از لایبرری های مرسوم استفاده نکنم و از اول بنویسم مثل سرویس های رجیستر و غیره</p>
<p align="right">تمامی اندپوینت ها تست شده و داخل کالکشن پستمن رسکوئست ها و ریسپانس ها قرار داده شده
</p>
<p align="right"> کانسپت کلی پروژه به صورت پیش فرض بر روی استفاده از یوزرمدل و سطح دسترسی های شخصی سازی شده بوده و سطح دسترسی های مدیر تیم و مدیر سازمان و هر کارمند به صورت مجزا تعریف شده</p>
<p align="right">جهت سهولت دریافت دیتا،صفحه گذاری و فیلتر سرچ بر روی کوئری پارامتر هم قرار داده شده است </p>
<p align="right ">نکته ی اخر اینکه این تسک حدود 9-10 ساعت زمان برده،خوشحال میشم اگر نظری یا سوالی دارید با من در تماس باشید </p>

## ➤ Contributors


| [<img alt="Amir Moshfeghi" src="https://avatars.githubusercontent.com/u/92248573?s=40&v=4" width="60">](https://amirmoshfegh.com) |  
|:--------------------------------------------------:|
| [Amirhossein  Moshfeghi](https://www.linkedin.com/in/amir-moshfeghi) |  






[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#license)







