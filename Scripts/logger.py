import datetime


class Logger:

    @classmethod
    def get_current_time(cls):
        return str(datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S--%f'))

    actions_file_name = f'src/logs/actions_{str(datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S--%f"))}.log'

    @classmethod
    def _write_actions_to_file(cls, data: str):
        with open(cls.actions_file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_action(cls, action: str):
        data_to_add = f'{cls.get_current_time()} {action}\n'
        cls._write_actions_to_file(data_to_add)

    nonexistent_lessons_file_name = f'src/logs/nonexistent_lessons_{str(datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S--%f"))}.log'

    @classmethod
    def _write_nonexistent_lesson_to_file(cls, data: str):
        with open(cls.nonexistent_lessons_file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_nonexistent_lesson(cls, lesson_id: str):
        data_to_add = f'{lesson_id}\n'
        cls._write_nonexistent_lesson_to_file(data_to_add)

    error_lessons_file_name = f'src/logs/error_lessons_{str(datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S--%f"))}.log'

    @classmethod
    def _write_error_lesson_to_file(cls, data: str):
        with open(cls.error_lessons_file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_error_lesson(cls, lesson_id: str):
        data_to_add = f'{lesson_id}\n'
        cls._write_error_lesson_to_file(data_to_add)



