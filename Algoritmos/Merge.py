def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

   
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            
            # Verifica se o elemento do começo de cada lista é menor
            # Caso o elemento no começo da lista da esquerda é menor, adiciona-o
            # à lista ordenada
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Caso o elemento no começo da lista da direita é  menor, adiciona-o
            # à lista ordenada
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Caso seja o final da lista da esquerda, adicionam-se os elementos
        # da lista da direita
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Caso seja o final da lista da direita, adicionam-se os elementos
        # da lista da esquerda
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    # Se a lista contém apenas um elemento, a retorna
    if len(nums) <= 1:
        return nums

    # Divide para pegar o índice do meio
    mid = len(nums) // 2

    # Ordena e faz o merge de cada metade
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Combina as listas em uma só
    return merge(left_list, right_list)


