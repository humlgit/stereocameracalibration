import functools
import queue
import threading
import time

def producer(num, frame_queue):
    for i in range(num):
        frame_queue.put(i)
        print(f"PRODUCER: added {i} to queue")
        time.sleep(0.05)

def consumer(frame_queue):
    while True:
        i = frame_queue.get()
        print(f"CONSUMER: popped {i} from queue")
        time.sleep(0.1)
        frame_queue.task_done()

def main():
    frame_queue = queue.Queue()
    threading.Thread(target=functools.partial(consumer, frame_queue), daemon=True).start()
    producer(10, frame_queue)
    print("MAIN: waiting for frame_queue to be emptied")
    frame_queue.join()

if __name__ == "__main__":
    main()