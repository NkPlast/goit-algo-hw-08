import heapq

def minimize_connection_cost(cables):
    # Перетворити список кабелів у мін-купу
    heapq.heapify(cables)
    
    total_cost = 0

    # Повторювати доти, доки не залишиться один кабель
    while len(cables) > 1:
        # Витягти два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Об'єднати їх, додати витрати на з'єднання до загальних витрат
        cost = first + second
        total_cost += cost
        
        # Додати новий кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print(f"Мінімальні витрати на з'єднання: {minimize_connection_cost(cables)}")
