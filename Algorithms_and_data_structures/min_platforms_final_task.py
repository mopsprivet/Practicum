# id посылки: 142479599

def min_amount_of_platforms(weights: list[int], limit: int) -> int:
    """Функция для поиска минимального кол-ва платформ
    для перевозки роботов."""
    
    sorted_weights: list[int] = sorted(weights)
    num_of_robot_pairs: int = 0 
    easier_robot: int = 0 
    heavier_robot: int = len(sorted_weights) - 1 
    
    while easier_robot < heavier_robot:
        if sorted_weights[easier_robot] + sorted_weights[heavier_robot] <= limit:
            num_of_robot_pairs += 1
            easier_robot += 1
        heavier_robot -= 1
    
    num_of_platforms = len(weights) - num_of_robot_pairs 
    return num_of_platforms


if __name__ == '__main__': 
    weights: list[int] = [int(item) for item in input().split()]
    limit: int = int(input()) 
    print(min_amount_of_platforms(weights, limit)) 
