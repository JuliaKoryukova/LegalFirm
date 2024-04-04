import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'legal_firm_project.settings')
django.setup()

from legal_firm.main.models import LegalFirm, Service, Contact

name = "Юридическая фирма LexNova"
description = ('"LexNova" - это юридическая фирма, специализирующаяся на предоставлении высококачественных юридических услуг '
               'для клиентов по всему миру. Наша команда состоит из опытных и высококвалифицированных юристов, готовых помочь '
               'в решении самых сложных правовых вопросов. Мы стремимся к долгосрочным отношениям с нашими клиентами, предлагая '
               'им экспертные знания и непревзойденный уровень обслуживания.')
address = "ул. Пушкина, дом 10, офис 201, г. Приморск"
phone = "+7 (123) 456-78-90"
email = "info @ lexnova.com"
name_us = "Услуги"
description_us = ("Интеллектуальное право: Мы предоставляем экспертные консультации и защищаем интересы клиентов в сфере интеллектуальной "
                  "собственности, включая авторские права, патенты, товарные знаки и другие аспекты интеллектуальной собственности. "
                  "Коммерческое право: Наша фирма оказывает полный спектр услуг по коммерческому праву, включая юридическое сопровождение сделок,"
                  " составление договоров, корпоративное управление и решение споров в сфере бизнеса. "
                  "Миграционное право: Мы предоставляем профессиональную помощь в вопросах миграционного права, включая получение виз, "
                  "разрешений на работу, гражданство и решение других иммиграционных вопросов. "
                  "Налоговое право: Наша команда специалистов по налоговому праву помогает клиентам оптимизировать налоговые обязательства, "
                  "обеспечивая соблюдение налогового законодательства и защиту от неправомерных действий со стороны налоговых органов. "
                  "Судебное представительство: Мы предоставляем квалифицированную правовую помощь и представляем интересы клиентов в судах "
                  "на всех уровнях юрисдикции, обеспечивая защиту и реализацию их прав и интересов в различных правовых спорах.")
def create_legal_firm():
    firm = LegalFirm.objects.create(name=name, description=description)
    Contact.objects.create(firm=firm, address=address, phone=phone, email=email)
    Service.objects.create(firm=firm, name=name_us, description=description_us)

if __name__ == '__main__':
    create_legal_firm()