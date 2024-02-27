import random
import threading
import time
from queue import Queue


def task_producer(task_queue: Queue, time_between_events: float):
    counter = 0
    while True:
        message = f"{counter} th message being sent"
        counter += 1
        task_queue.put(message)
        time.sleep(time_between_events)
        print(f"current size of Task Queue: {task_queue.qsize()}")


def heavy_io(taskqueue: Queue, result_queue):
    while True:
        task_str = taskqueue.get()
        time.sleep(random.randint(1, 5))
        result_queue.put("result: " + task_str)


def welcome_results(result_queue: Queue):
    while True:
        res = result_queue.get()
        print("Welcome result: ", res)


def main(time_between_events: float, thread_count: int):
    task_queue = Queue()
    result_queue = Queue()
    thread_list = list()

    task_thread = threading.Thread(target=task_producer, args=(task_queue, time_between_events))
    task_thread.start()

    for _ in range(thread_count):
        t = threading.Thread(target=heavy_io, args=(task_queue, result_queue))
        thread_list.append(t)
    [t.start() for t in thread_list]

    result_thread = threading.Thread(target=welcome_results, args=(result_queue, ))
    result_thread.start()

    task_thread.join()


if __name__ == '__main__':
    main(0.5, 10)
