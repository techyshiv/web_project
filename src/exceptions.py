import sys
from logger import logging


def error_message_details(error, error_details):
    _, _, exe_tb = error_details.exc_info()
    file_name = exe_tb.tb_frame.f_code.co_filename
    error_message = "Error Occured in Python Script  Name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exe_tb.tb_lineno, str(error)
    )
    return error_message


class CustomExceptions(Exception):
    def __init__(self, error_message, error_details):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details)

    def __str__(self):
        return self.error_message


try:
    print(1 / 0)
except Exception as e:
    logging.info(CustomExceptions(e, sys))
