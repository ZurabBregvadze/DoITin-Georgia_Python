########################################
#Homework_22 Task_1
########################################
import asyncio
import time

async def task_2_sec_delay():
    start_time = time.time()
    print(f"Task, 2 წამიანი დაყოვნებით დაიწყო: {start_time:.4f}")
    await asyncio.sleep(2)
    end_time = time.time()
    print(f"Task, 2 წამიანი დაყოვნებით დასრულდა: {end_time:.4f}")


async def task_5_sec_delay():
    start_time = time.time()
    print(f"Task 5 წამიანი დაყოვნებით დაიწყო: {start_time:.4f}")
    await asyncio.sleep(5)
    end_time = time.time()
    print(f"Task 5 წამიანი დაყოვნებით დასრულდა: {end_time:.4f}")


async def main():
    task_2 = asyncio.create_task(task_2_sec_delay())
    task_5 = asyncio.create_task(task_5_sec_delay())

    await task_2
    await task_5


asyncio.run(main())

########################################


########################################
#Homework_22 Task_2
########################################
import asyncio
import random

async def print_numbers_with_random_delay():
    for i in range(1, 11):
        print(i)

        delay = random.uniform(1, 5)

        await asyncio.sleep(delay)

async def main():
    await print_numbers_with_random_delay()

if __name__ == "__main__":
    asyncio.run(main())

########################################


########################################
#Homework_22 Task_3
########################################
import asyncio

async def is_even(number: int) -> bool:
    return number % 2 == 0

async def square_if_even(number: int) -> int:
    if await is_even(number):
        return number ** 2
    else:
        return None

async def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    tasks = [square_if_even(num) for num in numbers]
    results = await asyncio.gather(*tasks)

    for num, result in zip(numbers, results):
       if result is not None:
          print(f"{num}-ის კვადრატი არის {result}")
       else:
          print(f"{num} კენტია, კვადრატს არ გამოვითვლით")

asyncio.run(main())

########################################



########################################
#Homework_22 Task_4
########################################
import asyncio

async def write_to_file(filename, content):
    print(f"Task დაიწყო {filename} ფაილისთვის")
    await asyncio.sleep(2)
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Task დასრულდა {filename} ფაილისთვის")

async def main():

    tasks = [
        write_to_file('file1.txt', 'In file 1 text written'),
        write_to_file('file2.txt', 'In file 1 text written'),
        write_to_file('file3.txt', 'In file 1 text written')
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())

########################################
