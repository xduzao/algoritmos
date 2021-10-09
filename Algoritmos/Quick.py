# Existem diferentes formas de particionar o Quick Sort,
# essa é a implementação do Tony Hoare, criador do algoritmo.
def partition(nums, low, high):
    # Seleciona-se o elemento do meio para ser o pivô.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Se um elemento em i (à esquerda do pivô) 
        # é maior que o elemento em j (à direita), 
        # então é feita a troca
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    
    # Função auxiliar que será chamada recursivamente
    def _quick_sort(items, low, high):
        if low < high:
            # Este é o índice depois do pivô, 
            # onde a lista é dividida
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)





