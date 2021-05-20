import time
def multi_print(phrase: str, times):
    for i in range(times):
        print(phrase)
start = time.perf_counter_ns() # get the time in nano second
multi_print("hello", 10)
end = time.perf_counter_ns()
print(f"Time in nano seconds: {end-start}/1_000_000_000")


