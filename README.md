# Python asyncio IOT

- **Please note:** read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md)
before starting.

You're given a skeleton of the IoT service taken from the internet.
As you have noticed - it's fully synchronous and has blocking operations (sleep for example).
The idea of this task is to make the program work faster (using asyncio) without breaking its logic.

For easier asynchronous setup please follow these steps:
1. Make your code use asyncio - connect/disconnect/send_message must be async functions (just the async/await interface). 
   Is the code working faster? If the answer is no - then proceed.
2. Try to `gather` registering devices - that should be easy, devices may be registered simultaneously.
   And when you run the code - wow it works faster (at least should). 
   That's because each device doesn't need to wait for the previous to register.
3. After that `gather` running programs (in `service.py`) - here the code also may be easy.
   And if you run it - wow! it works so fast, asyncio is powerful. But look at the logic.
   We've broken it: we may start playing music on Speaker before it was turned on, 
   same with flushing and cleaning Smart Toilet. So, despite it working fast, it works incorrectly.
4. And finally your task is to fix these logical problems. As you already have understood, some of these
   operations may be performed in "parallel", and some of them must still run in a sequence (flush -> clean).
   So, you may use these helper functions:
    ```python
    from typing import Any, Awaitable
    
    
    async def run_sequence(*functions: Awaitable[Any]) -> None:
        for function in functions:
            await function
    
    
    async def run_parallel(*functions: Awaitable[Any]) -> None:
        await asyncio.gather(*functions)
    ```
   And change the `wake_up_program`, and `sleep_program` blocks and their run - to a combination of
   `run_sequence` and `run_parallel` sending messages to the service (please do that separately, firstly for wake_up, then for sleep). 
   So the logic won't be broken. After that, your code will work a bit longer (still faster than at the beginning), 
   but at least it works correctly now.
    



