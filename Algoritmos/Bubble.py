def bubble_sort(nums):
    # Define swapped como True para que o loop seja executado pelo menos um vez
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap dos elementos
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Define swapped como true para que o loop seja executado novamente
                swapped = True


