def fibonacci (n):
    if  n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
def fibonacci_caching (n, cacheNone):
    if  cache is None:
        cache=()
    if  n<=1:
        return n
    if n in cache:
        return cache[n]
    resul= fibonacci_caching(n-1, cache)+ fibonacci_caching(n-2, cacheNone)
    return resul

def main():
    print("programacion dinamica")

    star_time = time.time_ns()
    print(fibonacci(4))
    end_time = time.time_ns
    print (f"Time taken: (end_time-star_time) ns")

    
    star_time = time.time_ns()
    print(fibonacci_caching(4))
    end_time = time.time_ns
    print (f"Time taken: (end_time-star_time) ns")
    

if __name__ == "__main__":
    main()