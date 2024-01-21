# class EmailValidator:
#     def __init__(self, min_length: int, mails: list, domains: list) -> None:
#         self.min_length = min_length
#         self.mails = mails
#         self.domains = domains

#     def __splitter(self, email: str):
#         name_and_all_else_of_email = email.split("@")
#         mail_and_domain = name_and_all_else_of_email[1].split(".")

#         name_of_email = name_and_all_else_of_email[0]
#         mail = mail_and_domain[0]
#         doamin = mail_and_domain[1]

#         return (name_of_email, mail, doamin)

#     def __is_name_valid(self, email: str):
#         splitted_email = self.__splitter(email)
#         if len(splitted_email[0]) >= self.min_length:
#             return True
#         else:
#             return False

#     def __is_mail_valid(self, email: str):
#         splitted_email = self.__splitter(email)
#         if splitted_email[1] in self.mails:
#             return True
#         else:
#             return False

#     def __is_domain_valid(self, email:str):
#         splitted_email = self.__splitter(email)
#         if splitted_email[2] in self.domains:
#             return True
#         else:
#             return False

#     def validate(self, email: str):
#         if self.__is_name_valid(email) and self.__is_mail_valid(email) and self.__is_domain_valid(email):
#             return True
#         else:
#             return False

class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: list) -> None:
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str):
        return mail in self.mails

    def __is_domain_valid(self, domain:str):
        return domain in self.domains

    def __splitter(self, email: str):
        name_and_all_else_of_email = email.split("@")
        mail_and_domain = name_and_all_else_of_email[1].split(".")

        name_of_email = name_and_all_else_of_email[0]
        mail = mail_and_domain[0]
        doamin = mail_and_domain[1]

        return (name_of_email, mail, doamin)

    def validate(self, email: str):
        if self.__is_name_valid(self.__splitter(email)[0]) and \
            self.__is_mail_valid(self.__splitter(email)[1]) and \
            self.__is_domain_valid(self.__splitter(email)[2]):
            return True
        else:
            return False


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
