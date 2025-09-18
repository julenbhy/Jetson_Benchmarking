import time
import threading
from jtop import jtop

def monitor_resources(func, *args, **kwargs):
    """Run func(*args, **kwargs) while monitoring Jetson resources."""
    max_stats = {}
    start_time = time.time()
    with jtop() as jetson:
        running = True
        result = None

        def run_func():
            nonlocal result, running
            result = func(*args, **kwargs)
            running = False

        t = threading.Thread(target=run_func)
        t.start()

        while running:
            stats = jetson.stats
            for key, value in stats.items():
                if isinstance(value, (int, float)):
                    if key not in max_stats or value > max_stats[key]:
                        max_stats[key] = value
            time.sleep(0.1)

        t.join()
    end_time = time.time()
    max_stats["execution_time_sec"] = round(end_time - start_time, 4)
    return result, max_stats
