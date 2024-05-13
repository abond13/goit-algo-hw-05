def binary_search_up(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    iter = 0
    up = arr[-1]
 
    while low <= high:
        iter += 1
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            up = arr[mid]
            high = mid - 1
 
        # інакше x присутній на позиції і повертаємо його
        else:
            return (iter, arr[mid])
 
    # якщо елемент не знайдений
    return (iter, up)

# Test
arr = [1.1, 2.2, 3.3, 4.4, 5.5]

print(binary_search_up(arr, 1.1))  # (2, 1.1)
print(binary_search_up(arr, 3.3))  # (1, 3.3)
print(binary_search_up(arr, 3))    # (3, 3.3)
print(binary_search_up(arr, -1.0)) # (2, 1.1)
print(binary_search_up(arr, 10))   # (3, 5.5)