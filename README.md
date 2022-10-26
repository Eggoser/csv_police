### Задание из gist: https://gist.github.com/tm-minty/c39f9ab2de1c70ca9d4d559505678234



Таблица с индексом:
~~~~
create table police_calls
(
    id                         integer primary key,
    "Crime Id"                 integer,
    "Original Crime Type Name" integer,
    "Report Date"              datetime,
    "Call Date"                datetime,
    "Offense Date"             datetime,
    "Call Time"                datetime,
    "Call Date Time"           datetime,
    Disposition                varchar(100),
    Address                    varchar(100),
    City                       varchar(80),
    State                      varchar(80),
    "Agency Id"                varchar(100),
    "Address Type"             varchar(100),
    "Common Location"          varchar(100)
);

create index police_calls_ReportReportDate_index
    on police_calls ("Report Date");
~~~~



Лог файл: file.log

Перед началом работы поставить пакеты: `pip install -r requirements.txt`
И переместите файл police-department-calls-for-service.csv в корень проекта

Запуск API: `python api.py`

Чтобы протестировать API: `python test_api.py`

Скрипт загрузки в базу: `python load_to_database.py`
