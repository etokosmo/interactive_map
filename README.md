# Interactive map of interesting places in Moscow

## About
This project allows you to use an interactive map of Moscow to show interesting places.

You can see this project [here](https://etokosmo.pythonanywhere.com/).

You can add location on admin-panel [here](https://etokosmo.pythonanywhere.com/admin/).

Frontend taken from this [repository](https://github.com/devmanorg/where-to-go-frontend).

Locations taken from this [repository](https://github.com/devmanorg/where-to-go-places).

## Project goals

* Create a Django project with interesting locations in Moscow
* Create an API with location data
* Make the admin-panel as convenient as possible for filling

> The code is written for educational purposes - this is a lesson in the course on Python and web development on the site [Devman](https://dvmn.org).

## Website example

You can see this project [here](https://etokosmo.pythonanywhere.com/).

![website example](https://user-images.githubusercontent.com/93794917/180652312-b4e9d5ab-d98f-455c-91bf-53b212a633ff.png)

## API

You can send request to `http://127.0.0.1:8000/places/{location_id: int}`.

You will get json data with information about this location.

<details>
  <summary>Example</summary>

#### Request
`http://127.0.0.1:8000/places/1`

#### Response
```json
{
  "title": "Экскурсионная компания «Легенды Москвы»",
  "imgs": [
    "/media/%D0%AD%D0%BA%D1%81%D0%BA%D1%83%D1%80%D1%81%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F%20%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D1%8F%20%C2%AB%D0%9B%D0%B5%D0%B3%D0%B5%D0%BD%D0%B4%D1%8B%20%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D1%8B%C2%BB/4f793576c79c1cbe68b73800ae06f06f.jpg",
    "/media/%D0%AD%D0%BA%D1%81%D0%BA%D1%83%D1%80%D1%81%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F%20%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D1%8F%20%C2%AB%D0%9B%D0%B5%D0%B3%D0%B5%D0%BD%D0%B4%D1%8B%20%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D1%8B%C2%BB/7a7631bab8af3e340993a6fb1ded3e73.jpg",
    "/media/%D0%AD%D0%BA%D1%81%D0%BA%D1%83%D1%80%D1%81%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F%20%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D1%8F%20%C2%AB%D0%9B%D0%B5%D0%B3%D0%B5%D0%BD%D0%B4%D1%8B%20%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D1%8B%C2%BB/a55cbc706d764c1764dfccf832d50541.jpg",
    "/media/%D0%AD%D0%BA%D1%81%D0%BA%D1%83%D1%80%D1%81%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F%20%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D1%8F%20%C2%AB%D0%9B%D0%B5%D0%B3%D0%B5%D0%BD%D0%B4%D1%8B%20%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D1%8B%C2%BB/65153b5c595345713f812d1329457b54.jpg",
    "/media/%D0%AD%D0%BA%D1%81%D0%BA%D1%83%D1%80%D1%81%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F%20%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D1%8F%20%C2%AB%D0%9B%D0%B5%D0%B3%D0%B5%D0%BD%D0%B4%D1%8B%20%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D1%8B%C2%BB/0a79676b3d5e3b394717b4bf2e610a57.jpg",
    "/media/%D0%AD%D0%BA%D1%81%D0%BA%D1%83%D1%80%D1%81%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F%20%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D1%8F%20%C2%AB%D0%9B%D0%B5%D0%B3%D0%B5%D0%BD%D0%B4%D1%8B%20%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D1%8B%C2%BB/1e27f507cb72e76b604adbe5e7b5f315.jpg"
  ],
  "description_short": "Неважно, живёте ли вы в Москве всю жизнь или впервые оказались в столице, составить ёмкий, познавательный и впечатляющий маршрут по городу — творческая и непростая задача. И её с удовольствием берёт на себя экскурсионная компания «Легенды Москвы»!",
  "description_long": "&lt;p&gt;Экскурсия от компании &amp;laquo;Легенды Москвы&amp;raquo; &amp;mdash; простой, удобный и приятный способ познакомиться с городом или освежить свои чувства к нему. Что выберете вы &amp;mdash; классическую или необычную экскурсию, пешую прогулку или путешествие по городу на автобусе? Любые варианты можно скомбинировать в уникальный маршрут и создать собственную индивидуальную &lt;strong&gt;экскурсионную программу&lt;/strong&gt;.&lt;/p&gt;\r\n&lt;p&gt;Компания &amp;laquo;Легенды Москвы&amp;raquo; сотрудничает с аккредитованными экскурсоводами и тщательно следит за качеством экскурсий и сервиса. Автобусные экскурсии проводятся на комфортабельном современном транспорте. Для вашего удобства вы можете заранее забронировать конкретное место в автобусе &amp;mdash; это делает посадку организованной и понятной.&lt;/p&gt;\r\n&lt;p&gt;По любым вопросам вы можете круглосуточно обратиться по телефонам горячей линии.&lt;/p&gt;\r\n&lt;p&gt;Подробности узнавайте &lt;a class=\"\\&amp;quot;external-link\\&amp;quot;\" href=\"\\&amp;quot;https:/moscowlegends.ru\" target=\"\\&amp;quot;_blank\\&amp;quot;\"&gt;на сайте&lt;/a&gt;. За обновлениями удобно следить &lt;a class=\"\\&amp;quot;external-link\\&amp;quot;\" href=\"\\&amp;quot;https:/vk.com/legends_of_moscow\" target=\"\\&amp;quot;_blank\\&amp;quot;\"&gt;&amp;laquo;ВКонтакте&amp;raquo;&lt;/a&gt;, &lt;a class=\"\\&amp;quot;external-link\\&amp;quot;\" href=\"\\&amp;quot;https:/www.facebook.com/legendsofmoscow?ref=bookmarks\" target=\"\\&amp;quot;_blank\\&amp;quot;\"&gt;в Facebook&lt;/a&gt;.&lt;/p&gt;",
  "coordinates": {
    "lng": 37.64912239999976,
    "lat": 55.77754550000014
  }
}
```
</details>

## Configurations

* Python version: 3.10
* Libraries: [requirements.txt](https://github.com/etokosmo/interactive_map/blob/main/requirements.txt)

## Launch

### Local server

- Download code
- Through the console in the directory with the code, install the virtual environment with the command:
```bash
python3 -m venv env
```

- Activate the virtual environment with the command:
```bash
source env/bin/activate
```

- Install the libraries with the command:
```bash
pip install -r requirements.txt
```

- Write the environment variables in the `.env` file in the format KEY=VALUE

`SECRET_KEY` - A secret key for a particular Django installation. This is used to provide cryptographic signing, and should be set to a unique, unpredictable value.

`ALLOWED_HOSTS` - A list of strings representing the host/domain names that this Django site can serve. This is a security measure to prevent HTTP Host header attacks, which are possible even under many seemingly-safe web server configurations.

`DEBUG` - A boolean that turns on/off debug mode. If your app raises an exception when DEBUG is True, Django will display a detailed traceback, including a lot of metadata about your environment, such as all the currently defined Django settings (from settings.py).

`DATABASE_URL` - URL to db. For more information check [this](https://github.com/jazzband/dj-database-url).

`MEDIA_URL` - URL that handles the media served from MEDIA_ROOT, used for managing stored files. It must end in a slash if set to a non-empty value.

- Create your database with the command:
```bash
python manage.py makemigrations
python manage.py migrate
```

- Run local server with the command (it will be available at http://127.0.0.1:8000/):
```bash
python manage.py runserver
```

## Management commands
You can load location with command:
```bash
python manage.py load_place http://address/file.json
```
<details>
  <summary>Example of <a href="https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json">file</a></summary>

```json
{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
    "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения. В стоимость уже включены напитки, сладкие угощения, библиотека комиксов, большая коллекция популярных настольных и видеоигр. Также вы можете арендовать ВИП-зал для большой компании и погрузиться в мир виртуальной реальности с помощью специальных очков от топового производителя.</p><p>В течение недели организаторы проводят разнообразные встречи для меломанов и киноманов. Также можно присоединиться к английскому разговорному клубу или посетить образовательные лекции и мастер-классы. Летом организаторы запускают марафон настольных игр. Каждый день единомышленники собираются, чтобы порубиться в «Мафию», «Имаджинариум», Codenames, «Манчкин», Ticket to ride, «БЭНГ!» или «Колонизаторов». Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```
</details>
