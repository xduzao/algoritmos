def insertion_sort(nums):
    # Começa pelo segundo elemento, assume-se que o 
    # primeito elemento já está ordenado
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # Mantém uma referência do índice do elemento anterior
        j = i - 1
        # Move todos os elementos do segmento ordenado 
        # para frente, caso eles sejam
        # maiores que o item que está sendo inserido
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Insere o item
        nums[j + 1] = item_to_insert


