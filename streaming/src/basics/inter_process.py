import multiprocessing
from utils.queue import MyQueue as Queue
import time
import random


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


def main(time_between_events: float, process_count: int):
    task_queue = Queue()
    result_queue = Queue()
    process_list = list()

    task_process = multiprocessing.Process(target=task_producer, args=(task_queue, time_between_events))
    task_process.start()

    for _ in range(process_count):
        t = multiprocessing.Process(target=heavy_io, args=(task_queue, result_queue))
        process_list.append(t)
    [p.start() for p in process_list]

    result_thread = multiprocessing.Process(target=welcome_results, args=(result_queue, ))
    result_thread.start()

    task_process.join()


if __name__ == '__main__':
    main(0.5, 10)