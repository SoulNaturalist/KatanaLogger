import time
import asyncio
import unittest
from katanalogger import Logger

class TestKatanaLoggerStress(unittest.TestCase):
    def setUp(self):
        self.logger = Logger(emoji=False, time_log=False)

    def test_stress_log(self):
        async def test():
            start_time = time.time()
            for _ in range(1000):
                await self.logger.log("Stress test log message")
            end_time = time.time()
            print(f"Stress test for 'log': 1000 calls {end_time - start_time:.2f} seconds")
        asyncio.run(test())

    def test_stress_debug(self):
        async def test():
            start_time = time.time()
            for _ in range(1000):
                await self.logger.debug("Stress test debug message")
            end_time = time.time()
            print(f"Stress test for 'debug': 1000 calls {end_time - start_time:.2f} seconds")
        asyncio.run(test())

    def test_stress_die(self):
        async def test():
            start_time = time.time()
            for _ in range(1000):
                await self.logger.die("Stress test critical error")
            end_time = time.time()
            print(f"Stress test for 'die': 1000 calls {end_time - start_time:.2f} seconds")
        asyncio.run(test())

    def test_stress_log_traceback(self):
        async def test():
            start_time = time.time()
            for _ in range(1000):
                try:
                    1 / 0
                except Exception as e:
                    await self.logger.log_traceback(e)
            end_time = time.time()
            print(f"Stress test for 'log_traceback': 1000 calls {end_time - start_time:.2f} seconds")
        asyncio.run(test())

if __name__ == "__main__":
    unittest.main()