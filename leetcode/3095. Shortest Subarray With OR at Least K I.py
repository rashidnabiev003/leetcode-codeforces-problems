def minimumSubarrayLength(nums, k):
    n = len(nums)
    min_len = float('inf')
    left = 0
    bit_counts = [0] * 32  # Счетчики для 32 битов
    current_or = 0
    
    for right in range(n):
        # 1. Добавляем nums[right] в окно
        num = nums[right]
        for i in range(32):
            if (num >> i) & 1:  # Если i-й бит равен 1
                bit_counts[i] += 1
        
        # 2. Пересчитываем current_or на основе счетчиков
        current_or = 0
        for i in range(32):
            if bit_counts[i] > 0:
                current_or |= (1 << i)
        
        # 3. Пытаемся сжать окно слева, пока условие выполняется
        while current_or >= k and left <= right:
            # Обновляем минимальную длину
            min_len = min(min_len, right - left + 1)
            
            # Удаляем nums[left] из окна
            left_num = nums[left]
            for i in range(32):
                if (left_num >> i) & 1:
                    bit_counts[i] -= 1
            
            # Снова пересчитываем current_or
            current_or = 0
            for i in range(32):
                if bit_counts[i] > 0:
                    current_or |= (1 << i)
            
            left += 1
    
    return -1 if min_len == float('inf') else min_len