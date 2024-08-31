from threading import Thread
from time import sleep
from datetime import datetime

from tensorflow.python.ops.summary_ops_v2 import write


def write_words(count, name):
    with open(name, "w", encoding="utf-8") as file:
        for i in range(count):
            file.write(f"Какое-то слово N{i+1}\n")
            sleep(0.1)
        print(f"Закончилась запись в файл {name}")


start = datetime.now()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
end = datetime.now()
print(f"Время работы функций: {end-start}")

start = datetime.now()
thr_first = Thread(target=write_words, args=(10, "example5.txt"))
thr_second = Thread(target=write_words, args=(30, "example6.txt"))
thr_third = Thread(target=write_words, args=(200, "example7.txt"))
thr_fourth = Thread(target=write_words, args=(100, "example8.txt"))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

end = datetime.now()
print(f"Время работы функций: {end-start}")
