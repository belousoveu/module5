import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __len__(self):
        return len(self.nickname)

    def __hash__(self):
        return hash(self.nickname + self.password)


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0

    def __str__(self):
        return self.title

    def __repr__(self):
        return "'" + self.title + "'"


class UrTube:
    users = []
    videos = []

    def __init__(self):
        self.current_user = None

    def register(self, nickname, password, age):
        if self.is_user(nickname):
            print(f"Пользователь {nickname} уже зарегистрирован.\nВведите другое имя или войдите со своим паролем")
            return
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.current_user = user
            print(f"Пользователь {nickname} успешно зарегистрирован.")
            return

    def login(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print(f"Вы успешно вошли как {nickname}.")
                return
            print(f"Неверный логин или пароль.")
        return

    def log_out(self):
        self.current_user = None
        print("Вы вышли из аккаунта.")
        return

    def is_user(self, nickname):
        for user in self.users:
            if user.nickname == nickname:
                return True
        return False

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def watch_video(self, title):
        if self.current_user is None:
            print('Вы не авторизованы')
            return
        current_video = self.find_video_by_title(title)
        if current_video is None:
            print(f'Видео {title} не найдено')
            return
        if current_video.adult_mode and self.current_user.age < 18:
            print('Вы не можете смотреть взрослый контент')
            return
        for t in range(current_video.time_now, current_video.duration + 1):
            print(f'Время воспроизведения : {t} из {current_video.duration}')
            time.sleep(1.0)
        print('Конец воспроизведения')
        current_video.time_now = 0

    def find_video_by_title(self, title):
        for video in self.videos:
            if video.title == title:
                return video
        return None

    def get_videos(self, title):
        return [video for video in self.videos if title.lower() in video.title.lower()]


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
